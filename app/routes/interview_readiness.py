# app/routes/interview_readiness.py
from flask import Blueprint, render_template, request

interview_readiness_bp = Blueprint('interview_readiness', __name__)

@interview_readiness_bp.route('/dashboard/interview-readiness', methods=['GET', 'POST'])
def interview_readiness():
    questions = None
    if request.method == 'POST':
        resume_text = request.form.get('resume_text')
        if resume_text:
            questions = [
                "Tell me about your last project.",
                "How do you manage deadlines?",
                "Explain your leadership experience."
            ]
    return render_template('dashboard/interview_readiness.html', questions=questions)
