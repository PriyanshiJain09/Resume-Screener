# semantic_matcher.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Free, lightweight, CPU-friendly model
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_semantic_match(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    similarity = cosine_similarity(
        [embeddings[0]], [embeddings[1]]
    )[0][0]
    return round(similarity * 100, 2)
