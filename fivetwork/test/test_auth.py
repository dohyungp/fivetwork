import unittest
import json
from fivetwork.test.base import BaseTestCase


def register_user(self):
    """Test function for create new user via client"""
    return self.client.post(
        '/api/user/',
        data=json.dumps(dict(
            email='example@gmail.com',
            username='username',
            password='123456',
            hire_date='2020-04-11'
        )),
        content_type='application/json'
    )


def login_user(self, email='example@gmail.com'):
    """Test function for login user via client"""
    return self.client.post(
        '/api/auth/login',
        data=json.dumps(dict(
            email=email,
            password='123456'
        )),
        content_type='application/json'
    )


def update_user_profile(self, headers):
    return self.client.patch(
        '/api/user/1',
        data=json.dumps(dict(
            email='example2@gmail.com'
        )),
        content_type='application/json',
        headers=headers
    )


def update_user_to_admin(self, headers):
    return self.client.patch(
        '/api/user/1',
        data=json.dumps(dict(
            admin=True
        )),
        content_type='application/json',
        headers=headers
    )


class TestAuthBlueprint(BaseTestCase):
    """TestAuth Blueprint Class"""

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registered user login
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

    def test_valid_user_data_update_after_login(self):

        with self.client:
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            headers = dict(
                Authorization='Bearer ' + json.loads(
                    login_response.data.decode()
                )['Authorization']
            )

            update_response = update_user_profile(self, headers)
            data = json.loads(update_response.data.decode())
            self.assertEqual(update_response.status_code, 200)
            self.assertEqual(data['status'], 'success')

            update_response = update_user_to_admin(self, headers)
            data = json.loads(update_response.data.decode())
            self.assertEqual(update_response.status_code, 403)

            # valid token logout
            response = self.client.post(
                '/api/auth/logout',
                headers=headers
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)

            login_response = login_user(self, 'example2@gmail.com')
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registered user login
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            # valid token logout
            response = self.client.post(
                '/api/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(
                        login_response.data.decode()
                    )['Authorization']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
