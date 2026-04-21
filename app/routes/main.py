from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
import os

from app.forms import (
    UploadForm, CareerPathForm, ATSCheckForm, GrammarCheckForm,
    LinkedInAnalyzerForm, InterviewReadinessForm, JobTrackerForm,
    ResumeRewriterForm, VisualResumeBuilderForm
)
from app.ai import (
    extract_text_from_pdf, ats_scoring, grammar_readability, 
    career_prediction, linkedin_analysis, interview_readiness, resume_rewriter
)

main_bp = Blueprint('main', __name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Placeholder Job Tracker list (In production, replace with DB model)
job_list = []

# ---------------- Dashboard / Home ----------------
@main_bp.route('/')
def home():
    return render_template('index.html')


# ---------------- 2. Resume Upload & Parsing ----------------
@main_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_resume():
    form = UploadForm()
    results = None
    if form.validate_on_submit():
        extracted_text = ""
        for file in form.resume_files.data:
            filepath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(filepath)
            
            if file.filename.endswith('.pdf'):
                with open(filepath, 'rb') as f:
                    extracted_text += extract_text_from_pdf(f) + "\n"

        jd_text = form.jobdesc_text.data or ""
        jd_file = form.jobdesc_file.data
        if jd_file and jd_file.filename.endswith('.pdf'):
            filepath = os.path.join(UPLOAD_FOLDER, secure_filename(jd_file.filename))
            jd_file.save(filepath)
            with open(filepath, 'rb') as f:
                jd_text += extract_text_from_pdf(f) + "\n"

        from app.ai import extract_skills, ats_scoring
        skills = extract_skills(extracted_text)
        
        results = {'skills': skills}
        if jd_text.strip():
            ats_results = ats_scoring(extracted_text, jd_text)
            results.update(ats_results)

        flash('Resume uploaded and processed successfully.', 'success')
        return render_template('upload.html', form=form, results=results)

    return render_template('upload.html', form=form, results=results)


# ---------------- 5. ATS Scoring ----------------
@main_bp.route('/ats-check', methods=['GET', 'POST'])
@login_required
def ats_check():
    form = ATSCheckForm()
    results = {}
    if form.validate_on_submit():
        resume_text = form.resume_text.data
        job_desc_text = form.job_description_text.data or ""
        
        results = ats_scoring(resume_text, job_desc_text)
        flash("ATS analysis complete.", "success")

    return render_template('dashboard/ats_checker.html', form=form, results=results)


# ---------------- 6. Grammar & Readability ----------------
@main_bp.route('/grammar-check', methods=['GET', 'POST'])
@login_required
def grammar_check():
    form = GrammarCheckForm()
    feedback = []

    if form.validate_on_submit():
        text = form.text_to_check.data
        feedback = grammar_readability(text)
        flash("Grammar and readability check complete.", "info")

    return render_template('dashboard/grammar_checker.html', form=form, feedback=feedback)


# ---------------- 7. Career Prediction ----------------
@main_bp.route('/career-path', methods=['GET', 'POST'])
@login_required
def career_path():
    form = CareerPathForm()
    prediction = []

    if form.validate_on_submit():
        skills_text = form.current_skills.data + " " + (form.interests.data or "")
        prediction = career_prediction(skills_text)
        flash("Career path successfully predicted!", "info")

    return render_template('dashboard/career_predictor.html', form=form, prediction=prediction)


# ---------------- 8. LinkedIn Analyzer ----------------
@main_bp.route('/linkedin-analyzer', methods=['GET', 'POST'])
@login_required
def linkedin_analyzer():
    form = LinkedInAnalyzerForm()
    feedback = []

    if form.validate_on_submit():
        linkedin_text = form.linkedin_text.data
        resume_text = form.resume_text.data
        feedback = linkedin_analysis(linkedin_text, resume_text)
        flash("LinkedIn profile comparison complete.", "info")

    return render_template('dashboard/linkedin_analyzer.html', form=form, feedback=feedback)


# ---------------- 9. Interview Readiness ----------------
@main_bp.route('/interview-readiness', methods=['GET', 'POST'])
@login_required
def interview_readiness_route():
    form = InterviewReadinessForm()
    results = {}

    if form.validate_on_submit():
        resume_text = form.resume_text.data
        results = interview_readiness(resume_text)
        flash("Interview readiness analysis complete.", "info")

    return render_template('dashboard/interview_readiness.html', form=form, results=results)


# ---------------- 10. Job Tracker ----------------
@main_bp.route('/job-tracker', methods=['GET', 'POST'])
@login_required
def job_tracker():
    form = JobTrackerForm()
    if form.validate_on_submit():
        job_list.append({
            'job_title': form.job_title.data,
            'company_name': form.company_name.data,
            'job_url': form.job_url.data,
            'resume_version': form.resume_version.data,
            'status': form.status.data,
            'notes': form.notes.data
        })
        flash(f"Job application for {form.company_name.data} added to tracker.", "success")
        return redirect(url_for('main.job_tracker'))

    return render_template('dashboard/job_tracker.html', form=form, jobs=job_list)


# ---------------- Resume Rewriter ----------------
@main_bp.route('/resume-rewriter', methods=['GET', 'POST'])
@login_required
def resume_rewriter_route():
    form = ResumeRewriterForm()
    rewritten_text = ""

    if form.validate_on_submit():
        original_text = form.resume_text.data
        rewritten_text = resume_rewriter(original_text)
        flash("Resume sections successfully rewritten!", "success")

    return render_template('dashboard/resume_rewriter.html', form=form, rewritten_text=rewritten_text)


# ---------------- Visual Resume ----------------
@main_bp.route('/visual-resume', methods=['GET', 'POST'])
@login_required
def visual_resume():
    form = VisualResumeBuilderForm()
    if form.validate_on_submit():
        data = {
            'full_name': form.full_name.data,
            'email': form.email.data,
            'phone': form.phone.data,
            'summary': form.summary.data,
            'skills': form.skills.data,
            'experience': form.experience.data,
            'education': form.education.data,
        }
        flash("Visual resume ready for preview.", "success")
        return render_template('dashboard/resume_preview.html', data=data)

    return render_template('dashboard/visual_bulider.html', form=form)
