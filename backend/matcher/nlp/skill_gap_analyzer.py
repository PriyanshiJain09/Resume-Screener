# skill_gap_analyzer.py

def find_missing_skills(resume_skills, jd_skills):
    return sorted(set(jd_skills) - set(resume_skills))
