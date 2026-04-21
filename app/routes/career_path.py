# app/routes/career_path.py
from flask import Blueprint, render_template, request

career_path_bp = Blueprint('career_path', __name__)

@career_path_bp.route('/dashboard/career-path', methods=['GET', 'POST'])
def career_predictor():
    prediction = None
    if request.method == 'POST':
        resume_text = request.form.get('resume_text')
        if resume_text:
            # TODO: Replace this dummy logic with your AI model for career prediction
            prediction = ['Software Engineer', 'Team Lead', 'Engineering Manager']
    return render_template('dashboard/career_predictor.html', prediction=prediction)

