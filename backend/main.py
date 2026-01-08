from fastapi import FastAPI, UploadFile
from resume_parser import extract_text

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile):
    text = extract_text(file.file)
    return {"extracted_text": text[:2000]}  # first 2000 chars
