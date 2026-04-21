# app/routes/resume_rewriter.py
from flask import Blueprint, render_template, request

resume_rewriter_bp = Blueprint('resume_rewriter', __name__)

@resume_rewriter_bp.route('/dashboard/resume-rewriter', methods=['GET', 'POST'])
def resume_rewriter():
    rewritten = None
    if request.method == 'POST':
        text = request.form.get('resume_text')
        tone = request.form.get('tone')
        if text and tone:
            # Dummy rewritten logic (replace with AI model)
            rewritten = f"({tone.capitalize()} tone): Improved version of - {text}"
    return render_template('dashboard/resume_rewriter.html', rewritten=rewritten)
