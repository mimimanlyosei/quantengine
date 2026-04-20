from datetime import datetime
from app import db

class Scenario(db.Model):
    '''This class defines the Scenario model for storing investment scenarios created by users.
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    initial_investment = db.Column(db.Float, nullable=False)
    expected_return = db.Column(db.Float, nullable=False)
    years_of_investment = db.Column(db.Integer, nullable=False)
    risk_appetite = db.Column(db.String(20), nullable=True)
    base_result = db.Column(db.Float, nullable=True)
    optimistic_result = db.Column(db.Float, nullable=True)
    pessimistic_result = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def validate(self):
        errors = []
        
        # Validate initial investment
        try:
            initial_investment = float(self.initial_investment)
        except ValueError:
            errors.append("Please enter a valid initial investment amount.")
        else:
            if initial_investment <= 0:
                errors.append("Initial investment cannot be less than £1.")
        

        # Validate expected return
        try:
            expected_return = float(self.expected_return)
        except ValueError:
            errors.append("Please enter a valid expected return.")
        else:
            if expected_return < 0 or expected_return > 50:
                errors.append("Expected return must be between 0% and 50%.")

        # Validate years of investment
        try:
            years_of_investment = int(self.years_of_investment)
        except ValueError:
            errors.append("Please enter a valid number of years.")
        else:
            if years_of_investment <= 0 or years_of_investment > 70:
                errors.append("Years of investment must be between 1 and 70.")

        # Validate risk appetite
        risk_appetite = str(self.risk_appetite).lower()
        if risk_appetite not in ["low", "medium", "high"]:
            errors.append("Please select a valid risk appetite.")

        return errors