from flask import Flask,render_template,url_for,request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("main.html")

@app.route("/add")
def getAddingPage():
	return render_template("add.html")


@app.route("/addTest",methods=["POST"])
def addTest():
	form_data = request.form
	NameTest = form_data["NameTest"]
	r = requests.post("http://localhost:5000/tests",data={"NameTest":NameTest})
	getTest = requests.get("http://localhost:5000/tests/" +r.text+"")
	ID_Test = getTest.text.replace('"','').split("|")[0]
	NameTest = getTest.text.replace('"','').split("|")[1]
	return render_template("add.html",ID_Test=ID_Test,NameTest=NameTest)

@app.route("/addQuestion",methods=["POST","GET"])
def addQuestion():
	form_data = request.args.get("ID_Test") # возвращает get параметры из url
	
	getTest = requests.get("http://localhost:5000/tests/" +form_data+"")
	ID_Test = getTest.text.replace('"','').split("|")[0]
	NameTest = getTest.text.replace('"','').split("|")[1]
	return render_template("add.html",ID_Test=ID_Test,NameTest=NameTest,QuestionAdded=True)
if __name__ == "__main__":
	app.run(port=5001)