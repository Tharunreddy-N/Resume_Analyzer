# tagging.py

def tag_entities(model_output):
    """
    Mock entity tagging: Tag known skills in the input text.
    Input: raw model_output (e.g., list of words or tokens)
    Output: list of (label, value) tuples
    """
    known_skills = {"python", "nlp", "machine learning", "deep learning", "sql"}
    tagged = []

    for word in model_output.split():
        cleaned_word = word.strip(".,").lower()
        if cleaned_word in known_skills:
            tagged.append(("Skill", cleaned_word.capitalize()))
        else:
            tagged.append(("Other", word))

    return tagged