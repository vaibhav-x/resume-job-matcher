import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "technologies"],
    "experience": ["experience", "work experience", "employment"],
    "education": ["education", "academic background"],
    "projects": ["projects", "personal projects"]
}

def detect_sections(text):
    """Split resume text into sections based on common header keywords."""
    lines = text.split("\n")
    sections = {key: [] for key in SECTION_HEADERS}
    current_section = None

    for line in lines:
        line_lower = line.lower().strip()
        matched = False
        for section, keywords in SECTION_HEADERS.items():
            if any(line_lower == kw or line_lower.startswith(kw) for kw in keywords):
                current_section = section
                matched = True
                break
        if not matched and current_section:
            sections[current_section].append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}