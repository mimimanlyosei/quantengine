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
    risk_appetite = ""

    if request.method == "POST":
        # Initialise scenario
        scenario = Scenario(user_id=current_user.id,
            initial_investment=float(request.form.get("initial_investment")),
            expected_return=float(request.form.get("expected_return")),
            years_of_investment=int(request.form.get("years_of_investment")),
            risk_appetite=request.form.get("risk_appetite").lower()
        )

        # Validate scenario
        errors = scenario.validate()

        if errors:
            return render_template("calculate.html", errors=errors,results=results)
        else:
            base_result, optimistic_result, pessimistic_result = calculate_scenarios(
            scenario.initial_investment, scenario.expected_return, scenario.years_of_investment
            )
            results = [base_result, optimistic_result, pessimistic_result]

            scenario.base_result = base_result
            scenario.optimistic_result = optimistic_result
            scenario.pessimistic_result = pessimistic_result

            db.session.add(scenario)
            db.session.commit()
            risk_appetite = scenario.risk_appetite

    return render_template("calculate.html", errors=errors, results=results, risk_appetite=risk_appetite)
