from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Scenario
from app.calculations import calculate_scenarios

calculate_bp = Blueprint('calculate', __name__)

@calculate_bp.route('/calculate', methods=["GET", "POST"])
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
