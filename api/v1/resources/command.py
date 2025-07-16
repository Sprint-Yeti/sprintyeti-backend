# api/v1/resources/command.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.command import Command
from api.v1.schemas.command import CommandSchema

blp = Blueprint('commands', 'commands', url_prefix='/api/v1/commands',
                description='Operations on commands')


@blp.route('', methods=['POST'])
@blp.arguments(CommandSchema)
@blp.response(201, CommandSchema)
def execute_command(data):
    cmd = Command(**data)
    db.session.add(cmd)
    db.session.commit()
    # TODO: parse and apply command to tasks
    return cmd
