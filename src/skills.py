import spacy

nlp = spacy.load("en_core_web_sm")

KNOWN_SKILLS = [
    "python", "java", "javascript", "c++", "c", "sql", "r",
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
    "react", "node.js", "flask", "django", "streamlit", "fastapi",
    "docker", "kubernetes", "aws", "gcp", "azure", "git", "github",
    "html", "css", "mongodb", "mysql", "postgresql", "spacy", "bm25",
    "faiss", "beautifulsoup", "scrapy", "matplotlib", "excel", "tableau"
]
def extract_skills(text):
    """Find known tech skills mentioned in the given text."""
    text_lower = text.lower()
    found = set()
    for skill in KNOWN_SKILLS:
        if skill in text_lower:
            found.add(skill)
    return sorted(found)