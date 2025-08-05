# inference.py
# For real-time predictions

from models.model_selector import select_model
from utils.cleaner import parse_resume_sections
from utils.tagging import tag_entities
from utils.formatter import format_result

def run_inference(resume_text, model_type="longformer"):
    """
    Runs the full inference pipeline:
    1. Selects the model
    2. Runs prediction
    3. Extracts contact info
    4. Tags entities
    5. Formats results
    """
    model = select_model(model_type)
    prediction = model.predict(resume_text)

    # Step 1: Extract contact info
    contact_info = parse_resume_sections(resume_text)

    # Step 2: Tag entities
    tagged_entities = tag_entities(resume_text)

    # Step 3: Format results
    formatted_entities = format_result(tagged_entities)

    return {
        "contact_info": contact_info,
        "skills": prediction.get("skills", []),
        "embedding": prediction.get("embedding", []),
        "entities": formatted_entities
    }

# Example usage
if __name__ == "__main__":
    sample_text = "John Doe\njohn@example.com\n+1-123-456-7890\nExperienced in Python, NLP, Deep Learning."
    result = run_inference(sample_text, model_type="bigbird")
    from pprint import pprint
    pprint(result)