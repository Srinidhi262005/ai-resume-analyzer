# app/routes/ats_checker.py
from flask import Blueprint, render_template, request
from flask_login import login_required

ats_checker_bp = Blueprint('ats_checker_bp', __name__)

@ats_checker_bp.route('/', methods=['GET', 'POST'])  # ✅ just '/' since url_prefix adds the prefix
@login_required
def index():
    results = None
    if request.method == 'POST':
        resume_file = request.files.get('resume_file')
        if resume_file:
            results = {
                'score': 78,
                'issues': ['No keywords', 'Lacks job title', 'No section headers']
            }
    return render_template('dashboard/ats_checker.html', results=results)








