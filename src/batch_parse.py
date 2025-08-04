import os
import json
from utils.parser_pipeline import process_resume_file

input_dir = "data/input"
output_dir = "data/output/batch_results"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".pdf") or filename.endswith(".docx"):
        file_path = os.path.join(input_dir, filename)
        result = process_resume_file(file_path)
        with open(os.path.join(output_dir, f"{filename}.json"), "w") as f:
            json.dump(result, f, indent=4)

print("✅ All resumes processed in batch mode!")