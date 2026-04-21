from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from .extensions import db


# --- User Model ---
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # hashed password field


    # Relationships
    resume_analyses = db.relationship('ResumeAnalysis', backref='user', lazy=True)
    career_predictions = db.relationship('CareerPathPrediction', backref='user', lazy=True)
    ats_checks = db.relationship('ATSCheck', backref='user', lazy=True)
    grammar_checks = db.relationship('GrammarCheck', backref='user', lazy=True)
    linkedin_analyses = db.relationship('LinkedInAnalysis', backref='user', lazy=True)
    interview_readinesses = db.relationship('InterviewReadiness', backref='user', lazy=True)
    job_trackers = db.relationship('JobTracker', backref='user', lazy=True)
    resume_rewrites = db.relationship('ResumeRewriter', backref='user', lazy=True)
    visual_resumes = db.relationship('VisualResumeBuilder', backref='user', lazy=True)

# --- Resume Analysis ---
class ResumeAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resume_filename = db.Column(db.String(120), nullable=False)
    match_percent = db.Column(db.Integer)
    suggestions = db.Column(db.Text)
    motivation_tips = db.Column(db.Text)
    format_tips = db.Column(db.Text)
    job_description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Career Path Predictor ---
class CareerPathPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    current_skills = db.Column(db.Text, nullable=False)
    interests = db.Column(db.Text)
    prediction_result = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- ATS Checker ---
class ATSCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resume_text = db.Column(db.Text, nullable=False)
    ats_score = db.Column(db.Float)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Grammar Checker ---
class GrammarCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text_checked = db.Column(db.Text, nullable=False)
    corrected_text = db.Column(db.Text)
    grammar_errors = db.Column(db.Text)  # Store error descriptions or counts
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- LinkedIn Analyzer ---
class LinkedInAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    linkedin_profile_url = db.Column(db.String(255))
    analysis_summary = db.Column(db.Text)
    suggestions = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Interview Readiness ---
class InterviewReadiness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    answers_text = db.Column(db.Text)  # e.g. user input answers to questions
    readiness_score = db.Column(db.Float)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Job Tracker ---
class JobTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150))
    status = db.Column(db.String(50))  # e.g. Applied, Interview Scheduled, Offer, Rejected
    applied_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Resume Rewriter ---
class ResumeRewriter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    original_resume_text = db.Column(db.Text, nullable=False)
    rewritten_resume_text = db.Column(db.Text)
    rewrite_notes = db.Column(db.Text)  # e.g. style changes, improvements suggested
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Visual Resume Builder ---
class VisualResumeBuilder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resume_data_json = db.Column(db.Text)  # Store resume content in JSON for visual builder
    template_used = db.Column(db.String(100))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)










