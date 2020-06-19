from .db import db
from werkzeug.security import check_password_hash
from . import wantlist

class User(db.Model):
    __tablename__ = 'user'

    id           = db.Column(db.Integer, primary_key=True)
    username     = db.Column(db.String(80), unique=True, nullable=False)
    password     = db.Column(db.String(1000), nullable=False)
    display_name = db.Column(db.String(80))
    budget       = db.Column(db.Integer, nullable=True)
    discogs_username = db.Column(db.String(32), unique=True, nullable=True)

    wantlist_id  = db.Column(db.Integer, db.ForeignKey(wantlist.Wantlist.id))
    Wanlist      = db.relationship(wantlist.Wantlist, uselist=False)

    def __init__(self, username, display_name, password, budget=0, discogs_username=None):
        self.username       = username
        self.display_name   = display_name
        self.password       = password
        self.budget         = budget
        self.discogs_username=discogs_username

    def __repr__(self):
        return "<User: {}>".format(self.username)

    def get(id):
        return User.query.get(id)

    def get_id(self):
        return self.id

    def get_records(self):
        return User.query.with_entities(User.records)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return not self.is_authenticated()
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
