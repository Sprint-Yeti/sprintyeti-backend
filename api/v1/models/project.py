# models/project.py
from datetime import datetime
from api.v1.extensions import db


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tasks = db.relationship('Task', backref='project', lazy=True)
    kanban_boards = db.relationship(
        'KanbanBoard', backref='project', lazy=True)
    table_views = db.relationship('TableView', backref='project', lazy=True)
