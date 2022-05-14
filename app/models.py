from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), nullable = False, unique = True)
    pitches = db.relationship("Pitch", backref = 'user', lazy = 'dynamic')
    email = db.Column(db.String(255), unique = True, nullable = False)
    pass_secure = db.Column(db.String(128), unique = True, nullable = False)
    bio = db.Column(db.String())
    upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')
    
    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    pitch = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String)
    upvotes = db.relationship('Upvote', backref='pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref='pitch', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.pitch} {self.category}'
    
    
class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
     
    def __repr__(self):
        return f'Comment  {self.title} {self.comment}'