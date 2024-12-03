from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length

class CreateAssessment(FlaskForm):
    module_code = StringField('Module Code', validators=[InputRequired(),Length(min=8,max=8)])
    assess_title = StringField('Asessment Title', validators=[InputRequired(),Length(min=5,max=15)])
    description = TextAreaField('Description', validators=[InputRequired(),Length(max=50)])
    due_date = DateField('Due Date', format='%Y-%m-%d')