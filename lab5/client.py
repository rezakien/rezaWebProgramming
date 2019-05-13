from flask import Flask,render_template,url_for,request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("main.html")

@app.route("/getClient",methods=['POST'])
def getClient():
	form_data = request.form
	r = ''
	user_id = form_data['user_id']
	if user_id == "":
		r = requests.get("http://localhost:5000/getUsers")
	else:
		r = requests.get("http://localhost:5000/getUsers/" + user_id + "")
	return str(r.text)

@app.route("/postClient",methods=['POST'])
def postClient():
	form_data = request.form
	client_name = form_data['client_name']
	r = requests.post("http://localhost:5000/getUsers",data={'name':client_name})
	return str(r.text)

@app.route("/putClient",methods=['POST'])
def putClient():
	form_data = request.form
	_id = form_data['user_id']
	user_name = form_data['user_name']
	r = requests.put("http://localhost:5000/getUsers",data={'name':user_name,'_id':_id})
	return str(r.text)

@app.route("/deleteClient",methods=['POST'])
def deleteClient():
	form_data = request.form
	user_name = form_data['user_name']
	r = requests.delete("http://localhost:5000/getUsers",data={'name':user_name})
	return str(r.text)

@app.route("/getService",methods=['POST'])
def getService():
	form_data = request.form
	r = ''
	_id = form_data['_id']
	if _id == "":
		r = requests.get("http://localhost:5000/getServices")
	else:
		r = requests.get("http://localhost:5000/getServices/" + _id + "")
	return str(r.text)

@app.route("/postService",methods=['POST'])
def postService():
	form_data = request.form
	name = form_data['name']
	price = form_data['price']
	r = requests.post("http://localhost:5000/getServices",data={'name':name,'price':price})
	return str(r.text)

@app.route("/putService",methods=['POST'])
def putService():
	form_data = request.form
	id_service = form_data['id_service']
	name = form_data['name']
	price = form_data['price']
	r = requests.put("http://localhost:5000/getServices",data={'id_service':id_service,'name':name,'price':price})
	return str(r.text)

@app.route("/deleteService",methods=['POST'])
def deleteService():
	form_data = request.form
	id_service = form_data['id_service']
	r = requests.delete("http://localhost:5000/getServices",data={'id_service':id_service})
	return str(r.text)

if __name__ == "__main__":
	app.run(port=5001)