from fastapi import FastAPI, UploadFile, Form
from resume_parser import extract_text
from ai_engine import analyze_resume
from ats_engine import calculate_ats_score

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile, job_desc: str = Form(...)):
    resume_text = extract_text(file.file)

    ats_score, matched, all_keywords = calculate_ats_score(resume_text, job_desc)

    ai_result = analyze_resume(resume_text, job_desc)

    return {
        "ats_score": ats_score,
        "matched_keywords": matched,
        "missing_keywords": list(set(all_keywords) - set(matched)),
        "ai_analysis": ai_result
    }
