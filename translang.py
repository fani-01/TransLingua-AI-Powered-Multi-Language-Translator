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
# Language Selection Dropdowns
source_lang = st.selectbox(
    "🌐 Select Source Language",
    ["English", "Spanish", "French", "German", "Chinese", "Hindi"]
)

target_lang = st.selectbox(
    "🌍 Select Target Language",
    ["English", "Spanish", "French", "German", "Chinese", "Hindi"]
)

# Translate Button
if st.button("🔁 Translate"):
    if text and source_lang and target_lang:
        translated_text = translate_text(text, source_lang, target_lang)
        st.subheader("✅ Translated Text:")
        st.write(translated_text)
    else:
        st.warning("⚠️ Please fill in all fields.")

