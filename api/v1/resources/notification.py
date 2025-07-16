# api/v1/resources/notification.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.notification import Notification
from api.v1.schemas.notification import NotificationSchema

blp = Blueprint('notifications', 'notifications',
                url_prefix='/api/v1/notifications', description='Operations on notifications')


@blp.route('', methods=['GET'])
@blp.response(200, NotificationSchema(many=True))
def list_notifications():
    return Notification.query.all()


@blp.route('/<int:user_id>/mark_read', methods=['POST'])
@blp.response(204)
def mark_read(user_id):
    Notification.query.filter_by(user_id=user_id).update({'is_read': True})
    db.session.commit()
