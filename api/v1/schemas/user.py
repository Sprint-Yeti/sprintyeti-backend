# api/v1/schemas/user.py
from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True,
                          validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)


class UserUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    email = fields.Email()
    password = fields.Str(load_only=True, validate=validate.Length(min=6))
