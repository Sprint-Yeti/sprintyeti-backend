# api/v1/schemas/role.py
from marshmallow import Schema, fields


class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
