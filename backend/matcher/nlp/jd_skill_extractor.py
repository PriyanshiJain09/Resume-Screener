# jd_skill_extractor.py

from .skills_list import SKILLS

def extract_jd_skills(jd_text):
    jd_text = jd_text.lower()
    found_skills = set()

    for skill in SKILLS:
        if skill in jd_text:
            found_skills.add(skill)

    return sorted(found_skills)
