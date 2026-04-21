# app/routes/visual_builder.py
from flask import Blueprint, render_template

visual_builder_bp = Blueprint('visual_builder', __name__)

@visual_builder_bp.route('/dashboard/visual-builder')
def visual_builder():
    return render_template('dashboard/visual_resume.html')

