# app/routes/job_tracker.py
from flask import Blueprint, render_template, request

job_tracker_bp = Blueprint('job_tracker', __name__)

job_entries = []  # In-memory storage for now

@job_tracker_bp.route('/dashboard/job-tracker', methods=['GET', 'POST'])
def job_tracker():
    if request.method == 'POST':
        entry = {
            'title': request.form.get('job_title'),
            'url': request.form.get('job_url'),
            'status': request.form.get('status'),
            'resume_version': request.form.get('resume_version')
        }
        job_entries.append(entry)
    return render_template('dashboard/job_tracker.html', jobs=job_entries)

