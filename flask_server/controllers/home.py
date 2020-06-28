from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_login import current_user
from werkzeug.security import check_password_hash, generate_password_hash
from ..forms.budget import BudgetForm
from ..modules.db   import db
import functools

blueprint = Blueprint('home', __name__, url_prefix='/')

@blueprint.route('/', methods=('GET', 'POST'))
def home():
    if current_user.is_authenticated:
        form = BudgetForm(request.form)
        
        if request.method == 'POST' and form.validate():
            current_user.budget = float(form.budget.raw_data[0])
            db.session.commit()

        return render_template('home/home_authenticated.html', form=form)

    return render_template('home/home_unauthenticated.html')