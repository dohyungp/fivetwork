from datetime import datetime
import jwt
from fivetwork.main import db
from fivetwork.main.model.user import User
from fivetwork.main.model.department import Department


def create_admin(data):
    """Create Super User"""
    user = User.query.filter_by(email=data['email']).first()
    assert not user, f'Admin {data["email"]} already exists!'
    new_user = User(
        email=data['email'],
        username=data['username'],
        password=data['password'],
        hire_date=datetime(1900, 1, 1).date(),
        admin=True
    )
    save_changes(new_user)
    return f'Admin {data["email"]} is successfully created!'


def save_new_user(data):
    """Save new user service"""
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            hire_date=datetime.strptime(data['hire_date'], '%Y-%m-%d'),
        )
        save_changes(new_user)
        return generate_token(new_user)

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


def assign_manager(id, manager_id):
    """Assign manager to user"""
    User.query.filter_by(id=id).update({'manager_id': manager_id})
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'The manager is sucessfully assigned'
    }
    return response_object, 200


def unassign_manager(id):
    """Unassign manager to user"""
    User.query.filter_by(id=id).update({'manager_id': None})
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully manager is unassigned'
    }
    return response_object, 200


def update_a_user(id, data):
    """Update a user information"""
    if 'hire_date' in data:
        data['hire_date'] = datetime.strptime(data['hire_date'], '%Y-%m-%d')

    if 'department_id' in data:
        dept = Department.query.filter_by(id=data['department_id']).first()
        if not dept:
            response_object = {
                'status': 'fail',
                'message': 'Request department is not found.'
            }
            return response_object, 404

    # Prevent not allow data injection
    not_allowed_update = set(data.keys()) - \
        set(['hire_date', 'email', 'admin', 'username', 'department_id'])
    if not_allowed_update:
        response_object = {
            'status': 'fail',
            'message': 'The update is not allowed. please check allowed update fields.'
        }
        return response_object, 403

    User.query.filter_by(id=id).update(data)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated'
    }
    return response_object, 200


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
