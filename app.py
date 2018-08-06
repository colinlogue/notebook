from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import datetime
from forms import NoteForm
from local.config import LocalConfig
from db import get_next_seq_val

app = Flask(__name__)
app.config.from_object(LocalConfig)
mongo = PyMongo(app)
notebook = mongo.db.notebook

@app.route('/')
def home():
	return "<a href='/add-note'>Add a note</a>"

@app.route('/add-note', methods=['GET', 'POST'])
def add_note():
	form = NoteForm()
	if form.validate_on_submit():
		note = {}
		note['text'] = form.text.data
		if form.title.data:
			note['title'] = form.title.data
		if form.url.data:
			note['url'] = form.url.data
		if form.tags.data:
			note['tags'] = [t.strip('\"') for t in form.tags.data.split(',')]
		note['created_at'] = datetime.datetime.now()
		note['_id'] = get_next_seq_val(mongo.db, 'note_id')
		notebook.insert_one(note)
		return redirect('/view-notes')
	return render_template('new_note.html', form=form)

@app.route('/view-notes')
def view_notes():
	notes = notebook.find({})
	return render_template('view_notes.html', notes=notes)

@app.route('/test-form', methods=['GET', 'POST'])
def test_form():
	form = NoteForm()
	if form.validate_on_submit():
		return redirect('/view-notes')
	return render_template('form.html', form=form)