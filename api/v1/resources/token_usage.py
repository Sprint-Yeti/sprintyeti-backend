# api/v1/resources/token_usage.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.token_usage import TokenUsage
from api.v1.schemas.token_usage import TokenUsageSchema

blp = Blueprint('token_usage', 'token_usage', url_prefix='/api/v1/usage',
                description='Operations on token usage')


@blp.route('', methods=['GET'])
@blp.response(200, TokenUsageSchema(many=True))
def list_usage():
    return TokenUsage.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(TokenUsageSchema)
@blp.response(201, TokenUsageSchema)
def log_usage(data):
    usage = TokenUsage(**data)
    db.session.add(usage)
    db.session.commit()
    return usage
