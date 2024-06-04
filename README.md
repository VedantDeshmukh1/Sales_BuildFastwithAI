# Sales Pitch Generator

Welcome to the Sales Pitch Generator! This Streamlit app leverages OpenAI's powerful GPT-4 model to generate tailored sales pitches based on user input.

## Features

- **Easy-to-use interface**: Simply enter the course information, name, and occupation to generate a customized sales pitch.
- **Powerful AI model**: Utilizes OpenAI's GPT-4 model to create professional and compelling sales pitches.
- **Detailed output**: The sales pitch includes specific applications of Generative AI in the provided occupation, recent innovations, and convincing points on how the course will benefit the user's career.

## Installation

To run the Sales Pitch Generator locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/VedantDeshmukh1/Sales_BuildFastwithAI
    ```

2. Install the required packages:
    ```bash
    pip install -qU streamlit langchain langchain-openai
    ```

3. Set up your OpenAI API key:
    - Create a file named `.streamlit/secrets.toml` in the root of your project directory.
    - Add your OpenAI API key in the `secrets.toml` file:
      ```toml
      [secrets]
      OPENAI_API_KEY = "your-openai-api-key"
      ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser by navigating to the URL provided in the terminal after running the above command.
2. Fill in the required fields:
    - **Course Information**: Enter the details of the crash course "Build Fast with AI".
    - **Name**: Enter the name of the persona.
    - **Occupation**: Enter the occupation of the persona.
3. Click the **Generate Sales Pitch** button to generate a sales pitch.

## Example

Below is an example of how the inputs and outputs look in the app:

### Inputs

- **Course Information**:
    ```
    This crash course covers the fundamentals of Generative AI, including practical applications in various fields, recent innovations, and how to leverage AI tools for career advancement.
    ```
- **Name**: ```Vedant```
- **Occupation**: ```Intern```

### Output

**Sales Pitch**

- **How is Generative AI applicable in Intern field**:
    - Automates repetitive tasks.
    - Enhances research capabilities.
    - Assists in creating content.

- **Applications of Generative AI in general**:
    - Content creation.
    - Data analysis.
    - Predictive analytics.

- **Recent Generative AI innovations in Intern**:
    - AI-powered research tools.
    - Automated data entry systems.
    - Intelligent content recommendation engines.

- **Convince how this course will help them boost their career in Intern**:
    - Gain hands-on experience with AI tools.
    - Enhance problem-solving skills.
    - Increase employability with AI expertise.

## Contributing

We welcome contributions! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please contact [vedantdeshmukh1983@gmail.com].

---

Thank you for using the Sales Pitch Generator! Hope it helps you create compelling and effective sales pitches effortlessly.
