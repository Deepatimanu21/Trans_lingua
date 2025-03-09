import streamlit as st
import google.generativeai as genai

# Configure Google AI API
GENAI_API_KEY = "AIzaSyA56l0W7wTIqfe99xyoMHV2bysFyVUI8Ys"  # Replace with your actual API key
genai.configure(api_key=GENAI_API_KEY)

# Function to translate text using Google's Generative AI
def translate_text(text, source_lang, target_lang):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = f"Translate the following text from {source_lang} to {target_lang}:\n{text}"
        response = model.generate_content(prompt)
        return response.text if response and hasattr(response, 'text') else "Translation failed."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="TransLingua - AI Translator", layout="centered")
st.title("🌍 TransLingua: AI-Powered Multi-Language Translator")

# User Input
text = st.text_area("Enter text to translate:", "")
languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean", "Hindi", "Arabic"]
source_lang = st.selectbox("Select source language:", languages, index=0)
target_lang = st.selectbox("Select target language:", languages, index=1)

if st.button("Translate"):
    if text.strip():
        translation = translate_text(text, source_lang, target_lang)
        st.success("### Translation Result")
        st.write(translation)
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.caption("Powered by Google's Generative AI & Streamlit")
