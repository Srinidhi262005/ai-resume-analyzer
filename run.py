# run.py

from app import create_app
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Only for first-time setup; remove for production
    app.run(debug=True)

