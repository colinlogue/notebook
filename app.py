import datetime

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

from forms import NoteForm
from filters import register_filters
from db import get_next_seq_val

from local.config import LocalConfig



### configure app ###
app = Flask(__name__)
app.config.from_object(LocalConfig)
register_filters(app)

### database ###
mongo = PyMongo(app)
notebook = mongo.db.notebook

### app routes ###
@app.route('/')
def home():
	"""Renders the home page."""
	return "<a href='/add-note'>Add a note</a>"

@app.route('/notes/add', methods=['GET', 'POST'])
def add_note():
	"""Renders or submits form to add a note to DB."""
	form = NoteForm()
	if form.validate_on_submit():
		note = {
			'_id': get_next_seq_val(mongo.db, 'note_id'),
			'text': form.text.data,
			'created_at': datetime.datetime.now(),
		} #object to be added to db

		if form.title.data:
			note['title'] = form.title.data
		if form.url.data:
			note['url'] = form.url.data
		if form.tags.data:
			note['tags'] = [t.strip('\"') for t in form.tags.data.split(',')]

		notebook.insert_one(note)
		return redirect('/notes/view')

	return render_template('notes/new.html', form=form)

@app.route('/notes/view')
def view_notes():
	"""Displays notes from notebook"""
	notes = notebook.find({})
	return render_template('notes/view.html', notes=notes)

@app.route('/tdl')
def tdl():
	"""Displays the TDL page."""
	items = mongo.db.to_do_list.find({})
	return render_template('tdl.html', items=items)