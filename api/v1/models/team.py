# models/team.py
from datetime import datetime
from api.v1.extensions import db

team_members = db.Table(
    'team_members',
    db.Column('team_id', db.Integer, db.ForeignKey(
        'teams.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
)


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    members = db.relationship(
        'User', secondary=team_members, back_populates='teams')
    projects = db.relationship('Project', backref='team', lazy=True)
    commands = db.relationship('Command', backref='team', lazy=True)
