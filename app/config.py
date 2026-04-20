import os

class Config:
    """Configuration settings for quantEngine"""
    SECRET_KEY = os.getenv('SECRET_KEY') or 'this-is-a-secret'
    _db_url = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    if _db_url and _db_url.startswith('postgres://'):
        _db_url = _db_url.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

