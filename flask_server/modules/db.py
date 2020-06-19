# come back to this later, https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()

csrf = CSRFProtect()