import sys
import os

"""
Main entry point for running resume text extraction and parsing.
"""

# Allow importing from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.parser import extract_resume_text
from ..utils.parser import extract_resume_text
from ..utils.resume_parser import parse_resume_text

def main():
    file_path = "data/input/sample_resume.pdf"  # Change this to your actual file path

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    if not file_path.endswith((".pdf", ".docx", ".txt")):
        print("❌ Unsupported file type. Only .pdf, .docx, or .txt are supported.")
        return

    try:
        text = extract_resume_text(file_path)
        print("✅ Resume text extracted successfully!\n")
        print(text[:10000])  # Print first 10000 characters for preview

        os.makedirs("data/output", exist_ok=True)
        with open("data/output/extracted_resume.txt", "w") as f:
            f.write(text)
        print("\n📄 Extracted text saved to: data/output/extracted_resume.txt")

        parsed_data = parse_resume_text(text)
        print("\n🔍 Parsed Resume Data:")
        for key, value in parsed_data.items():
            print(f"{key.capitalize()}: {value}")
    except Exception as e:
        print(f"❌ Failed to extract resume text: {e}")

if __name__ == "__main__":
    main()
