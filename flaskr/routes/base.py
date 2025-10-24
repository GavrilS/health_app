'''
This file holds the base routes functionality:
- loading home page
'''

from flask import (
    Blueprint, render_template, abort
)
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    '''
    Load the home page:
    - no data needs to be passed
    '''
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)