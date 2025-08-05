import os
import json
from utils.parser_pipeline import process_resume_file

input_dir = "data/input"
output_dir = "data/output/batch_results"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith((".pdf", ".docx", ".txt")):
        file_path = os.path.join(input_dir, filename)
        print(f"Processing: {filename}")
        result = process_resume_file(file_path)
        json_filename = f"{os.path.splitext(filename)[0]}.json"
        with open(os.path.join(output_dir, json_filename), "w") as f:
            json.dump(result, f, indent=4)

print("✅ All resumes processed in batch mode!")