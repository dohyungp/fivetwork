from app.main.model.user import User


def get_all_staffs(manager_id):
    """Get all staff list"""
    return User.query.filter_by(manager_id=manager_id).all()


def get_a_staff(manager_id, staff_id):
    """Get a staff based on there id."""
    return User.query.filter_by(id=staff_id, manager_id=manager_id).all()
