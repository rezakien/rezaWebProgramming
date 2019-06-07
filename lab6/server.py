from flask import Flask,request,jsonify, Response,request,render_template,url_for
from flaskext.mysql import MySQL
from flask_restful import Resource,Api
import json
import datetime
import sys

app = Flask(__name__)
api = Api(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pp_lab6'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# RESTful Classes
class Test(Resource):
	def get(self,test_id=None):
		resp = ""
		if test_id is None:
			cursor.callproc("getTest")
			data = cursor.fetchall()
		else:
			args = [test_id]
			cursor.callproc("getTest",args)
			data = cursor.fetchone()
			print(data)
			resp = "|".join([str(word) for word in data])
			print(resp)
		# request_url = request.url
		# request_m = request.method
		# resp = dict(table='Clients',response=data,method=request_m,url=request_url)
		# User.safe(resp)
		return resp

	def post(self):
		data = request.form['NameTest']
		request_m = request.method
		request_url = request.url
		args = [data]
		print(args)
		cursor.callproc("addTest",args)
		response = cursor.fetchall()
		if response is not None:
			# print(response[0][0]) - последний ID по тестам
			conn.commit()
			# resp = dict(table='Tests',response=data,method=request_m,url=request_url)
			# User.safe(resp)
			return response[0][0]
	
	# def put(self):
	# 	name = request.form['name']
	# 	_id = request.form['_id']
	# 	request_m = request.method
	# 	request_url = request.url
	# 	args = [_id,name]
	# 	cursor.callproc("updateClient",args)
	# 	response = cursor.fetchall()
	# 	if len(response)==0:
	# 		conn.commit()
	# 		resp = dict(table='Clients',response=args,method=request_m,url=request_url)
	# 		# User.safe(resp)
	# 		return {'Clients was updated id': _id,'method':request_m}
	
	# def delete(self):
	# 	name = request.form['name']
	# 	request_m = request.method
	# 	request_url = request.url
	# 	args = [name]
	# 	cursor.callproc("deleteClient",args)
	# 	response = cursor.fetchall()
	# 	if len(response)==0:
	# 		conn.commit()
	# 		resp = dict(table='Clients',response=args,method=request_m,url=request_url)
	# 		# User.safe(resp)
	# 		return {'Client was deleted by name': name,'method':request_m}
	def safe(res):
		with open("result.json", "a") as op:
			json.dump(res, op,indent=2)
			op.write("\n")

class Question(Resource):
	def get(self):
		pass
	def delete(self):
		pass
	def post(self):
		pass

class Answer(Resource):
	def get(self):
		pass
	def delete(self):
		pass
	def post(self):
		pass

# Adding routing to REST
api.add_resource(Test,'/tests','/tests/<string:test_id>')


if __name__ == "__main__":
	app.run()