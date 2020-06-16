from flask import Flask
from . import controllers
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'))

    register_blueprints(app)

    return app

def register_blueprints(app):
    app.register_blueprint(controllers.home.blueprint)
    return None