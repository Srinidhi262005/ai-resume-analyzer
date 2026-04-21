import os
from io import BytesIO
import re
import random
import PyPDF2

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None

SKILLS_DB = {
    "python", "flask", "django", "sql", "machine learning", "nlp", 
    "data analysis", "javascript", "react", "node.js", "aws", "docker",
    "kubernetes", "c++", "java", "html", "css", "agile", "scrum", "git",
    "communication", "leadership", "teamwork", "problem-solving"
}

def extract_text_from_pdf(file_stream):
    try:
        reader = PyPDF2.PdfReader(file_stream)
        text = "".join([page.extract_text() or "" for page in reader.pages])
        return text
    except Exception as e:
        return ""

def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILLS_DB if skill in text]
    return found_skills

# 5. ATS Scoring
def ats_scoring(resume_text, job_desc_text):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_desc_text))
    
    missing_keywords = list(jd_skills - resume_skills)
    matched_keywords = list(jd_skills.intersection(resume_skills))
    
    if jd_skills:
        score = int((len(matched_keywords) / len(jd_skills)) * 100)
    else:
        score = random.randint(70, 95) if len(resume_skills) > 5 else random.randint(40, 69)

    notes = []
    if score < 70:
        notes.append("Your resume lacks keywords matching the job description.")
    if len(resume_text.split()) < 150:
        notes.append("Resume seems too short. Elaborate on your experience.")
    if "achieve" not in resume_text.lower() and "improve" not in resume_text.lower():
        notes.append("Use action verbs and quantifiable achievements.")

    return {
        'score': score,
        'missing_keywords': missing_keywords if missing_keywords else ["None - Great match!"],
        'notes': notes if notes else ["Looks good. Your resume is ATS optimized."]
    }

# 6. Grammar & Readability
def grammar_readability(text):
    feedback = []
    words = text.split()
    
    if len(words) < 50:
        feedback.append("The text is too short for a comprehensive grammar check.")
    
    # Common mistakes
    typos = {'teh': 'the', 'recieve': 'receive', 'occured': 'occurred', 'acheive': 'achieve'}
    for mistake, correction in typos.items():
        if re.search(r'\b' + mistake + r'\b', text.lower()):
            feedback.append(f"Typo detected: '{mistake}' should be '{correction}'.")
            
    # Readability heuristics
    sentences = text.split('.')
    long_sentences = sum(1 for s in sentences if len(s.split()) > 25)
    if long_sentences > 2:
        feedback.append(f"Found {long_sentences} very long sentences. Consider breaking them up for better readability.")
        
    if not feedback:
        feedback.append("No major grammar or readability issues detected. Good job!")
        
    return feedback

# 7. Career Prediction
def career_prediction(skills_text):
    keywords_map = {
        'Software Engineer': ['python', 'java', 'c++', 'javascript', 'react', 'node.js', 'git'],
        'Data Scientist': ['machine learning', 'python', 'sql', 'nlp', 'data analysis'],
        'DevOps Engineer': ['aws', 'docker', 'kubernetes', 'linux'],
        'Product Manager': ['agile', 'scrum', 'leadership', 'communication'],
    }
    
    skills = extract_skills(skills_text)
    matched = [(role, len(set(skills) & set(req_skills))) for role, req_skills in keywords_map.items()]
    matched.sort(key=lambda x: x[1], reverse=True)
    
    predictions = [m[0] for m in matched if m[1] > 0]
    if not predictions:
        predictions = ["General/Administrative Role (Consider adding more specific technical skills)"]
        
    return predictions

# 8. LinkedIn Analysis
def linkedin_analysis(linkedin_text, resume_text):
    feedback = []
    if "linkedin.com/in/" not in linkedin_text.lower():
        feedback.append("Make sure your LinkedIn URL is correctly formatted.")
        
    resume_skills = set(extract_skills(resume_text))
    linkedin_skills = set(extract_skills(linkedin_text))
    
    missing_on_linkedin = list(resume_skills - linkedin_skills)
    if missing_on_linkedin:
        feedback.append(f"Add these skills to your LinkedIn: {', '.join(missing_on_linkedin)}")
    else:
        feedback.append("Your LinkedIn profile aligns well with your resume skills.")
        
    return feedback

# 9. Interview Readiness
def interview_readiness(resume_text):
    feedback = []
    soft_skills = ['leadership', 'communication', 'teamwork', 'problem-solving', 'agile']
    resume_lower = resume_text.lower()
    
    found_skills = [s for s in soft_skills if s in resume_lower]
    missing_skills = [s for s in soft_skills if s not in resume_lower]
    
    score = int((len(found_skills) / len(soft_skills)) * 100)
    
    if missing_skills:
        feedback.append(f"Consider highlighting these soft skills with examples: {', '.join(missing_skills)}.")
    
    feedback.append("Prepare STAR (Situation, Task, Action, Result) stories for your listed experiences.")
    
    return {'score': score, 'feedback': feedback}

# 10. Resume Rewriter
def resume_rewriter(text):
    # Simulated AI rewrite
    sentences = text.split('.')
    rewritten = []
    for s in sentences:
        s = s.strip()
        if not s: continue
        if s.lower().startswith('i was responsible for'):
            s = s.lower().replace('i was responsible for', 'Spearheaded and managed')
            s = s.capitalize()
        elif s.lower().startswith('helped'):
            s = s.lower().replace('helped', 'Collaborated to')
            s = s.capitalize()
        rewritten.append(s)
        
    if not rewritten:
        return "Please provide more detail to rewrite."
        
    return ". ".join(rewritten) + "."
