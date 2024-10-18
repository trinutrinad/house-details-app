import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Database URL from .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False
