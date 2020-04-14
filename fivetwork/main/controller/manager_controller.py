from flask import request
from flask_restx import Resource

from ..util.dto import ManagerDto
from ..service.manager_service import get_a_staff, get_all_staffs

api = ManagerDto.api
_staff = ManagerDto.staff


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User or Manager not found.')
class StaffList(Resource):
    """StaffList Route"""
    @api.doc('list of registered staff')
    @api.marshal_list_with(_staff, envelope='staffs')
    def get(self, id):
        """List all registered staffs from current manager_id"""
        return get_all_staffs(id)


@api.route('/<id>/staff/<staff_id>')
@api.param('manger_id', 'The Manager identifier')
@api.param('user_id', 'The staff identifier')
@api.response(404, 'Manager or Staff not found.')
class Staff(Resource):
    """Staff Route"""
    @api.doc('get a staff')
    @api.marshal_with(_staff, skip_none=True)
    def get(self, id, staff_id):
        """get a user given its identifier"""
        staff = get_a_staff(id, staff_id)
        if not staff:
            api.abort(404)
        else:
            return staff
        return None
