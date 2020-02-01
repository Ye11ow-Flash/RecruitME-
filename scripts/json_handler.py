import json


user = "data/user_data.json"


def load(filename):

	with open(filename, "r") as f:
		data = json.load(f)

	return data
	

def dump(filename, data):

	with open(filename, "w") as f:
		data = json.dump(data, f)



def validate(username, password):

	data = load(user)

	if username not in data.keys():
		return False,-1

	if data[username]["password"] != password:
		return False,-1

	return True, data[username]


def signup_user(username, password, mobile, emailid, t):
	print(username, password, mobile, emailid, t)
	data = load(user)
	print(1111)

	data[username] = {"password":password, "mobile":mobile, "emailid":emailid, "t":t}

	dump(user, data)






