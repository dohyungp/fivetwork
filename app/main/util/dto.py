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
        'hire_date': fields.Date(required=True, description='user hire date'),
        'admin': fields.Boolean(required=True, description='is user admin')
    })

    profile = api.model('profile', {
        'email': fields.String(description='user email address'),
        'username': fields.String(description='user username'),
        'hire_date': fields.Date(description='user hire date'),
        'admin': fields.Boolean(description='is user admin'),
    })

    manager = api.model('user_manager_relationship', {
        'manager_id': fields.Integer(description='manger id', required=True)
    })


class AuthDto:
    """Auth DTO"""
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class ManagerDto:
    """Manager DTO"""
    api = Namespace('manager', description='manager related operations')
    staff = api.model('staff', {
        'id': fields.Integer(description='staff identifier', readonly=True),
        'manager_id': fields.Integer(description='manager identifier', readonly=True),
        'email': fields.String(required=True, description='staff email address'),
        'username': fields.String(required=True, description='staff username'),
        'hire_date': fields.Date(required=True, description='staff hire date')
    })
