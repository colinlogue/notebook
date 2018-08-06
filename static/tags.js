
// tdl: load list of tags with page, add to whitelist

function initTags() {

	var input = document.querySelector('input[name=tags]');
	// init Tagify script on the above inputs
	tagify = new Tagify(input, {
	    whitelist : ['thoughts', 'programming']
	});
};

initTags();