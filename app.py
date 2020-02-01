from flask import Flask, render_template, url_for, request, jsonify, redirect
from scripts.json_handler import *
import requests
import json


app = Flask(__name__)

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
			return render_template("index.html", data = data)
		else:
			return render_template("demo.html", data = data)


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



@app.route("/demo")
def demo():
	return render_template("demo.html")


#for recruter
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


   
   