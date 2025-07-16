# models/task.py
from datetime import datetime
from api.v1.extensions import db
from .kanban import kanban_tasks
from .label import task_labels


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    importance = db.Column(db.Enum('critical', 'important_not_urgent', 'urgent_not_important',
                           'non_urgent_non_important', name='importance_levels'), nullable=False)
    status = db.Column(db.Enum('pending', 'not_started', 'in_progress', 'done',
                       'rework', name='status_levels'), default='pending', nullable=False)
    deadline = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    assigned_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    assigned_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    creator = db.relationship('User', foreign_keys=[assigned_user_id])
    team_assignee = db.relationship('Team', foreign_keys=[assigned_team_id])
    kanban_columns = db.relationship(
        'KanbanColumn', secondary=kanban_tasks, back_populates='tasks')
    labels = db.relationship(
        'Label', secondary=task_labels, back_populates='tasks')
    comments = db.relationship('Comment', backref='task', lazy=True)
    attachments = db.relationship('Attachment', backref='task', lazy=True)
