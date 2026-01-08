# app.py

import streamlit as st
import tempfile
from pipeline import run_resume_matching

st.set_page_config(page_title="Intelligent Resume Screener", layout="centered")

st.title("📄 Intelligent Resume Screener & Job Matcher")

st.markdown(
    """
Upload a resume and paste a job description to evaluate
semantic match and identify missing skills.
"""
)

# Upload resume
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
jd_text = st.text_area("Paste Job Description", height=250)

# Button
if st.button("Analyze Resume"):
    if uploaded_resume is None or jd_text.strip() == "":
        st.error("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_resume.read())
                resume_path = tmp.name

            results = run_resume_matching(resume_path, jd_text)

        st.success("Analysis Complete!")

        # Results
        st.subheader(f"✅ Match Score: {results['match_score']}%")
        score = float(results["match_score"]) / 100
        score = max(0.0, min(score, 1.0))  # clamp
        st.progress(score)

        st.subheader("📌 Extracted Resume Skills")
        st.write(results["resume_skills"])

        st.subheader("📌 Job Description Skills")
        st.write(results["jd_skills"])

        st.subheader("⚠️ Missing Skills")
        if results["missing_skills"]:
            st.write(results["missing_skills"])
        else:
            st.write("No missing skills detected 🎉")
