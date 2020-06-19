import functools
from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for )
from werkzeug.security import check_password_hash, generate_password_hash

blueprint = Blueprint('home', __name__, url_prefix='/')

@blueprint.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        print('logging in')
        
    return render_template('home.html')