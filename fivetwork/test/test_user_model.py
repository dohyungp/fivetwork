import unittest
import datetime

from fivetwork.main import db
from fivetwork.main.model.user import User
from fivetwork.test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    """Test User Model"""

    def test_encode_auth_token(self):
        """Test method for testing encoding auth token"""
        user = User(
            email='test@test.com',
            password='test',
            username='Dohyung Park',
            hire_date=datetime.date(2019, 1, 1),
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        """Test method for testing decoding auth token"""
        user = User(
            email='test@test.com',
            password='test',
            username='Dohyung Park',
            hire_date=datetime.date(2019, 1, 1),
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(
            auth_token.decode("utf-8")) == 1)


if __name__ == '__main__':
    unittest.main()
