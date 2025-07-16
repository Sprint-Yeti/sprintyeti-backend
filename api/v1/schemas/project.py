# api/v1/schemas/project.py
from marshmallow import Schema, fields


class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    owner_id = fields.Int(required=True)
    team_id = fields.Int()
    created_at = fields.DateTime(dump_only=True)
