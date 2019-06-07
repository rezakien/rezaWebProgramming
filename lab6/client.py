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
	ID_Test = request.args.get("ID_Test") # возвращает get параметры из url
	NameQuestion = request.args.get("NameQuestion")
	getTest = requests.get("http://localhost:5000/tests/" +str(ID_Test)+"")
	ID_Test = getTest.text.replace('"','').split("|")[0]
	NameTest = getTest.text.replace('"','').split("|")[1]
	return render_template("add.html",ID_Test=ID_Test,NameTest=NameTest,NameQuestion=NameQuestion,QuestionAdded=True)

@app.route("/addAnswer",methods=["POST"])
def addAnswer():
	answers = [answer for answer in request.form.getlist("answer") if answer!= ""]
	checks = [check for check in request.form.getlist("check")]
	ID_Test = request.form["ID_Test"]
	NameQuestion = request.form["NameQuestion"]
	
	r = requests.post("http://localhost:5000/questions",data={"answers":answers,"checks":checks,"NameQuestion":NameQuestion,"ID_Test":ID_Test})
	return "ok"
if __name__ == "__main__":
	app.run(port=5001)