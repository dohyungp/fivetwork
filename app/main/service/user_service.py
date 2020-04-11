from datetime import datetime
import jwt
from app.main import db
from app.main.model.user import User


def save_new_user(data):
    """Save new user service"""
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            hire_date=datetime.strptime(data['hire_date'], '%Y-%m-%d'),
            # registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """Get all user list"""
    return User.query.all()


def get_a_user(id):
    """Get a user by id"""
    return User.query.filter_by(id=id).first()


def save_changes(data):
    """Save new data"""
    db.session.add(data)
    db.session.commit()


def generate_token(user):
    """Generate new token based on JWT"""
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except jwt.PyJWTError:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
