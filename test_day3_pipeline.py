# test_day3_pipeline.py

import json
from resume_parser import parse_and_debug_all_resumes
from jd_parser import load_job_description
from jd_skill_extractor import extract_jd_skills
from semantic_matcher import compute_semantic_match
from skill_gap_analyzer import find_missing_skills

# Pick ONE resume & ONE JD for testing
resume_id = "10624813"
jd_path = "sample_data/job_descriptions/jd2.txt"

# Load resume text
with open(f"debug_output/{resume_id}.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

# Load resume skills
with open(f"structured_output/{resume_id}.json", "r", encoding="utf-8") as f:
    resume_data = json.load(f)

resume_skills = resume_data["skills"]

# Load JD
jd_text = load_job_description(jd_path)
jd_skills = extract_jd_skills(jd_text)

# Compute results
match_score = compute_semantic_match(resume_text, jd_text)
missing_skills = find_missing_skills(resume_skills, jd_skills)

print("\n=== MATCH RESULT ===")
print("Match Score:", match_score, "%")
print("Resume Skills:", resume_skills)
print("JD Skills:", jd_skills)
print("Missing Skills:", missing_skills)
