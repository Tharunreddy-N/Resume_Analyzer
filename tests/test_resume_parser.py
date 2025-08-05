# test_resume_parser.py

import json
from utils.resume_parser import parse_resume_text

def test_parse_sample_dataset():
    """
    Validates the resume parsing function using a pre-split JSONL test dataset.
    Each line must contain {"input": "...", "output": "..."} structure.
    """
    with open("data/resume_split_dataset.jsonl", "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            item = json.loads(line)
            parsed = parse_resume_text(item["input"])
            expected = json.loads(item["output"])
            for key in expected:
                assert parsed.get(key) == expected[key], (
                    f"Line {idx+1} - Mismatch for key '{key}':\n"
                    f"Expected: {expected[key]}\n"
                    f"Got: {parsed.get(key)}"
                )