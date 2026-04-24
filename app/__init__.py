import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import text

# Initialise extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    '''
    Application Factory patter.
    Creates and configures the Flask app instance.
    '''
    
    # Get the project root directory (parent of app package)
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    app = Flask(__name__,
                template_folder=os.path.join(basedir, "templates"),
                static_folder=os.path.join(basedir, "static"))

    # Load config
    from app.config import Config
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.calculate import calculate_bp
    from app.routes.history import history_bp
    from app.routes.info import info_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(calculate_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(info_bp)

    # User loader callback for Flask-Login
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # General routes
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/dashboard/<name>")
    def dashboard(name):
        return render_template("dashboard.html", name=name)
    
    @app.route("/404")
    def error_404():
        return render_template("404.html")
    
    @app.route("/health/db")
    def health_db():
        try:
            db.session.execute(text("SELECT 1"))
            return {"db": "ok"}, 200
        except Exception as e:
            return{"db": "error", "detail": str(e)}, 500
        
    # Create database tables
    with app.app_context():
        db.create_all()

    return app
