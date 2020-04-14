from functools import wraps
from flask import request

from fivetwork.main.service.auth_helper import Auth


def token_required(f):
    """Base Authenticate Wrapper"""
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    """Admin Authenticate Wrapper"""
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated


def self_token_required(f):
    """Base Authenticate Wrapper"""
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        if str(token['user_id']) not in args and\
                str(token['user_id']) != kwargs.get('id') and\
                not token['admin']:
            response_object = {
                'status': 'fail',
                'message': 'request is not allowed'
            }
            return response_object, 403

        return f(*args, **kwargs)

    return decorated
