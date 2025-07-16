# api/v1/schemas/task.py
from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    importance = fields.Str(required=True)
    status = fields.Str()
    deadline = fields.DateTime()
    project_id = fields.Int()
    assigned_user_id = fields.Int()
    assigned_team_id = fields.Int()
    created_at = fields.DateTime(dump_only=True)
