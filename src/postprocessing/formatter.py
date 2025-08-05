# formatter.py

def format_result(tagged_output):
    """
    Convert a list of (label, value) tuples into a structured dictionary.
    Example input: [("Skill", "Python"), ("Skill", "NLP"), ("Education", "B.Tech")]
    Output: {"Skill": ["Python", "NLP"], "Education": ["B.Tech"]}
    """
    formatted = {}
    for label, value in tagged_output:
        if label not in formatted:
            formatted[label] = []
        formatted[label].append(value)
    return formatted