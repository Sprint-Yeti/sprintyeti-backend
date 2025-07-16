# models/label.py
from api.v1.extensions import db

task_labels = db.Table(
    'task_labels',
    db.Column('task_id', db.Integer, db.ForeignKey(
        'tasks.id'), primary_key=True),
    db.Column('label_id', db.Integer, db.ForeignKey(
        'labels.id'), primary_key=True)
)


class Label(db.Model):
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20))

    tasks = db.relationship(
        'Task', secondary=task_labels, back_populates='tasks')
