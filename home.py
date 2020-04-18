import os
from flask import Blueprint, redirect, url_for


home = Blueprint('home', __name__, url_prefix='/')


@home.route('/')
def index():
    """root resource

    :return: redirect
    :rtype: Response
    """
    return redirect(url_for('view.index'))
