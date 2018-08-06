from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class NoteForm(FlaskForm):

	text = StringField('Note text', validators=[DataRequired()])
	title = StringField('Title')
	tags = StringField('Note tags')
	url = StringField('Note URL')