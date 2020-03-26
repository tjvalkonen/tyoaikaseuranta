from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ProjectForm(FlaskForm):
    name = StringField("Project name", [validators.Length(min=2)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False
