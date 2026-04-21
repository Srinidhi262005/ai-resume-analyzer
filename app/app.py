from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

# Initialize extensions globally
db = SQLAlchemy()
login_manager = LoginManager()

# User model with UserMixin for Flask-Login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    # Add email, password hash, etc. as needed

def create_app():
    app = Flask(__name__, static_folder='static')  # ✅ This line already includes static folder
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)

    # Set the login view
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ✅ Import blueprints inside the function (not at top level)
    from app.routes.auth import auth as auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.main import main_bp

    # ✅ Register blueprints with proper prefixes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(main_bp)  # default for homepage

    return app

# Optional CLI test
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)







