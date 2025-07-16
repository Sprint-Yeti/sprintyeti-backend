# api/v1/schemas/command.py
from marshmallow import Schema, fields


class CommandSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    team_id = fields.Int()
    text = fields.Str(required=True)
    deadline = fields.DateTime()
    tech_stack = fields.Str()
    phase_focus = fields.Str()
    created_at = fields.DateTime(dump_only=True)
