# api/v1/__init__.py
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from .extensions import db, jwt, cors, limiter
from .resources.user import blp as user_blp
from .resources.team import blp as team_blp
from .resources.role import blp as role_blp
from .resources.project import blp as project_blp
from .resources.task import blp as task_blp
from .resources.command import blp as command_blp
from .resources.subscription import blp as subscription_blp
from .resources.plan import blp as plan_blp
from .resources.token_usage import blp as token_usage_blp
from .resources.label import blp as label_blp
from .resources.comment import blp as comment_blp
from .resources.attachment import blp as attachment_blp
from .resources.notification import blp as notification_blp
from .resources.kanban import blp as kanban_blp
from .resources.table_view import blp as table_view_blp


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    limiter.init_app(app)
    Migrate(app, db)

    # Register blueprints
    api = Api(app)
    for bp in [
        user_blp, team_blp, role_blp, project_blp, task_blp,
        command_blp, subscription_blp, plan_blp, token_usage_blp,
        label_blp, comment_blp, attachment_blp, notification_blp,
        kanban_blp, table_view_blp
    ]:
        api.register_blueprint(bp)

    return app
