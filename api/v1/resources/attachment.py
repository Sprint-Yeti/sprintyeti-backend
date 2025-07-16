# api/v1/resources/attachment.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.attachment import Attachment
from api.v1.schemas.attachment import AttachmentSchema

blp = Blueprint('attachments', 'attachments', url_prefix='/api/v1/attachments',
                description='Operations on attachments')


@blp.route('', methods=['GET'])
@blp.response(200, AttachmentSchema(many=True))
def list_attachments():
    return Attachment.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(AttachmentSchema)
@blp.response(201, AttachmentSchema)
def upload_attachment(data):
    attach = Attachment(**data)
    db.session.add(attach)
    db.session.commit()
    return attach
