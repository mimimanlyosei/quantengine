from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Scenario

history_bp = Blueprint('history', __name__)

@history_bp.route("/history")
@login_required
def history():
    scenarios = Scenario.query.filter_by(user_id=current_user.id).all()
    return render_template("history.html", scenarios=scenarios)

@history_bp.route("/delete_scenario/<int:scenario_id>", methods=["POST"])
def delete_scenario(scenario_id):
    scenario = Scenario.query.get(scenario_id)
    if scenario and scenario.user_id == current_user.id:
        db.session.delete(scenario)
        db.session.commit()
        flash("Scenario deleted successfully!", "success")
    else:
        flash("Scenario not found or you don't have permission to delete it.", "error")
    return redirect(url_for("history.history"))