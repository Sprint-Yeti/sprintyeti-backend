# api/v1/resources/plan.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.plan import Plan
from api.v1.schemas.plan import PlanSchema

blp = Blueprint('plans', 'plans', url_prefix='/api/v1/plans',
                description='Operations on subscription plans')


@blp.route('', methods=['GET'])
@blp.response(200, PlanSchema(many=True))
def list_plans():
    return Plan.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(PlanSchema)
@blp.response(201, PlanSchema)
def create_plan(data):
    plan = Plan(**data)
    db.session.add(plan)
    db.session.commit()
    return plan
