# app.py
import streamlit as st
from model import evaluate_formality, rewrite_resume
from utils import text_diff

st.set_page_config(page_title="Smart Resume Refiner", layout="wide")

st.title("🧠 Smart Resume Refiner")

input_text = st.text_area("Paste your resume or career summary:", height=300)

if st.button("Refine Resume"):
    if input_text.strip():
        with st.spinner("Analyzing and rewriting..."):
            score = evaluate_formality(input_text)
            refined = rewrite_resume(input_text)
            diff = text_diff(input_text, refined)

        st.subheader("🔍 Formality Score")
        st.write(f"Your resume formality score: **{score * 100:.0f}%**")

        st.subheader("🪄 Refined Resume")
        st.text_area("Rewritten Version", value=refined, height=300)

        st.subheader("📊 Changes Made")
        st.markdown(diff)
    else:
        st.warning("Please paste some resume content first.")
