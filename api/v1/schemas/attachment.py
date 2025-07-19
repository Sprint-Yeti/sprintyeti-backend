# api/v1/schemas/attachment.py
from marshmallow import Schema, fields


class AttachmentSchema(Schema):
    id = fields.Int(dump_only=True)
    task_id = fields.Int(required=True)
    filename = fields.Str(required=True)
    url = fields.Str(required=True)
    uploaded_at = fields.DateTime(dump_only=True)
