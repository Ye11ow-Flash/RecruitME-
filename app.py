from flask import Flask, render_template, url_for, request, jsonify, redirect
from flask_cors import CORS, cross_origin
from werkzeug import secure_filename
from scripts.json_handler import *
import nltk
nltk.download("stopwords")
from pyresparser import ResumeParser
import requests
import json
import os
import shutil
from math import ceil
from Naive_Bayes import *



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "data"
CORS(app)




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


def get_query(condition):

  arr = [0 for i in range(len(s_skills))]

  for i in condition:
    if i in d_skills.keys():
      arr[d_skills[i]] = 1

  return arr


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

	username = request.form["username"]

	data = load(user)
	model = load("data/model.json")

	if True:	
		if request.method == 'POST':
			f = request.files['file']
			#f.save(secure_filename(f.filename))
			#shutil.move(secure_filename(f.filename), "data/")
			print(1111)
			resume = ResumeParser("data/"+secure_filename(f.filename)).get_extracted_data()
			print(resume)
			model = load("data/model.json")
			print(1)
			nb = [Naive_Bayes(model[str(i)]) for i in range(11)]
			print(2)
			print(nb)
			predictions = [nb[i].predict(get_query(resume["skills"])) for i in range(11)]
			data[username]["rating"] = predictions 
			summ = 0
			for i in predictions:
				summ += i[1]
			data[username]["avg_rating"] = summ/11

			data[username]["resume"] = secure_filename(f.filename)
			data[username]["skills"] = resume["skills"]
			data[username]["total_experience"] = resume["total_experience"]
			dump(user, data)
			#os.system("mv ")
	else:
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

@app.route("/profile")
def profile():
	username = request.args.get("username")
	data = load(user)
	print(data[username])
	return render_template("profile.html", username = username, mobile = data[username]["mobile"], emailid = data[username]["emailid"])


@app.route("/load_data")
def load_data():

	try:
		experience = int(request.args.get("experience"))
	except:
		experience = 0
	position = request.args.get("position")
	skill = request.args.get("skill")

	print(position, experience, skill)

	if position == "":

		data1 = load(user)
		data = {}
		for i in data1.keys(): 
			if data1[i]["t"] == 0 and data1[i]["total_experience "] >= experience:
				if skill == "":
					data[i] = data1[i]
				elif skill in data1[i]["skills"]:
					data[i] = data1[i]

		arr = sorted([[data[i]["avg_rating"], ceil(data[i]["total_experience "]), data[i]["resume"], i, data[i]["emailid"]] for i in data.keys()], reverse=True)

		return jsonify(data = arr)

	else:

		data1 = load(user)
		data = {}
		for i in data1.keys():
			if data1[i]["t"] == 0 and data1[i]["total_experience "] >= experience:
				if skill == "":
					data[i] = data1[i]
				elif skill in data1[i]["skills"]:
					data[i] = data1[i]

		arr = sorted([[data[i]["rating"][int(position)-1], ceil(data[i]["total_experience "]), data[i]["resume"], i, data[i]["emailid"]] for i in data.keys()], reverse=True)

		return jsonify(data = arr)







	#return render_template("index.html")
	return ""



if __name__ == "__main__":
   	app.run(debug = True)


   
   