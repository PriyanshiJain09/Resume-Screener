# structured_resume_builder.py

import os
import json
from skill_extractor import extract_skills_from_text

INPUT_FOLDER = "debug_output"
OUTPUT_FOLDER = "structured_output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".txt"):
        resume_id = file.replace(".txt", "")
        path = os.path.join(INPUT_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            resume_text = f.read()

        skills = extract_skills_from_text(resume_text)

        structured_data = {
            "resume_id": resume_id,
            "skills": skills
        }

        output_path = os.path.join(OUTPUT_FOLDER, resume_id + ".json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=2)

print("✅ Structured resume data created.")
