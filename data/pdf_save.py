from werkzeug import secure_filename


def save(f):
	print(f.filename)
	f.save(secure_filename(f.filename))

    