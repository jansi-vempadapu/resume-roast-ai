from fastapi import FastAPI, UploadFile, Form
from resume_parser import extract_text
from ai_engine import analyze_resume

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile, job_desc: str = Form(...)):
    resume_text = extract_text(file.file)
    result = analyze_resume(resume_text, job_desc)
    return {"result": result}
