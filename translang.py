from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(
    page_title="AI-Powered Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.header("🌍 AI-Powered Language Translator")

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("AIzaSyBcqyRGGui_5PEOsoYHSW2BiipccOiqSEM")

if not api_key:
    st.error("API Key not found. Please check your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

# UI
st.title("Language Translator")

text = st.text_area("Enter Text")
source_lang = st.text_input("Source Language")
target_lang = st.text_input("Target Language")

if st.button("Translate"):
    if text and source_lang and target_lang:
        result = translate_text(text, source_lang, target_lang)
        st.success(result)
    else:
        st.warning("Please fill all fields")

