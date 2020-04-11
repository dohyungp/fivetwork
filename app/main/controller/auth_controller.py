from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth
auth_parser = api.parser()
auth_parser.add_argument('Authorization', location='headers',
                         help='Bearer {{ Token }}', required=True)


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        """Login method"""
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    @api.expect(auth_parser)
    @api.response(200, 'User successfully logged out.')
    @api.response(401, 'User logout was failed.')
    def post(self):
        """Logout method"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
