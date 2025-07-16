# api/v1/resources/label.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.label import Label
from api.v1.schemas.label import LabelSchema

blp = Blueprint('labels', 'labels', url_prefix='/api/v1/labels',
                description='Operations on labels')


@blp.route('', methods=['GET'])
@blp.response(200, LabelSchema(many=True))
def list_labels():
    return Label.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(LabelSchema)
@blp.response(201, LabelSchema)
def create_label(data):
    label = Label(**data)
    db.session.add(label)
    db.session.commit()
    return label
