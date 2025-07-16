# api/v1/resources/project.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.project import Project
from api.v1.schemas.project import ProjectSchema

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
