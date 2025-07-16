# api/v1/schemas/token_usage.py
from marshmallow import Schema, fields


class TokenUsageSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    date = fields.Date(dump_only=True)
    feature = fields.Str(required=True)
    tokens_used = fields.Int(required=True)
