# api/v1/resources/table_view.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.table_view import TableView
from api.v1.schemas.table_view import TableViewSchema

blp = Blueprint('table_views', 'table_views', url_prefix='/api/v1/table_views',
                description='Operations on table views')


@blp.route('', methods=['GET'])
@blp.response(200, TableViewSchema(many=True))
def list_views():
    return TableView.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(TableViewSchema)
@blp.response(201, TableViewSchema)
def create_view(data):
    view = TableView(**data)
    db.session.add(view)
    db.session.commit()
    return view
