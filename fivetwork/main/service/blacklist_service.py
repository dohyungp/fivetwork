from fivetwork.main import db
from fivetwork.main.model.blacklist import BlacklistToken
from sqlalchemy.exc import SQLAlchemyError


def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        # insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except SQLAlchemyError as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 200
