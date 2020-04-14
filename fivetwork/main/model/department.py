from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .. import db
# from .user import User


class Department(db.Model):
    """ Department Model for storing department related details """
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(14), nullable=False)
    manager_id = db.Column(
        db.Integer, db.ForeignKey('user.id', use_alter=True))
    members = relationship(
        'User', back_populates='department', foreign_keys='User.department_id')
    manager = relationship('User', foreign_keys=[manager_id], post_update=True)
