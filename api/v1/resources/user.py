# api/v1/resources/user.py
from flask_smorest import Blueprint, abort
from flask import request
from api.v1.extensions import db
from api.v1.models.user import User
from api.v1.schemas.user import UserSchema, UserUpdateSchema

blp = Blueprint('users', 'users', url_prefix='/api/v1/users',
                description='Operations on users')


@blp.route('', methods=['GET'])
@blp.response(200, UserSchema(many=True))
def list_users():
    '''List all users'''
    return User.query.all()


@blp.route('', methods=['POST'])
@blp.arguments(UserSchema)
@blp.response(201, UserSchema)
def create_user(user_data):
    '''Create a new user'''
    user = User(**user_data)
    db.session.add(user)
    db.session.commit()
    return user


@blp.route('/<int:user_id>')
@blp.response(200, UserSchema)
def get_user(user_id):
    '''Get user by ID'''
    user = User.query.get_or_404(user_id)
    return user


@blp.route('/<int:user_id>', methods=['PUT', 'PATCH'])
@blp.arguments(UserUpdateSchema)
@blp.response(200, UserSchema)
def update_user(update_data, user_id):
    '''Update user by ID'''
    user = User.query.get_or_404(user_id)
    for key, value in update_data.items():
        setattr(user, key, value)
    db.session.commit()
    return user


@blp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    '''Delete user by ID'''
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted'}
