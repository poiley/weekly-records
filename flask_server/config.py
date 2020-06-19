import os

SECRET_KEY = 'hello world'
ENV = os.getenv('FLASK_ENV', default='development')
DEBUG = ENV == 'development'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), '../app.sqlite')