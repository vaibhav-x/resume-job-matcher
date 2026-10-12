import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "technologies", "tech stack"],
    "experience": [
        "experience", "work experience", "employment",
        "internships", "internships & live projects", "internships and live projects"
    ],
    "education": ["education", "academic background"],
    "projects": [
        "projects", "personal projects",
        "internships & live projects", "internships and live projects"
    ],
    "activities": [
        "roles of responsibility", "extracurricular activities & achievements",
        "extracurricular activities and achievements", "achievements", "activities"
    ]
}

def detect_sections(text):
    """Split resume text into sections based on common header keywords."""
    lines = text.split("\n")
    sections = {key: [] for key in SECTION_HEADERS}
    current_sections = []

    for line in lines:
        line_lower = line.lower().strip()
        matched_sections = []
        for section, keywords in SECTION_HEADERS.items():
            if any(line_lower == kw or line_lower.startswith(kw) for kw in keywords):
                matched_sections.append(section)

        if matched_sections:
            current_sections = matched_sections
        elif current_sections:
            for section in current_sections:
                sections[section].append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}