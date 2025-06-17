import streamlit as st
from model import load_model, evaluate_formality, rewrite_resume
from utils import text_diff

st.set_page_config(page_title="Smart Resume Refiner", layout="wide")
st.title("🧠 Smart Resume Refiner")

# ✅ Load spaCy model safely
load_model()

input_text = st.text_area("Paste your resume content here:", height=200)

if st.button("Refine My Resume"):
    if input_text.strip():
        score = evaluate_formality(input_text)
        refined = rewrite_resume(input_text)
        diff = text_diff(input_text, refined)

        st.subheader("🧪 Formality Score")
        st.json(score)

        st.subheader("🧾 Refined Resume")
        st.text_area("Improved version", refined, height=200)

        st.subheader("🔍 Changes Made")
        st.markdown(diff, unsafe_allow_html=True)
    else:
        st.warning("Please paste your resume text to begin.")
