# api/v1/resources/role.py
from flask_smorest import Blueprint
from api.v1.extensions import db
from api.v1.models.role import Role
from api.v1.schemas.role import RoleSchema

blp = Blueprint('roles', 'roles', url_prefix='/api/v1/roles',
                description='Operations on roles')


@blp.route('', methods=['GET'])
@blp.response(200, RoleSchema(many=True))
def list_roles():
    return Role.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(RoleSchema)
@blp.response(201, RoleSchema)
def create_role(data):
    role = Role(**data)
    db.session.add(role)
    db.session.commit()
    return role
