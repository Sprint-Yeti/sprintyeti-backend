# models/command.py
from datetime import datetime
from api.v1.extensions import db


class Command(db.Model):
    __tablename__ = 'commands'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    text = db.Column(db.String(1000), nullable=False)
    deadline = db.Column(db.DateTime)
    tech_stack = db.Column(db.String(200))
    phase_focus = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
