# api/v1/schemas/kanban.py
from marshmallow import Schema, fields


class KanbanColumnSchema(Schema):
    id = fields.Int(dump_only=True)
    board_id = fields.Int(required=True)
    name = fields.Str(required=True)
    position = fields.Int(required=True)
    tasks = fields.List(fields.Int())


class KanbanBoardSchema(Schema):
    id = fields.Int(dump_only=True)
    project_id = fields.Int(required=True)
    name = fields.Str(required=True)
    columns = fields.List(fields.Nested(KanbanColumnSchema))
