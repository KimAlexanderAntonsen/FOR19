from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired

class BusForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Fuel', choices=[
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric')
    ])
    submit = SubmitField('Submit')

class CarForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Fuel', choices=[
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid')
    ])
    submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Flight type', choices=[
        ('Short-haul', 'Short-haul'),
        ('Long-haul', 'Long-haul')
    ])
    submit = SubmitField('Submit')

class FerryForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Fuel', choices=[('Diesel', 'Diesel')])
    submit = SubmitField('Submit')

class MotorcycleForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Type', choices=[
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large')
    ])
    submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Fuel', choices=[('No Fossil Fuel', 'No Fossil Fuel')])
    submit = SubmitField('Submit')

class TrainForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Travel area', choices=[
        ('Norway', 'Norway'),
        ('EU', 'EU')
    ])
    submit = SubmitField('Submit')

class WalkForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[DataRequired()], render_kw={"step": "any"})
    fuel_type = SelectField('Fuel', choices=[('No Fossil Fuel', 'No Fossil Fuel')])
    submit = SubmitField('Submit')
