import fitz  # PyMuPDF
import re
import os


def extract_text_from_pdf(pdf_path):
    """
    Extracts raw text from a PDF resume using PyMuPDF.
    """
    doc = fitz.open(pdf_path)
    text = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text("text")
        if page_text:
            text.append(page_text)

    doc.close()
    return "\n".join(text)


def clean_text(text):
    """
    Light cleaning to preserve maximum semantic content.
    """
    # Normalize line breaks but keep paragraph structure
    text = text.replace("\r", "\n")
    text = re.sub(r'\n{2,}', '\n\n', text)

    # Remove non-informative symbols but KEEP important ones
    text = re.sub(r'[•●■◆►▶]', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove weird unicode

    # Normalize spaces
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()


def parse_and_debug_all_resumes(
    resume_folder="sample_data/resumes",
    debug_folder="debug_output"
):
    """
    Parses all resumes and saves debug text files
    with the same name as the PDF.
    """

    if not os.path.exists(resume_folder):
        raise FileNotFoundError(f"Resume folder not found: {resume_folder}")

    os.makedirs(debug_folder, exist_ok=True)

    pdf_files = [f for f in os.listdir(resume_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("❌ No PDF resumes found.")
        return

    print(f"\n📄 Found {len(pdf_files)} resume PDFs\n")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(resume_folder, pdf_file)
        print(f"▶ Parsing: {pdf_file}")

        raw_text = extract_text_from_pdf(pdf_path)
        cleaned_text = clean_text(raw_text)

        # Create debug file with SAME NAME as PDF
        debug_filename = os.path.splitext(pdf_file)[0] + ".txt"
        debug_path = os.path.join(debug_folder, debug_filename)

        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(
            f"   ✔ Saved debug text | "
            f"Chars: {len(cleaned_text)} | "
            f"Words: {len(cleaned_text.split())}"
        )

    print("\n✅ All resumes parsed and saved successfully.")


if __name__ == "__main__":
    parse_and_debug_all_resumes()
