import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    return full_text.strip()

if __name__ == "__main__":
    sample_pdf = "data/sample_earnings.pdf"
    extracted_text = extract_text_from_pdf(sample_pdf)
    with open("data/extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    print("✅ PDF text extracted and saved to data/extracted_text.txt")
