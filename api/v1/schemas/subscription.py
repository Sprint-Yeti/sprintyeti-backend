# api/v1/schemas/subscription.py
from marshmallow import Schema, fields, validate


class SubscriptionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    plan_id = fields.Int(required=True)
    start_date = fields.DateTime(dump_only=True)
    end_date = fields.DateTime()
    status = fields.Str(required=True)
    remaining_tokens = fields.Int(required=True)
