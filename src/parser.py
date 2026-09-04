import pdfplumber

def extract_resume_text(pdf_path):
    """Extract raw text from a resume PDF, page by page."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def clean_raw_text(text):
    """Remove blank lines and extra whitespace from extracted text."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)