from fastapi import FastAPI, UploadFile, File
from app.parser import extract_text_from_pdf
from app.skills import extract_skills
from fastapi import HTTPException
from app.ats import calculate_ats_score
from fastapi import Form
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI(
    title="Smart ATS Resume Analyzer",
    description="AI-powered Resume Analyzer",
    version="1.0.0"
)

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    upload_folder = "uploads"

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Extract skills
    skills = extract_skills(extracted_text)

    return {
        "filename": file.filename,
        "message": "Resume uploaded successfully!",
        "skills": skills,
        "resume_text": extracted_text
    }


@app.post("/analyze")
def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Resume must be a PDF file."
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Please enter a job description."
        )

    resume_path = os.path.join(
        upload_folder,
        "resume_" + os.path.basename(resume.filename)
    )

    try:
        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        resume_text = extract_text_from_pdf(resume_path)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the resume PDF."
            )

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        result = calculate_ats_score(
            resume_skills,
            jd_skills
        )

        return {
            "resume_filename": resume.filename,
            "resume_skills": resume_skills,
            "job_description_skills": jd_skills,
            **result
        }

    finally:
        resume.file.close()