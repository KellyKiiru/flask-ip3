from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), nullable = False, unique = True)
    pitches = db.relationship("Pitch", backref = 'user', lazy = 'dynamic')
    
    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    pitch = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'User {self.pitch} {self.category}'