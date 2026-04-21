import random

def analyze_resume_and_jd(resume_paths, job_description):
    """
    Simulate analysis of resumes against a job description.

    Parameters:
    - resume_paths: list of file paths (strings) for uploaded resumes
    - job_description: string containing job description text (can be empty or None)

    Returns:
    A list of dictionaries, one per resume, each containing:
    - filename: name of the resume file
    - match_score: int percentage matching score (simulated)
    - skills_extracted: list of skill strings extracted
    - job_suggestions: list of suggested job titles
    - positive_feedback: list of positive feedback strings
    - constructive_feedback: list of suggestions to improve resume
    - template_suggestions: list of formatting/layout tips
    - motivational_tips: list of motivational messages
    """
    results = []
    
    for path in resume_paths:
        # Extract filename from path
        filename = path.split('/')[-1] if '/' in path else path.split('\\')[-1]
        
        # Simulated data - you can replace this with real NLP/ML analysis
        skills_extracted = ["Python", "SQL", "Excel", "Machine Learning", "Communication"]
        match_score = random.randint(60, 95)
        job_suggestions = [
            "Data Analyst",
            "Business Intelligence Analyst",
            "Machine Learning Engineer",
            "Data Scientist"
        ]
        positive_feedback = [
            "Resume contains relevant keywords.",
            "Strong technical background detected.",
            "Experience aligns with job role."
        ]
        constructive_feedback = [
            "Add quantifiable achievements (e.g., improved efficiency by 20%).",
            "Include more soft skills such as teamwork or leadership.",
            "Make sure formatting is ATS-friendly (avoid tables)."
        ]
        template_suggestions = [
            "Use a consistent font and spacing.",
            "Avoid columns and graphics in your resume.",
            "Stick to a clean, professional layout."
        ]
        motivational_tips = [
            "Keep applying – every resume is a step closer.",
            "Customize your resume for each role to stand out.",
            "Stay confident – you are more capable than you think."
        ]
        
        results.append({
            "filename": filename,
            "match_score": match_score,
            "skills_extracted": skills_extracted,
            "job_suggestions": job_suggestions,
            "positive_feedback": positive_feedback,
            "constructive_feedback": constructive_feedback,
            "template_suggestions": template_suggestions,
            "motivational_tips": motivational_tips
        })
    
    return results

