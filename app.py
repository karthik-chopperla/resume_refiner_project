import streamlit as st
from model import evaluate_formality, rewrite_resume
from utils import text_diff

st.set_page_config(page_title="Smart Resume Refiner", layout="wide")

st.title("🧠 Smart Resume Refiner")
st.write("Upload your resume and get suggestions to make it more professional and formal.")

uploaded_file = st.file_uploader("Upload your resume (TXT only)", type=["txt"])

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Original Resume")
    st.text_area("Original Text", resume_text, height=300, key="original")

    formality_score = evaluate_formality(resume_text)
    st.write(f"### Formality Score: {formality_score:.2f} / 1.0")

    improved_text = rewrite_resume(resume_text)
    st.subheader("✨ Improved Resume")
    st.text_area("Refined Text", improved_text, height=300, key="refined")

    st.subheader("🔍 Changes Made")
    diff = text_diff(resume_text, improved_text)
    st.markdown(diff, unsafe_allow_html=True)