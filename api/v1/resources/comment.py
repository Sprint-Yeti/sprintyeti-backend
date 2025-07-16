# api/v1/resources/comment.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.comment import Comment
from api.v1.schemas.comment import CommentSchema

blp = Blueprint('comments', 'comments', url_prefix='/api/v1/comments',
                description='Operations on comments')


@blp.route('', methods=['GET'])
@blp.response(200, CommentSchema(many=True))
def list_comments():
    return Comment.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(CommentSchema)
@blp.response(201, CommentSchema)
def create_comment(data):
    comment = Comment(**data)
    db.session.add(comment)
    db.session.commit()
    return comment
