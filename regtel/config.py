import os
import secrets

class Config:
    SECRET_KEY=secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///project.sqlite'
    LOGIN_URL = '/login'
