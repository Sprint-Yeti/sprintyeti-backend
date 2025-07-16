# models/kanban.py
from api.v1.extensions import db

kanban_tasks = db.Table(
    'kanban_tasks',
    db.Column('column_id', db.Integer, db.ForeignKey(
        'kanban_columns.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey(
        'tasks.id'), primary_key=True)
)


class KanbanBoard(db.Model):
    __tablename__ = 'kanban_boards'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    columns = db.relationship('KanbanColumn', backref='board', lazy=True)


class KanbanColumn(db.Model):
    __tablename__ = 'kanban_columns'
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey(
        'kanban_boards.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    tasks = db.relationship('Task', secondary=kanban_tasks,
                            back_populates='kanban_columns')
