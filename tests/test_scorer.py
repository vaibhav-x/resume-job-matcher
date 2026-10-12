from src.parser import extract_resume_text, clean_raw_text
from src.scorer import compute_similarity

SAMPLE_JOB_DESCRIPTION = """
We are looking for a Machine Learning Intern with experience in Python,
TensorFlow, and NLP. The ideal candidate should have hands-on experience
with data preprocessing, model training, and deploying ML pipelines.
Familiarity with Pandas, NumPy, and scikit-learn is required. Experience
with semantic search, embeddings, or retrieval systems like FAISS is a
strong plus. Strong communication skills and ability to work in a team
are essential.
"""

if __name__ == "__main__":
    raw = extract_resume_text("data/sample_resume.pdf")
    cleaned = clean_raw_text(raw)

    score = compute_similarity(cleaned, SAMPLE_JOB_DESCRIPTION)
    print(f"Match Score: {score}%")