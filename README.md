# 🚀 AI Resume Analyzer & Career Hub

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Flask Version](https://img.shields.io/badge/flask-3.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-purple.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

An advanced, AI-powered platform designed to help job seekers optimize their resumes, analyze ATS compatibility, and navigate their career paths with precision. Built with a stunning Glassmorphism UI and a robust Flask backend.

## ✨ Key Features

- **📄 ATS Compatibility Checker**: Automatically parses your resume against a target job description and generates a detailed Applicant Tracking System (ATS) score with actionable keyword suggestions.
- **🛣️ Career Path Predictor**: Uses Natural Language Processing (NLP) to extract skills from your profile and predict the most suitable career trajectories (e.g., Software Engineer, Data Scientist, Product Manager).
- **📝 Resume Rewriter**: AI-driven tool that refines and polishes your resume bullet points for maximum impact, transforming passive language into strong, action-oriented statements.
- **💼 LinkedIn Profile Analyzer**: Compares your resume data with your LinkedIn profile to identify missing skills and inconsistencies, ensuring a cohesive professional brand.
- **🎤 Interview Readiness Evaluator**: Analyzes your profile for critical soft skills (leadership, agile, teamwork) and generates a readiness score alongside personalized feedback.
- **📊 Personalized Job Tracker**: A built-in CRM for your job hunt. Track applications, interview stages, and notes directly from your dashboard.

## 🛠️ Technology Stack

- **Backend Framework**: Python / Flask
- **Database**: SQLite / SQLAlchemy
- **Natural Language Processing**: spaCy (`en_core_web_sm`), PyPDF2
- **Frontend / UI**: HTML5, Vanilla CSS (Dark Mode & Glassmorphism), Jinja2
- **Forms & Security**: Flask-WTF, CSRF Protection, Flask-Login, Werkzeug Security

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   
   # Download the spaCy English NLP model
   python -m spacy download en_core_web_sm
   ```

4. **Initialize the Database and Run the Application:**
   ```bash
   python run.py
   ```
   The application will be running locally at `http://127.0.0.1:5000/`.

## 🎨 UI Showcase
The application boasts a premium, fully responsive UI designed for a frictionless user experience. It features dynamic hover animations, a cohesive dark-mode color palette, and intuitive navigation across all 10 modules.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
