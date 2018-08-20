import markdown






def note_text_to_html(s):
	#return s.replace('\n', '</p><p>')
	return markdown.markdown(s)

NOTEBOOK_FILTERS = {
	'note_text_to_html': note_text_to_html,
}