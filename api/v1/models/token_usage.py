# models/token_usage.py
from datetime import datetime
from api.v1.extensions import db


class TokenUsage(db.Model):
    __tablename__ = 'token_usage'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    feature = db.Column(db.String(50), nullable=False)
    tokens_used = db.Column(db.Integer, nullable=False)
