from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import NumberRange

class BudgetForm(FlaskForm):
    budget = FloatField('Budget', validators=[NumberRange(min=0, max=50, message='Please enter a dollar value between $0.01 and $50.00')])