import requests, urllib
from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from ..forms.auth import SigninForm, SignupForm
from ..modules.auth import login_manager
from ..modules.db   import db
from ..modules.user import User
from ..modules.site import Sidelink, Sidebar

blueprint = Blueprint('auth', __name__, url_prefix='/sign')

@blueprint.route('/in', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    form = SigninForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.data['username']).first()

        if not user or not user.check_password(form.data['password']):
            flash('Invalid Username or Password.')
            return redirect(url_for('auth.in'))
        
        login_user(user, remember=True)
        
        return redirect(url_for('home.home'))

    sidelinks   = [Sidelink('Sign In', "javascript:document.getElementById('signin').submit()", 'submit', True)]
    sidebar     = [Sidebar('Home', 'home.home'), Sidebar('Github', 'https://github.com/poiley/weekly-records', True)]
    return render_template('auth/in.html', sidelinks=sidelinks, sidebar=sidebar, form=form)


@blueprint.route('/up', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    
    if request.method == 'POST' and form.validate():
        user = User(form.data['username'], form.data['displayname'], generate_password_hash(form.data['password']))

        db.session.add(user)
        db.session.commit()

        login_user(user, remember=True)

        return redirect(url_for('home.home'))
    
    sidelinks   = [Sidelink('Sign Up', "javascript:document.getElementById('signup').submit()", 'submit', True)]
    sidebar     = [Sidebar('Home', 'home.home'), Sidebar('Sign In', 'auth.signin'), Sidebar('Github', 'https://github.com/poiley/weekly-records', True)]
    return render_template('auth/up.html', sidelinks=sidelinks, sidebar=sidebar, form=form)

@blueprint.route("/out")
@login_required
def signout():
    logout_user()
    return redirect(url_for('home.home'))

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)