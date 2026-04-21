from flask import Blueprint, render_template, request

grammar_checker_bp = Blueprint('grammar_checker', __name__)

@grammar_checker_bp.route('/grammar-checker', methods=['GET', 'POST'])
def grammar_checker():
    feedback = None
    if request.method == 'POST':
        text = request.form.get('resume_text')
        if text:
            # Dummy suggestion engine - replace with real grammar checking logic later
            feedback = [
                'Consider changing "lead" to "led"',
                'Use active voice in achievements',
                'Fix punctuation in bullet points',
                'Avoid vague phrases like "worked on..."',
                'Quantify results when possible (e.g., "increased sales by 20%")'
            ]
    return render_template('grammar_checker.html', feedback=feedback)


