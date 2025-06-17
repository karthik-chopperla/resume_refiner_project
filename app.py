# app.py (cleaned up version)

import streamlit as st
from model import evaluate_formality, rewrite_resume

st.set_page_config(page_title="Smart Resume Refiner", layout="wide")
st.title("📄 Smart Resume Refiner")

input_mode = st.radio("Choose input method", ["Upload Resume File (.txt)", "Type or Paste Resume Text"])

if input_mode == "Upload Resume File (.txt)":
    uploaded_file = st.file_uploader("Upload your resume (.txt only)", type="txt")
    resume_text = uploaded_file.read().decode("utf-8") if uploaded_file else ""
else:
    resume_text = st.text_area("Paste or type your resume here:", height=300)

if resume_text:
    st.subheader("📊 Formality Score")
    score = evaluate_formality(resume_text)
    st.write(f"**Score:** {score:.2f} / 1.0")

    st.subheader("🛠 Refined Resume")
    refined = rewrite_resume(resume_text)
    st.code(refined, language="markdown")

    # Removed differences section
    # st.subheader("🔍 Differences")
    # st.write(text_diff(resume_text, refined))
else:
    st.info("Please upload a file or paste your resume above.")
