# pipeline.py

from .resume_parser import extract_text_from_pdf, clean_text
from .skill_extractor import extract_skills_from_text
from .jd_parser import clean_jd_text
from .jd_skill_extractor import extract_jd_skills
from .semantic_matcher import compute_semantic_match
from .skill_gap_analyzer import find_missing_skills


def run_resume_matching(resume_pdf_path, jd_text):
    # Resume processing
    raw_resume = extract_text_from_pdf(resume_pdf_path)
    resume_text = clean_text(raw_resume)
    resume_skills = extract_skills_from_text(resume_text)

    # JD processing
    jd_text_clean = clean_jd_text(jd_text)
    jd_skills = extract_jd_skills(jd_text_clean)

    # Matching
    match_score = compute_semantic_match(resume_text, jd_text_clean)
    
    missing_skills = find_missing_skills(resume_skills, jd_skills)

    return {
        
        "match_score": float(match_score),
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "missing_skills": missing_skills
    }
print("pipeline.py loaded")
print(dir())
