import datetime

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

from forms import NoteForm
from filters import register_filters
from db import get_next_seq_val

from local.config import LocalConfig


### constants ###
ASCENDING = 1
DESCENDING = -1



### configure app ###
app = Flask(__name__)
app.config.from_object(LocalConfig)
register_filters(app)

### database ###
mongo = PyMongo(app)
notebook = mongo.db.notebook