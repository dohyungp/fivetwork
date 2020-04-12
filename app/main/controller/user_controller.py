from flask import request
from flask_restx import Resource

from ..util.decorator import self_token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, update_a_user


api = UserDto.api
_signup = UserDto.signup
_lookup = UserDto.lookup
_profile = UserDto.profile

auth_parser = api.parser()
auth_parser.add_argument('Authorization', location='headers',
                         help='authentication token. should pass "Bearer {{ token }}"', required=True)


@api.route('/')
class UserList(Resource):
    """UserList Route"""
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_lookup, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_signup, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    """User Route"""
    @api.doc('get a user')
    @api.marshal_with(_lookup, skip_none=True)
    def get(self, id):
        """get a user given its identifier"""
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
            return user
        return None

    @api.doc('update user profile')
    # @api.expect(_profile, validate=True)
    @api.doc(body=_profile, parser=auth_parser)
    @self_token_required
    def patch(self, id):
        """patch a user given it identifier"""
        data = request.json
        user = get_a_user(id)
        if not user:
            api.abort(404)
        elif 'admin' in data and not user.admin:
            api.abort(401)

        return update_a_user(id, data)
