# models/user.py
from datetime import datetime
from api.v1.extensions import db
from .team import team_members
from .role import user_roles

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    subscriptions = db.relationship('Subscription', backref='user', lazy=True)
    token_usages = db.relationship('TokenUsage', backref='user', lazy=True)
    teams = db.relationship('Team', secondary=team_members, back_populates='members')
    roles = db.relationship('Role', secondary=user_roles, back_populates='users')
    projects = db.relationship('Project', backref='owner', lazy=True)
    tasks = db.relationship('Task', backref='creator', lazy=True)
    commands = db.relationship('Command', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)