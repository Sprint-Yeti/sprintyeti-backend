# api/v1/resources/project.py
from flask_smorest import Blueprint, abort
from api.v1.extensions import db
from api.v1.models.project import Project
from api.v1.models.task import Task
from api.v1.schemas.project import ProjectSchema
from api.v1.schemas.task import TaskSchema
from services.ai_service import AIService

blp = Blueprint('projects', 'projects', url_prefix='/api/v1/projects',
                description='Operations on projects')


@blp.route('', methods=['GET'])
@blp.response(200, ProjectSchema(many=True))
def list_projects():
    return Project.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(ProjectSchema)
@blp.response(201, ProjectSchema)
def create_project(data):
    proj = Project(**data)
    db.session.add(proj)
    db.session.commit()
    return proj

# Nested: Tasks for a project


@blp.route('/<int:project_id>/tasks', methods=['GET'])
@blp.response(200, TaskSchema(many=True))
def list_project_tasks(project_id):
    return Task.query.filter_by(project_id=project_id).all()

# AI-powered breakdown endpoint


@blp.route('/<int:project_id>/breakdown', methods=['POST'])
@blp.response(200, TaskSchema(many=True))
def breakdown_project(project_id):
    proj = Project.query.get_or_404(project_id)
    if not proj.description:
        abort(400, message='Project description required for breakdown')
    ai = AIService()
    tasks_data = ai.task_breakdown(proj.description)
    tasks = []
    for td in tasks_data:
        t = Task(
            title=td.get('title'),
            description=td.get('description'),
            deadline=td.get('deadline'),
            importance=td.get('importance'),
            project_id=project_id
        )
        db.session.add(t)
        tasks.append(t)
    db.session.commit()
    return tasks
