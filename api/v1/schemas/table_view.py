# api/v1/schemas/table_view.py
from marshmallow import Schema, fields


class TableViewSchema(Schema):
    id = fields.Int(dump_only=True)
    project_id = fields.Int(required=True)
    filters = fields.Dict()
    columns = fields.List(fields.Str())
