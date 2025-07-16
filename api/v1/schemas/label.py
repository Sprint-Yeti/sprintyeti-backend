# api/v1/schemas/label.py
from marshmallow import Schema, fields


class LabelSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    color = fields.Str()
