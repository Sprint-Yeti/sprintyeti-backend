# models/table_view.py
from api.v1.extensions import db


class TableView(db.Model):
    __tablename__ = 'table_views'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    filters = db.Column(db.JSON)
    columns = db.Column(db.JSON)
