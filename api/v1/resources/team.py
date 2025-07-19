# api/v1/resources/team.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.team import Team
from api.v1.models.task import Task
from api.v1.models.project import Project
from api.v1.schemas.team import TeamSchema
from api.v1.schemas.task import TaskSchema
from api.v1.schemas.project import ProjectSchema

blp = Blueprint('teams', 'teams', url_prefix='/api/v1/teams',
                description='Operations on teams')


@blp.route('', methods=['GET'])
@blp.response(200, TeamSchema(many=True))
def list_teams():
    return Team.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(TeamSchema)
@blp.response(201, TeamSchema)
def create_team(team_data):
    team = Team(**team_data)
    db.session.add(team)
    db.session.commit()
    return team

# Nested: Projects for a team


@blp.route('/<int:team_id>/projects', methods=['GET'])
@blp.response(200, ProjectSchema(many=True))
def list_team_projects(team_id):
    team = Team.query.get_or_404(team_id)
    return team.projects

# Nested: Tasks for a team


@blp.route('/<int:team_id>/tasks', methods=['GET'])
@blp.response(200, TaskSchema(many=True))
def list_team_tasks(team_id):
    return Task.query.filter_by(assigned_team_id=team_id).all()
