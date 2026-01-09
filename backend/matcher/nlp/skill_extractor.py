# skill_extractor.py

from .skills_list import SKILLS

def extract_skills_from_text(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return sorted(found_skills)
