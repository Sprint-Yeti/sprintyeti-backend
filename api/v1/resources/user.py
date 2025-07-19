# api/v1/resources/user.py
from flask_smorest import Blueprint, abort
from werkzeug.security import generate_password_hash
from api.v1.extensions import db
from api.v1.models.user import User
from api.v1.models.task import Task
from api.v1.models.project import Project
from api.v1.schemas.user import UserSchema, UserUpdateSchema
from api.v1.schemas.task import TaskSchema
from api.v1.schemas.project import ProjectSchema

blp = Blueprint('users', 'users', url_prefix='/api/v1/users',
                description='Operations on users')


@blp.route('', methods=['GET'])
@blp.response(200, UserSchema(many=True))
def list_users():
    return User.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(UserSchema)
@blp.response(201, UserSchema)
def create_user(user_data):
    raw_password = user_data.pop('password', None)
    if not raw_password:
        abort(400, message='Password is required')
    user = User(
        name=user_data['name'],
        email=user_data['email'],
        password_hash=generate_password_hash(raw_password)
    )
    db.session.add(user)
    db.session.commit()
    return user


@blp.route('/<int:user_id>', methods=['GET'])
@blp.response(200, UserSchema)
def get_user(user_id):
    return User.query.get_or_404(user_id)


@blp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@blp.arguments(UserUpdateSchema)
@blp.response(200, UserSchema)
def update_user(update_data, user_id):
    user = User.query.get_or_404(user_id)
    if 'password' in update_data:
        user.password_hash = generate_password_hash(
            update_data.pop('password'))
    for key, value in update_data.items():
        setattr(user, key, value)
    db.session.commit()
    return user


@blp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted'}

# Nested: Projects for a user


@blp.route('/<int:user_id>/projects', methods=['GET'])
@blp.response(200, ProjectSchema(many=True))
def list_user_projects(user_id):
    user = User.query.get_or_404(user_id)
    return user.projects

# Nested: Tasks for a user (assigned)


@blp.route('/<int:user_id>/tasks', methods=['GET'])
@blp.response(200, TaskSchema(many=True))
def list_user_tasks(user_id):
    return Task.query.filter_by(assigned_user_id=user_id).all()
