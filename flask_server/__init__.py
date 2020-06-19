from flask import Flask
from . import controllers
from . import config
from .modules.auth import login_manager
from .modules.db import db, csrf
import os

"""GLOBAL VARS"""
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), '../app.sqlite')

def create_app(test_config=config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)

    controllers.common.register(app)

    app.config['SECRET_KEY'] = test_config.SECRET_KEY
    
    return app

def register_blueprints(app):
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(controllers.auth.blueprint)
    return None

def register_extensions(app):
    db.init_app(app) 
    with app.app_context():
        db.create_all()
    
    login_manager.init_app(app)
    csrf.init_app(app)

    return None