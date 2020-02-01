from flask import Flask, render_template, url_for, request, jsonify, redirect
from werkzeug import secure_filename
from scripts.json_handler import *
import requests
import json
import os
import shutil


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "data"




#for candidate
@app.route("/login")
def login():
	return render_template("login.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():

	username = request.form["username"]
	password = request.form["password"]

	flag, data = validate(username, password)
	print(data)
	if flag:

		if data["t"] == 1:
			return render_template("index.html", username = username)
		else:
			return render_template("demo.html", username = username, mobile = data["mobile"], emailid = data["emailid"])


	return render_template("login.html", message = "Invalid Name or Password")	



@app.route("/signup_cand", methods=["GET", "POST"])
def signup_cand():

	username = request.form["username"]
	password = request.form["password"]
	mobile = request.form["mobile"]
	emailid = request.form["emailid"]

	signup_user(username, password, mobile, emailid, 0)

	return render_template("demo.html")



@app.route("/signup_rect", methods = ["GET", "POST"])
def signup_rect():

	username = request.form["username"]
	password = request.form["password"]
	mobile = request.form["mobile"]
	emailid = request.form["emailid"]

	signup_user(username, password, mobile, emailid, 1)

	return render_template("index.html")


#For Candidate
@app.route("/demo")
def demo():
	return render_template("demo.html")


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

	username = request.form["username"]

	data = load(user)

	try:	
		if request.method == 'POST':
			f = request.files['file']
			f.save(secure_filename(f.filename))
			shutil.move(secure_filename(f.filename), "data/")

			data[username]["resume"] = secure_filename(f.filename)
			dump(user, data)
			#os.system("mv ")
	except:
		pass

	return render_template("demo.html", username = username, mobile = data[username]["mobile"], emailid = data[username]["emailid"])

#For Recruter
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/rectlogin")
def rectlogin():
	return render_template("rectlogin.html")

@app.route("/postjob")
def postjob():
	return render_template("postjob.html")

if __name__ == "__main__":
   	app.run(debug = True)


   
   