import os
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from app.models import HTTPError

def create_app(app_name, extra_conf=None, **kwargs):
    app = Flask(app_name, **kwargs)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', 'postgresql://anitta:123456@localhost:5433/flaskapp')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if extra_conf:
        for item in extra_conf:
            app.config[item] = extra_conf[item]

    return app

def get_db_instance(app, **kwargs):
    return SQLAlchemy(app, **kwargs)
