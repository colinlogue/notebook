import datetime

from flask import render_template, redirect, Blueprint
from flask_pymongo import PyMongo

from .db import mongo



notebook = Blueprint('notebook', __name__,
						templat_folder='templates',
						static_folder='static')

### constants ###
ASCENDING = 1
DESCENDING = -1

### app routes ###
@notebook.route('/')
def home():
	"""Displays all notes from notebook"""
	notes = mongo.db.notebook.find().sort('_id', DESCENDING)
	return render_template('notes/view.html', notes=notes)

@notebook.route('/add', methods=['GET', 'POST'])
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

		mongo.db.notebook.insert_one(note)
		return redirect('/notes/view')

	return render_template('notes/new.html', form=form)

@notebook.route('/view/<note_id>')
def view_notes():
	"""Displays a single from notebook"""
	notes = mongo.db.notebook.find_one({'_id':note_id}).sort('_id', DESCENDING)
	return render_template('notes/view.html', notes=notes)

@notebook.route('/tdl')
def tdl():
	"""Displays the TDL page."""
	items = mongo.db.to_do_list.find({})
	return render_template('tdl.html', items=items)