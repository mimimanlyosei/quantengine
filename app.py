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




login_manager = LoginManager()


def create_app():
    '''
    This function creates an instance of my app.
    This will later allow me to duplicate as as when needed and test/reconfigure independently.
    '''

    app = Flask(__name__)
    app.config.from_object(Config)
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
            
            # Basic validation

            # Check if username is empty
            if not (3 <= len(username) <= 80):
                errors.append("Username must be between 3 and 80 characters")

            # Check if email is empty
            if email == "":
                errors.append("Email is required")

            # Check if password is empty
            if password == "":
                errors.append("Password is required")
            elif len(password) < 8:
                errors.append("Password must be at least 8 characters")

            # Check if passwords match
            if confirm == "":
                errors.append("Please confirm your password")
            
            elif password != confirm:
                errors.append("Passwords do not match")



            # Check if username already exists
            if errors == []:
                if User.query.filter_by(username=username).first():
                    errors.append("Username already exists")
                elif User.query.filter_by(email=email).first():
                    errors.append("Email already exists")
                else:    
                    # If we get here, all validation has passed - create the user
                    password_hash = generate_password_hash(password)
                    new_user = User(username=username, email=email, password_hash=password_hash)
                    db.session.add(new_user)
                    db.session.commit()
                    flash("Registration successful! Please log in.", "success")




            if errors:
                return render_template("register.html", errors=errors)

            return redirect(url_for("login"))
        

        
        return render_template("register.html", errors=errors)





    @app.route("/login", methods=["GET", "POST"])
    def login():
        errors = []


        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                flash("Logged in successfully!", "success")
                return redirect(url_for("dashboard", name=user.username))
            else:
                errors.append("Invalid username or password")
        return render_template("login.html", errors=errors)

    

    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("index"))
    
    @app.route("/dashboard/<name>")
    def dashboard(name):
        return render_template("dashboard.html", name=name)
    

    @app.route('/calculate', methods=["GET", "POST"])
    @login_required
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
            base_result, optimistic_result, pessimistic_result = calculate_scenarios(
                initial_investment, expected_return, years_of_investment
            )
            results = [base_result, optimistic_result, pessimistic_result]

            new_scenario = Scenario(
                user_id=current_user.id,
                initial_investment=initial_investment,
                expected_return=expected_return,
                years_of_investment=years_of_investment,
                risk_appetite=risk_appetite,
                base_result=base_result,
                optimistic_result=optimistic_result,
                pessimistic_result=pessimistic_result
            )
            db.session.add(new_scenario)
            db.session.commit()

        return render_template("calculate.html", errors=errors, results=results, risk_appetite=risk_appetite)


    @app.route("/history")
    @login_required
    def history():
        scenarios = Scenario.query.filter_by(user_id=current_user.id).all()
        return render_template("history.html", scenarios=scenarios)

    @app.route("/delete_scenario/<int:scenario_id>", methods=["POST"])
    def delete_scenario(scenario_id):
        scenario = Scenario.query.get(scenario_id)
        if scenario and scenario.user_id == current_user.id:
            db.session.delete(scenario)
            db.session.commit()
            flash("Scenario deleted successfully!", "success")
        else:
            flash("Scenario not found or you don't have permission to delete it.", "error")
        return redirect(url_for("history"))

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