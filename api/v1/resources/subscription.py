# api/v1/resources/subscription.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.subscriptions import Subscription
from api.v1.schemas.subscription import SubscriptionSchema

blp = Blueprint('subscriptions', 'subscriptions',
                url_prefix='/api/v1/subscriptions', description='Operations on subscriptions')


@blp.route('/<int:user_id>', methods=['GET'])
@blp.response(200, SubscriptionSchema(many=True))
def get_user_subscriptions(user_id):
    return Subscription.query.filter_by(user_id=user_id).all()


@blp.route('', methods=['POST'])
@blp.arguments(SubscriptionSchema)
@blp.response(201, SubscriptionSchema)
def create_subscription(data):
    sub = Subscription(**data)
    db.session.add(sub)
    db.session.commit()
    return sub
