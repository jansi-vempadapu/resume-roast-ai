from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_resume(resume_text, job_desc):
    prompt = f"""
You are an ATS resume evaluator.

Resume:
{resume_text}

Job Description:
{job_desc}

Return JSON with:
- ats_score
- missing_keywords
- weak_points
- improved_bullets
- hiring_verdict
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
