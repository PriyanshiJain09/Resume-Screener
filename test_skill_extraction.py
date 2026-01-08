import os
from skill_extractor import extract_skills_from_text

DEBUG_FOLDER = "debug_output"

for file in os.listdir(DEBUG_FOLDER):
    if file.endswith(".txt"):
        with open(os.path.join(DEBUG_FOLDER, file), "r", encoding="utf-8") as f:
            text = f.read()

        skills = extract_skills_from_text(text)
        print(file, "→", skills)
