import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    TESTING = os.getenv('TESTING', 'False') == 'True'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///tasks.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')