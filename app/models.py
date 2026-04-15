from datetime import datetime
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    '''This class defines the User model for authentication and user management.
    It inherits from UserMixin to integrate with
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
    

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