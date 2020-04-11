from flask_restx import Namespace, fields


class UserDto:
    """User DTO"""
    api = Namespace('user', description='user related operations')
    signup = api.model('signup', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'hire_date': fields.Date(required=True, description='user hire date')
    })

    lookup = api.model('lookup', {
        'id': fields.Integer(description='user identifier', readonly=True),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'hire_date': fields.Date(required=True, description='user hire date')
    })


class AuthDto:
    """Auth DTO"""
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
