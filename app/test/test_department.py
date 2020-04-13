import unittest
import json

from app.main import db
from app.main.model.department import Department
from app.test.base import BaseTestCase


def add_department(self):
    """Test function for create new department via client"""
    return self.client.post(
        '/api/department/',
        data=json.dumps(dict(
            department_name='test'
        )),
        content_type='application/json'
    )


def delete_department(self):
    """Test function for delete department via client"""
    return self.client.delete('/api/department/1')


def get_a_department(self):
    """Test function for delete department via client"""
    return self.client.get('/api/department/1')


class TestDeptModel(BaseTestCase):
    """Test Department Model"""

    def test_department_create_and_delete(self):
        """ Test for department create and delete"""
        with self.client:
            # department creation
            dept_response = add_department(self)
            self.assertEqual(dept_response.status_code, 201)

            # department deletion
            dept_response = delete_department(self)
            self.assertEqual(dept_response.status_code, 200)

    def test_department_create_and_inquiry(self):
        """ Test for department create and delete"""
        with self.client:
            # department creation
            dept_response = add_department(self)
            self.assertEqual(dept_response.status_code, 201)

            # department deletion
            dept_response = get_a_department(self)
            self.assertEqual(dept_response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
