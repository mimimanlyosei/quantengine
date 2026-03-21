from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from sqlalchemy import text
import re

db = SQLAlchemy()
login_manager = LoginManager()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

def create_app():
    '''
    This function creates an instance of my app.
    This will later allow me to duplicate as as when needed and test/reconfigure independently.
    '''

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'this-is-a-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

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


    @app.route("/register", methods=["GET", "POST"])
    def register():
        errors = []

        
        if request.method == "POST":
            username = (request.form.get("username")or "").strip()
            email = (request.form.get("email")or "").strip()
            password = request.form.get("password")or ""
            confirm = request.form.get("confirm_password")or ""
            
            if not (3 <= len(username) <= 80):
                errors.append("Username must be between 3 and 80 characters")

            return redirect(url_for("dashboard", name=username))
        
        return render_template("register.html")


    @app.route("/login")
    def login():
        return render_template("login.html")
    
    @app.route("/logout")
    def logout():
        return render_template("logout.html")
    
    @app.route("/dashboard/<name>")
    def dashboard(name):
        return render_template("dashboard.html", name=name)
    

    @app.route('/calculate', methods=["GET", "POST"])
    def calculate():
        errors = []
        results = []
        risk_appetite = None

        if request.method == "POST":
            
            # Validate and process form data

            # Validate initial investment
            try:
                initial_investment = float(request.form.get("initial_investment"))
            except ValueError:
                errors.append("Please enter a valid initial investment amount.")
            else:
                if initial_investment <= 0:
                    errors.append("Initial investment cannot be less than £1.")
            

            # Validate expected return
            try:
                expected_return = float(request.form.get("expected_return"))
            except ValueError:
                errors.append("Please enter a valid expected return.")
            else:
                if expected_return < 0 or expected_return > 50:
                    errors.append("Expected return must be between 0% and 50%.")

            # Validate years of investment
            try:
                years_of_investment = int(request.form.get("years_of_investment"))
            except ValueError:
                errors.append("Please enter a valid number of years.")
            else:
                if years_of_investment <= 0 or years_of_investment > 70:
                    errors.append("Years of investment must be between 1 and 70.")

            # Validate risk appetite
            risk_appetite = str(request.form.get("risk_appetite"))
            if risk_appetite not in ["low", "medium", "high"]:
                errors.append("Please select a valid risk appetite.")

            if errors:
                return render_template("calculate.html", errors=errors,results=results)
            else:
                print(f"Initial Investment: {initial_investment}")
                print(f"Expected Return: {expected_return}")
                print(f"Years of Investment: {years_of_investment}")
                print(f"Risk Appetite: {risk_appetite}")
            # if we get here, all inputs are valid
            print("All inputs are valid - ready to calculate")

            # Perform calculations
            swing = 0.05
            base_rate = expected_return / 100
            optimistic_rate = base_rate + swing
            pessimistic_rate = base_rate - swing

            base_result = round(initial_investment * ((1 + base_rate) ** years_of_investment), 2)
            optimistic_result = round(initial_investment * ((1 + optimistic_rate) ** years_of_investment), 2)
            pessimistic_result = round(initial_investment * ((1 + pessimistic_rate) ** years_of_investment), 2)

            results = [base_result, optimistic_result, pessimistic_result]
            print(f"Base Result: {base_result}")
            print(f"Optimistic Result: {optimistic_result}")
            print(f"Pessimistic Result: {pessimistic_result}")

        return render_template("calculate.html", errors=errors, results=results, risk_appetite=risk_appetite)


    @app.route("/history")
    def history():
        return render_template("history.html")
    
    @app.route("/404")
    def error_404():
        return render_template("404.html")

    @login_manager.user_loader
    def load_user(user_id):
        return None


    return app





if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=5555, debug=True)