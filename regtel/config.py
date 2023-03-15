import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or "myscretkey123"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///project.sqlite'
    LOGIN_URL = '/login'
