import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate, LLMChain

# Set up OpenAI API key
openai_api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize LLM models
gpt3_model = ChatOpenAI(model_name="gpt-3.5-turbo-0125")  # use "gpt-4o" for new GPT-4 model
gpt4_model = ChatOpenAI(model_name="gpt-4o")

# Define sales pitch template
sales_template = """
The following is the description of the crash course 'Build Fast with AI' offers

{course_information}

Based on the above information, create a sales pitch for a person with the following persona:

Name : {name}
Occupation: {occupation}

Write about the points below and answer them in bullet points which are easy to read and interpret on the go.
1. How is Generative AI applicable in {occupation} field. (bullet points)
2. Applications of Generative AI in general. (bullet points)
3. Recent Generative AI innovations in {occupation}. (bullet points)
4. Convince how will this course help them boost their career in {occupation}. (bullet points)

Include a part which will highlight the use of the course or specifically generative AI for the Occupation {occupation} and justify it too.

The output shouldn't assume responses from the person talking to and should only give all the required things that are asked. Write "Client Response:" between 2 points of a sales pitch as it would be in a real world scenario.
The sales pitch should contain the script the salesperson can say in the first call.
"""

sales_prompt_template = PromptTemplate(template=sales_template, input_variables=['course_information', 'name', 'occupation'])

# Create LLMChain
from langchain import LLMChain
sales_persona_chain = sales_prompt_template | gpt4_model

# Streamlit app
st.title("Sales Pitch Generator")

# Input fields
course_information = st.text_area("Course Information")
name = st.text_input("Name")
occupation = st.text_input("Occupation")

# Generate sales pitch
if st.button("Generate Sales Pitch"):
    # Ensure all inputs are provided
    if not course_information or not name or not occupation:
        st.error("Please fill in all the fields.")
    else:
        # Generate the response
        try:
            response = sales_persona_chain.invoke({
                "course_information": course_information,
                "name": name,
                "occupation": occupation
            })
            
            # Display parsed output
            st.markdown("## Sales Pitch")
            for point in response.content.split("\n"):
                if point.strip():
                    if point.startswith("1.") or point.startswith("2.") or point.startswith("3.") or point.startswith("4."):
                        st.markdown(f"**{point.strip()}**")
                    elif point.startswith("Client Response:"):
                        st.markdown(f"> {point.strip()}")
                    else:
                        st.markdown(f"- {point.strip()}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
