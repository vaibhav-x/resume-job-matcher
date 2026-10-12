from sentence_transformers import SentenceTransformer, util
from src.skills import extract_skills

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_description):
    """Compute semantic similarity score between resume and job description."""
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    similarity = util.cos_sim(resume_embedding, jd_embedding)
    return round(float(similarity[0][0]) * 100, 2)

def compare_skills(resume_text, job_description):
    """Compare skills in resume vs job description, return matched and missing skills."""
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_description))

    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "skill_match_percent": round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0
    }
