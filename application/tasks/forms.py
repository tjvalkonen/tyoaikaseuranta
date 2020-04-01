from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, DecimalField, validators

class TaskForm(FlaskForm):
    taskType = StringField("Task type", [validators.Length(min=2)])
    description = StringField("Description", [validators.Length(min=2)])
    time = DecimalField("Time", [validators.Length(min=1)])
 
    class Meta:
        csrf = False
