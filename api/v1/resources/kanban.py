# api/v1/resources/kanban.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.kanban import KanbanBoard, KanbanColumn
from api.v1.schemas.kanban import KanbanBoardSchema, KanbanColumnSchema

blp = Blueprint('kanban', 'kanban', url_prefix='/api/v1/kanban',
                description='Operations on kanban boards and columns')


@blp.route('/boards', methods=['GET'])
@blp.response(200, KanbanBoardSchema(many=True))
def list_boards():
    return KanbanBoard.query.all()


@blp.route('/boards', methods=['POST'])
@blp.arguments(KanbanBoardSchema)
@blp.response(201, KanbanBoardSchema)
def create_board(data):
    board = KanbanBoard(**data)
    db.session.add(board)
    db.session.commit()
    return board


@blp.route('/columns', methods=['POST'])
@blp.arguments(KanbanColumnSchema)
@blp.response(201, KanbanColumnSchema)
def create_column(data):
    col = KanbanColumn(**data)
    db.session.add(col)
    db.session.commit()
    return col
