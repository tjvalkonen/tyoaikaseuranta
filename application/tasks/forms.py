from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class TaskForm(FlaskForm):
    taskType = StringField("Task type", [validators.Length(min=2)])
    description = StringField("Description", [validators.Length(min=2)])
    time = IntegerField("Time")
 
    class Meta:
        csrf = False
