from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, MultipleFileField,
    TextAreaField, FileField, BooleanField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, Optional, URL
)
from flask_wtf.file import FileAllowed
from wtforms.fields import DateField
from wtforms import StringField, TextAreaField, SelectField, SubmitField



# ------------------- Authentication Forms -------------------

class RegisterForm(FlaskForm):
    """Form for user registration"""
    username = StringField('Username', validators=[
        DataRequired(), Length(min=3, max=25)
    ])
    email = StringField('Email', validators=[
        DataRequired(), Email(), Length(max=120)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6, message="Password must be at least 6 characters.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Form for user login"""
    email = StringField('Email', validators=[
        DataRequired(), Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# ------------------- Resume Upload & Analysis -------------------

class UploadForm(FlaskForm):
    """Form to upload resumes and optional job description"""
    resume_files = MultipleFileField('Upload Resume(s)', validators=[
        DataRequired(message="Please upload at least one resume."),
        FileAllowed(['pdf', 'docx'], 'Only PDF and DOCX files are allowed.')
    ])
    jobdesc_file = FileField('Upload Job Description (Optional)', validators=[
        FileAllowed(['pdf', 'docx'], 'Only PDF and DOCX files are allowed.')
    ])
    jobdesc_text = TextAreaField('Or Paste Job Description', validators=[
        Optional()
    ])
    submit = SubmitField('Analyze Resume(s)')


# ------------------- Career Guidance -------------------

class CareerPathForm(FlaskForm):
    """Form for predicting career path based on skills and interests"""
    current_skills = TextAreaField('Current Skills', validators=[
        DataRequired(), Length(max=1000)
    ])
    interests = TextAreaField('Interests (Optional)', validators=[
        Optional(), Length(max=1000)
    ])
    submit = SubmitField('Predict Career Path')


class ATSCheckForm(FlaskForm):
    """Form to check ATS compatibility"""
    resume_text = TextAreaField('Paste Resume Text', validators=[
        DataRequired(), Length(max=10000)
    ])
    job_description_text = TextAreaField('Paste Job Description (Optional)', validators=[
        Optional(), Length(max=10000)
    ])
    submit = SubmitField('Check ATS Compatibility')


class GrammarCheckForm(FlaskForm):
    """Form to check grammar in provided text"""
    text_to_check = TextAreaField('Enter Text to Check', validators=[
        DataRequired(), Length(max=5000)
    ])
    submit = SubmitField('Check Grammar')


# ------------------- LinkedIn Profile Analyzer -------------------


class LinkedInAnalyzerForm(FlaskForm):
    linkedin_text = TextAreaField('LinkedIn Profile Text / URL', validators=[DataRequired()])
    resume_text = TextAreaField('Resume Text', validators=[DataRequired()])
    submit = SubmitField('Analyze')


# ------------------- Interview Readiness -------------------


class InterviewReadinessForm(FlaskForm):
    resume_text = TextAreaField('Resume Text', validators=[DataRequired()])
    submit = SubmitField('Analyze')


# ------------------- Job Tracker -------------------

class JobTrackerForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    job_url = StringField('Job URL', validators=[DataRequired(), URL()])
    resume_version = TextAreaField('Resume Version Used', validators=[DataRequired()])
    status = SelectField(
        'Application Status', 
        choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Offer', 'Offer'), ('Rejected', 'Rejected')],
        default='Applied'
    )
    notes = TextAreaField('Notes / Feedback', validators=[Optional()])
    submit = SubmitField('Add / Update Job')


# ------------------- Resume Rewriter -------------------

class ResumeRewriterForm(FlaskForm):
    """Form to rewrite resume content"""
    resume_text = TextAreaField('Paste Resume Text', validators=[
        DataRequired(), Length(max=10000)
    ])
    submit = SubmitField('Rewrite Resume')


# ------------------- Visual Resume Builder -------------------

class VisualResumeBuilderForm(FlaskForm):
    """Form to build a visual resume"""
    full_name = StringField('Full Name', validators=[
        DataRequired(), Length(max=100)
    ])
    email = StringField('Email', validators=[
        DataRequired(), Email(), Length(max=120)
    ])
    phone = StringField('Phone Number (Optional)', validators=[
        Optional(), Length(max=20)
    ])
    summary = TextAreaField('Professional Summary (Optional)', validators=[
        Optional(), Length(max=1000)
    ])
    skills = TextAreaField('Skills (comma separated)', validators=[
        Optional(), Length(max=1000)
    ])
    experience = TextAreaField('Experience (Optional)', validators=[
        Optional(), Length(max=2000)
    ])
    education = TextAreaField('Education (Optional)', validators=[
        Optional(), Length(max=1000)
    ])
    submit = SubmitField('Build Resume')







