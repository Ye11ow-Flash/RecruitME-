from flask import Flask, render_template, url_for, request, jsonify
import requests
import json


app = Flask(__name__)

#for candidate
@app.route("/login")
def login():
	return render_template("login.html")

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


   
   