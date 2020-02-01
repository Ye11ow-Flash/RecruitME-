from flask import Flask, render_template, url_for, request, jsonify
import requests
import json


app = Flask(__name__)

@app.route("/")
def index():
	return render_template(".html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/article")
def article():

	title = "Rahul, Iyer show their worth as India make light work of 204 target "
	source = "Cricbuzz"
	author = "Cricbuzz Staff"
	description = "Not the city, the $57 million-funded cryptocurrency custodian startup. When someone wants to keep tens or hundreds of millions of dollars in Bitcoin, Ethereum, or other coins safe, they put them in Anchorage’s vault. And now they can trade straight from custo…"
	urlToImage = "https://techcrunch.com/wp-content/uploads/2020/01/Anchorage-Trading-1.png?w=740"
	publishedAt = "2020-01-15T11:57:30Z"


	return render_template("main.html", title = title, source = source, author = author, description = description, urlToImage = urlToImage, publishedAt = publishedAt)

if __name__ == "__main__":
   	app.run(debug = True)


   
   