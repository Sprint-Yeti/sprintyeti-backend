# models/plan.py
from api.v1.extensions import db


class Plan(db.Model):
    __tablename__ = 'plans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    monthly_price = db.Column(db.Float, nullable=False)
    included_tokens = db.Column(db.Integer, nullable=False)
    overage_price = db.Column(db.Float, nullable=False)
    overage_token_unit = db.Column(db.Integer, default=1)

    subscriptions = db.relationship('Subscription', backref='plan', lazy=True)
