def calculate_ats_score(resume_skills, job_skills):
    """
    Compare resume skills with job description skills.
    Returns the score, matched skills, and missing skills.
    """

    resume_set = {skill.lower() for skill in resume_skills}
    job_set = {skill.lower() for skill in job_skills}

    if not job_set:
        return {
            "ats_score": 0.0,
            "matched_skills": [],
            "missing_skills": [],
            "message": "No skills found in the job description."
        }

    matched = sorted(resume_set & job_set)
    missing = sorted(job_set - resume_set)

    score = round((len(matched) / len(job_set)) * 100, 2)

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }