import argparse
import json
import os
from src.preprocessing.parser import extract_resume_text
from src.utils.resume_parser import parse_resume_text

def main():
    parser = argparse.ArgumentParser(description="Resume Parser CLI")
    parser.add_argument("--input", required=True, help="Path to resume file (PDF or DOCX)")
    parser.add_argument("--json", action="store_true", help="Output parsed resume in JSON format")
    parser.add_argument("--output", type=str, help="Path to save the output JSON file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"❌ File not found: {args.input}")
        return

    try:
        text = extract_resume_text(args.input)
        parsed = parse_resume_text(text)

        if args.json:
            json_data = json.dumps(parsed, indent=2)
            if args.output:
                with open(args.output, "w", encoding="utf-8") as out_file:
                    out_file.write(json_data)
                print(f"✅ JSON output saved to {args.output}")
            else:
                print(json_data)
        else:
            print("\n✅ Resume Text:\n")
            print(text[:1000])  # preview first 1000 chars
            print("\n🔍 Parsed Resume Fields:")
            for key, value in parsed.items():
                print(f"{key.capitalize()}: {value}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()