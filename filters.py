






def note_text_to_html(s):
	return s.replace('\n', '</p><p>')

ALL_FILTERS = {
	'note_text_to_html': note_text_to_html,
}

def register_filters(app, filters=ALL_FILTERS):
	for filt_name, filt_func in filters.items():
		app.jinja_env.filters[filt_name] = filt_func