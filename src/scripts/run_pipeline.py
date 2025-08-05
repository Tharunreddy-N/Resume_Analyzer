# run_pipeline.py

from utils.parser import extract_resume_text
from utils.cleaner import parse_resume_sections
from utils.tagging import tag_entities
from utils.formatter import format_result
from models.model_selector import select_model

def main():
    file_path = "sample_resume.pdf"
    text = extract_resume_text(file_path)

    # Choose model (can be 'bigbird' or 'longformer')
    model = select_model("longformer")
    prediction = model.predict(text)

    # Extract contact info
    contact_info = parse_resume_sections(text)

    # Tag and format entities
    tagged = tag_entities(text)
    formatted = format_result(tagged)

    # Print results
    print("=== Contact Info ===")
    print(contact_info)
    print("\n=== Skills from Model ===")
    print(prediction.get("skills", []))
    print("\n=== Structured Entities ===")
    print(formatted)

if __name__ == "__main__":
    main()