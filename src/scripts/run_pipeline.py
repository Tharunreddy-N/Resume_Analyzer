# run_pipeline.py
from src.preprocessing.parser import parse_resume
from src.preprocessing.cleaner import clean_text
from src.models.model_selector import select_model
from src.postprocessing.tagging import tag_entities
from src.postprocessing.formatter import format_result

def main():
    text = parse_resume("sample_resume.pdf")["text"]
    cleaned = clean_text(text)
    model = select_model()
    prediction = model.predict(cleaned)
    tags = tag_entities(prediction)
    result = format_result(tags)
    print(result)

if __name__ == "__main__":
    main()