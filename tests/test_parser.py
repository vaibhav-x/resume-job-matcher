from src.parser import extract_resume_text, clean_raw_text
from src.sections import detect_sections

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