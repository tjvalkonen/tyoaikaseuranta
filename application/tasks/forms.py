from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField, validators

class TaskForm(FlaskForm):
    tasktype = SelectField("Task type", choices=[('Design', 'Design'), ('Programming', 'Programming'), ('Testing', 'Testing'), ('Maintenance', 'Maintenance'), ('Other', 'Other')])
    taskstatus = SelectField("Task status", choices=[('Actual', 'Actual'), ('Estimate', 'Estimate')])
    description = StringField("Description", [validators.Length(min=2)])
    time = IntegerField("Time in hours")
 
    class Meta:
        csrf = False
