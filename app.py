import streamlit as st
from model import evaluate_formality, rewrite_resume
from utils import text_diff

st.set_page_config(page_title="Smart Resume Refiner", layout="wide")

st.title("🧠 Smart Resume Refiner")
st.write("Paste your resume below to get a formality score, grammar suggestions, and AI-powered rewrites.")

resume_input = st.text_area("📄 Paste Resume Text", height=300)

if st.button("✨ Refine Resume"):
    if not resume_input.strip():
        st.warning("Please enter some resume content.")
    else:
        score, issues = evaluate_formality(resume_input)
        revised = rewrite_resume(resume_input)
        comparison = text_diff(resume_input, revised)

        st.subheader("📊 Formality Score")
        st.success(f"Your Resume Formality Score: {score}/100")

        st.subheader("🔍 Identified Issues")
        st.write(f"- Long Sentences: {issues['long_sentences']}")
        st.write(f"- Contractions: {issues['contractions']}")
        st.write(f"- Passive Voice Uses: {issues['passive_voice']}")

        st.subheader("✍️ Suggested Rewrite")
        st.text_area("Rewritten Resume", revised, height=300)

        st.subheader("🧠 AI Explanation of Changes")
        st.markdown(comparison)
