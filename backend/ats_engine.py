import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text

def extract_keywords(job_desc):
    job_desc = clean_text(job_desc)
    words = job_desc.split()

    stopwords = ["and","or","the","with","for","a","an","to","of","in","on","is","are","as","by"]
    keywords = [w for w in words if w not in stopwords and len(w) > 2]

    return list(set(keywords))

def calculate_ats_score(resume_text, job_desc):
    resume_text = clean_text(resume_text)
    keywords = extract_keywords(job_desc)

    matched = [kw for kw in keywords if kw in resume_text]

    score = (len(matched) / len(keywords)) * 100 if keywords else 0

    return round(score, 2), matched, keywords
