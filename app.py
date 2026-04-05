import re

from datetime import datetime
from sqlalchemy import text
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app.config import Config
from app.models import User, Scenario
from app.calculations import calculate_scenarios
from app import db
from app.routes.auth import auth_bp
from app.routes.calculate import calculate_bp
from app.routes.history import history_bp




login_manager = LoginManager()


def create_app():
    '''
    This function creates an instance of my app.
    This will later allow me to duplicate as as when needed and test/reconfigure independently.
    '''

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(calculate_bp)
    app.register_blueprint(history_bp)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @app.route("/health/db")
    def health_db():
        try:
            db.session.execute(text("SELECT 1"))
            return {"db": "ok"}, 200
        except Exception as e:
            return{"db": "error", "detail": str(e)}, 500

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/dashboard/<name>")
    def dashboard(name):
        return render_template("dashboard.html", name=name)

    @app.route("/404")
    def error_404():
        return render_template("404.html")

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    return app





if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=5555, debug=True)