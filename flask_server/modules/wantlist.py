from .db import db

class Wantlist(db.Model):
    __tablename__ = 'wantlist'

    id      = db.Column(db.Integer, primary_key=True)
    wantlist= db.Column(db.String)
    user    = db.relationship("User", backref=db.backref("wantlist", uselist=False))

    def __init__(self, wantlist):
        self.wantlist = wantlist

    def __repr__(self):
        return "<Wantlist {}>".format(self.id)

    def insert(new_record):
        self.wantlist += ",new_record"
        db.session.commit()