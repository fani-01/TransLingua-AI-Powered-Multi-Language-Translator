from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI-Powered Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- CUSTOM CSS (Dark Theme Styling) ----------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.stApp {
    background-color: #0E1117;
    color: white;
}
textarea, .stTextInput > div > div > input {
    background-color: #1E1E2F !important;
    color: white !important;
    border-radius: 10px !important;
}
.stSelectbox > div > div {
    background-color: #1E1E2F !important;
    color: white !important;
    border-radius: 10px !important;
}
.stButton > button {
    background-color: #1f77ff;
    color: white;
    border-radius: 10px;
    padding: 8px 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align: center;'>🌍 AI-Powered Language Translator</h1>", unsafe_allow_html=True)

# ---------------- LOAD API KEY ----------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# ---------------- MODEL ----------------

model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------- FUNCTION ----------------
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

# ---------------- UI ----------------
st.markdown("### 📄 Enter text to translate:")
text = st.text_area("", height=150)

st.markdown("### 🌐 Select source language:")
source_lang = st.selectbox("", ["English", "Spanish", "French", "German", "Chinese", "Hindi"])

st.markdown("### 🌍 Select target language:")
target_lang = st.selectbox("", ["English", "Spanish", "French", "German", "Chinese", "Hindi"], index=1)

if st.button("🔁 Translate"):
    if text:
        translated_text = translate_text(text, source_lang, target_lang)
        st.markdown("## 💬 Translated Text:")
        st.success(translated_text)
    else:
        st.warning("⚠️ Please enter text to translate.")

       
