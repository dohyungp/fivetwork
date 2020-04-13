from app.main import db
from app.main.model.department import Department


def create_new_department(data):
    """Create new department"""
    new_department = Department(
        department_name=data['department_name']
    )
    save_changes(new_department)
    response_object = {
        'status': 'success',
        'message': 'Successfully created new department.'
    }
    return response_object, 201


def get_all_departments():
    """Get all department list"""
    return Department.query.all()


def get_a_department(id):
    """Get a department by id"""
    return Department.query.filter_by(id=id).first()


def update_a_department(id, data):
    # Prevent not allow data injection
    not_allowed_update = set(data.keys()) - set(['department_name'])
    if not_allowed_update:
        response_object = {
            'status': 'fail',
            'message': 'The update is not allowed. please check allowed update fields.'
        }
        return response_object, 403

    Department.query.filter_by(id=id).update(data)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated'
    }
    return response_object, 200


def delete_a_department(id):
    """Delete a department"""
    Department.query.filter_by(id=id).delete()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully deleted'
    }
    return response_object, 200


def save_changes(data):
    """Save new department"""
    db.session.add(data)
    db.session.commit()
