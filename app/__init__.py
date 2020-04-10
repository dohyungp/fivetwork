from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='FIVETWORK REST API',
          version='1.0',
          description='a fivetwork rest web service',
          doc='/documentation'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
