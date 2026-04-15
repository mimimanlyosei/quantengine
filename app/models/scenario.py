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
    risk_appetite = db.Column(db.String(20), nullable=False)
    base_result = db.Column(db.Float, nullable=False)
    optimistic_result = db.Column(db.Float, nullable=False)
    pessimistic_result = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
