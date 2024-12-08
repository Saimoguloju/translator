# [English to Telugu Translator](https://huggingface.co/spaces/MogulojuSai/Translator)
This project is a Streamlit-based web application that uses the Google Generative AI (Gemini Pro) model to translate text from English to Telugu. The application features a clean, user-friendly interface where users can input English text, receive a Telugu translation, and view the chat history of previous translations.

## Features
1. Real-Time Translation: Converts English input into Telugu using Google's advanced AI.
2. Interactive Interface:Two-column layout for input and output text.
3. Translation displayed instantly upon clicking the "Translate" button.
4. Chat History: Logs all input and output messages for easy reference.
5. Environment Variables: Secures API keys using the dotenv library.

## Technologies Used
1. Python: Main programming language.
2. Streamlit: Framework for creating the web app.
3. Google Generative AI (Gemini Pro): Translation and response model.
4. dotenv: For managing environment variables securely.

## Installation and Setup
### Prerequisites
1. Python 3.7 or above installed on your system.
1. A valid Google Generative AI API key.
#### Steps
##### Clone this repository:
```python
git clone https://github.com/your-username/english-to-telugu-translator.git
cd english-to-telugu-translator
```
Create and activate a virtual environment:
```python
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
Install the required dependencies:
```python
pip install -r requirements.txt
```

### Set up your environment variables:
1. Create a .env file in the project root directory.
2. Add your Google API key: env
```python
GOOGLE_API_KEY=your_google_api_key_here
```

Run the Streamlit app:
```python
streamlit run app.py
Open the app in your browser at http://localhost:8501.
```
### Usage
1. Enter text in English in the Input (English) text area.
2. Click the Translate button to generate the Telugu translation.
3. View the translated text in the Output (Telugu) section.
4. Review past translations in the Chat History section.
### File Structure
1. app.py: Main application file containing the Streamlit app logic.
2. .env: Stores environment variables (not included in the repository for security).
3. requirements.txt: Contains the Python dependencies.
4. README.md: Documentation for the project.
### Troubleshooting
1. API Key Issues: Ensure your .env file contains a valid GOOGLE_API_KEY.
2. Dependencies: Run pip install -r requirements.txt to ensure all packages are installed.
3. Port Conflicts: If port 8501 is in use, specify a different port when running Streamlit:
```python
streamlit run app.py --server.port 8502
```


### Acknowledgments
1. Streamlit Documentation
2. Google Generative AI
3. dotenv for managing environment variables.

### Image 
![alt_image](https://github.com/Saimoguloju/translator/blob/main/image.png)
   

#### Let us know if you encounter any issues or have suggestions for improvement. Happy translating! 🎉
