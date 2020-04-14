from flask import request
from flask_restx import Resource

from ..util.dto import DepartmentDto
from ..service.department_service import (create_new_department,
                                          get_a_department,
                                          get_all_departments,
                                          update_a_department,
                                          delete_a_department)


api = DepartmentDto.api
_lookup = DepartmentDto.lookup_dept
_establish = DepartmentDto.establish_dept
_detail = DepartmentDto.department_information

auth_parser = api.parser()
auth_parser.add_argument('Authorization', location='headers',
                         help='authentication token. should pass "Bearer {{ token }}"',
                         required=True)


@api.route('/')
class DepartmentList(Resource):
    """Department List Route"""
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_lookup, envelope='departments')
    def get(self):
        """List all registered department"""
        return get_all_departments()

    @api.response(201, 'Department successfully created.')
    @api.doc('create a new user')
    @api.expect(_establish, validate=True)
    def post(self):
        """Creates a new Department """
        data = request.json
        return create_new_department(data=data)


@api.route('/<id>')
@api.param('id', 'The Department identifier')
@api.response(404, 'Department not found.')
class Department(Resource):
    """Department Route"""
    @api.doc('get a department')
    @api.marshal_with(_lookup, skip_none=True)
    def get(self, id):
        """get a department given its identifier"""
        department = get_a_department(id)
        if not department:
            api.abort(404)
            return None

        return department

    @api.doc('update department info')
    @api.expect(_detail, validate=True)
    def patch(self, id):
        """patch dept data"""
        data = request.json
        department = get_a_department(id)
        if not department:
            api.abort(404)
            return None
        return update_a_department(id, data)

    @api.doc('delete a department')
    def delete(self, id):
        """get a department given its identifier"""
        department = get_a_department(id)
        if not department:
            api.abort(404)
            return None

        return delete_a_department(id)
