from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField, validators

class TaskForm(FlaskForm):
    tasktype = SelectField("Task type", choices=[('Design', 'Design'), ('Programming', 'Programming'), ('Testing', 'Testing'), ('Maintenance', 'Maintenance'), ('Other', 'Other')])
    description = StringField("Description", [validators.Length(min=2)])
    time = IntegerField("Time")
 
    class Meta:
        csrf = False
