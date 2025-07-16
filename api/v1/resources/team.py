# api/v1/resources/team.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.team import Team
from api.v1.schemas.team import TeamSchema

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
