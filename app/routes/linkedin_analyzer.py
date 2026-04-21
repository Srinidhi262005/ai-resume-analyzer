# app/routes/linkedin_analyzer.py
from flask import Blueprint, render_template, request

linkedin_analyzer_bp = Blueprint('linkedin_analyzer', __name__)

@linkedin_analyzer_bp.route('/dashboard/linkedin-analyzer', methods=['GET', 'POST'])
def linkedin_analyzer():
    feedback = None
    if request.method == 'POST':
        resume_text = request.form.get('resume_text')
        linkedin_text = request.form.get('linkedin_text')
        if resume_text and linkedin_text:
            # Dummy comparison logic (replace with your AI model)
            feedback = ['Mismatch in job titles', 'Experience years differ']
    return render_template('dashboard/linkedin_analyzer.html', feedback=feedback)

