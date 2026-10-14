import streamlit as st
import tempfile
import os

from src.parser import extract_resume_text, clean_raw_text
from src.scorer import compute_similarity, compare_skills

st.set_page_config(page_title="Resume-Job Match Scorer", page_icon="📄")
st.title("📄 Resume-Job Match Scorer")
st.write("Upload your resume and paste a job description to see how well they match.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the job description here", height=250)

if st.button("Analyze Match"):
    if not uploaded_file or not job_description.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        raw = extract_resume_text(tmp_path)
        cleaned = clean_raw_text(raw)
        os.remove(tmp_path)

        score = compute_similarity(cleaned, job_description)
        skill_data = compare_skills(cleaned, job_description)

        st.subheader(f"Match Score: {score}%")
        st.progress(min(int(score), 100))

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("✅ Matched Skills")
            if skill_data["matched_skills"]:
                for skill in skill_data["matched_skills"]:
                    st.write(f"- {skill}")
            else:
                st.write("None detected")

        with col2:
            st.subheader("❌ Missing Skills")
            if skill_data["missing_skills"]:
                for skill in skill_data["missing_skills"]:
                    st.write(f"- {skill}")
            else:
                st.write("None — great coverage!")

        st.caption(f"Skill coverage: {skill_data['skill_match_percent']}% of job-required skills found in resume.")