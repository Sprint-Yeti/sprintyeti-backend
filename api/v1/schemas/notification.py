# api/v1/schemas/notification.py
from marshmallow import Schema, fields


class NotificationSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    message = fields.Str(required=True)
    is_read = fields.Bool()
    created_at = fields.DateTime(dump_only=True)
