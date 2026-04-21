from flask import Flask
from app.extensions import db, login_manager, migrate
from app.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='your-secret-key',
        SQLALCHEMY_DATABASE_URI='sqlite:///site.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Core blueprints (must exist)
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    # Optional blueprints (safe import)
    optional_blueprints = [
        ('app.routes.ats_checker', 'ats_checker_bp', '/dashboard/ats'),
        ('app.routes.grammar_checker', 'grammar_checker_bp', '/dashboard/grammar')
    ]

    for module_path, bp_name, url_prefix in optional_blueprints:
        try:
            mod = __import__(module_path, fromlist=[bp_name])
            bp = getattr(mod, bp_name)
            app.register_blueprint(bp, url_prefix=url_prefix)
        except (ImportError, AttributeError) as e:
            print(f"[!] Skipping {bp_name}: {e}")

    # Show registered routes for debugging
    with app.app_context():
        print("\n[*] Registered Routes:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint} -> {rule.rule}")
        print()

    return app


































