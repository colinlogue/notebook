from flask_pymongo import PyMongo
from pymongo import ReturnDocument



mongo = PyMongo()
notebook_db = mongo.db


def get_next_seq_val(db, seq_name):
	doc = db.counters.find_one_and_update(
		filter={"_id":seq_name},
		update={"$inc":{"sequence_val":1}},
		return_document=ReturnDocument.AFTER)
	return doc['sequence_val']