from src.parser import extract_resume_text, clean_raw_text
from src.sections import detect_sections
from src.skills import extract_skills

if __name__ == "__main__":
    raw = extract_resume_text("data/sample_resume.pdf")
    cleaned = clean_raw_text(raw)
    print(cleaned)
    print("=" * 40)
    sections = detect_sections(cleaned)

    for section, content in sections.items():
        print(f"--- {section.upper()} ---")
        print(content if content else "(nothing detected)")
        print()

    print("=== EXTRACTED SKILLS ===")
    all_skills = extract_skills(cleaned)
    print(all_skills if all_skills else "(no skills matched)")
    