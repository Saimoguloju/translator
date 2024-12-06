from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize the Streamlit app
st.set_page_config(page_title="Translator")

st.header("English to Telugu Translator")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Create separate boxes for input and output
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input (English)")
    input_text = st.text_area("Enter your text here:", key="input")

with col2:
    st.subheader("Output (Telugu)")
    if 'translated_text' not in st.session_state:
        st.session_state['translated_text'] = ""
    translated_text = st.text_area("Translation will appear here:", value=st.session_state['translated_text'], disabled=True)

# Submit button for translation
if st.button("Translate"):
    if input_text:
        response = get_gemini_response("translate English to Telugu: " + input_text)
        
        # Collecting the translation response
        translated_response = ""
        for chunk in response:
            translated_response += chunk.text
        
        # Update session state with the translation
        st.session_state['translated_text'] = translated_response
        st.session_state['chat_history'].append(("You", input_text))
        st.session_state['chat_history'].append(("Bot", translated_response))

# Display chat history
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
