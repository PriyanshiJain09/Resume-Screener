# jd_parser.py

import re

def clean_jd_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()

def load_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return clean_jd_text(f.read())
