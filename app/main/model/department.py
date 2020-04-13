from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .. import db
# from .user import User


class Department(db.Model):
    """ Department Model for storing department related details """
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(14), nullable=False)
    user = relationship("User")
