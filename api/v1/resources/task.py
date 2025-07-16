# api/v1/resources/task.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.task import Task
from api.v1.schemas.task import TaskSchema

blp = Blueprint('tasks', 'tasks', url_prefix='/api/v1/tasks',
                description='Operations on tasks')


@blp.route('', methods=['GET'])
@blp.response(200, TaskSchema(many=True))
def list_tasks():
    return Task.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(TaskSchema)
@blp.response(201, TaskSchema)
def create_task(data):
    task = Task(**data)
    db.session.add(task)
    db.session.commit()
    return task
