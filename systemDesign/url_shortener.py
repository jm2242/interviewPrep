# pseudocode for the URL shortener 


def shortlink(request):
	# ignore non post for now
	if request.method is not 'POST':
		return Error501

	# the destination URL for us to redirect
	destionation = request.data.destination

	# use the slug if included
	if request.data.slug:
		slug = request.data.slug

	else:
		slug = generate_random_slug()


	DB.insert('Links',{'slug': slug, 'destination:': destination})


	#send a response bag with slug
	response_body = {
		'slug': : slug
	}

	return Success200(json.format(response_body))


# redirect endpoint
def redirect(request):
	destination = DB.get('Links','destionation',{'slug':request.path})
	return Redirect302(destination)


# basic way to produce slug, not considering duplicates

def gen_slug_basic():
	alphabet = "ABCDEFGHIJKLMNOPQURSTUVQXYZabcdefghijklmnopqurstuvwxyz123456789"
	num_chars = 7
	return ''.join([random.choice(alphabet) for _ in range num_chars] )

# generate slug by keeping track of a base 62 global id that is 
# constantly incremented
def gen_slug_base62():
	global current_id
	while True:
		slug = base_convert(current_id, base_62_alphabet)
		current_id += 1

		# make sure slug isn't already used
		existing = db.get(slug)
		if not existing:
			return slug









