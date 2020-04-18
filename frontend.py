import os
from flask import Blueprint, send_from_directory

view = Blueprint('view',
                 __name__,
                 static_folder='fivetwork-frontend/build',
                 url_prefix='/app')


@view.route('/', defaults={'path': ''})
@view.route('/<path:path>')
def index(path):
    """serve view"""
    if path != '' and os.path.exists(view.static_folder + '/' + path):
        return send_from_directory(view.static_folder, path)

    return send_from_directory(view.static_folder, 'index.html')
