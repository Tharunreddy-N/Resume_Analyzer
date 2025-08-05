# postprocessing.py

def deduplicate_entities(entity_dict):
    """
    Remove duplicate values from each list in the entity dictionary.
    Example: {"Skill": ["Python", "Python"]} => {"Skill": ["Python"]}
    """
    return {label: list(set(values)) for label, values in entity_dict.items()}
