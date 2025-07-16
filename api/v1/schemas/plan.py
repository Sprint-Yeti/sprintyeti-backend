# api/v1/schemas/plan.py
from marshmallow import Schema, fields


class PlanSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    monthly_price = fields.Float(required=True)
    included_tokens = fields.Int(required=True)
    overage_price = fields.Float(required=True)
    overage_token_unit = fields.Int(required=True)
