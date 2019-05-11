from flask import Flask,request,jsonify, Response,request
from flaskext.mysql import MySQL
from flask_restful import Resource,Api
import json

app = Flask(__name__)
api = Api(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pp_lab2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

class User(Resource):
	def get(self,user_id=None):
		if user_id is None:
			cursor.callproc("getClients")
			data = cursor.fetchall()
		else:
			args = [user_id]
			cursor.callproc("getClient",args)
			data = cursor.fetchone()
		request_url = request.url
		request_m = request.method
		resp = dict(table='Clients',response=data,method=request_m,url=request_url)
		User.safe(resp)

	def post(self):
		data = request.form['name']
		request_m = request.method
		request_url = request.url
		args = [data]
		cursor.callproc("addClient",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Clients',response=data,method=request_m,url=request_url)
			User.safe(resp)
			return {'Created new client by name': args,'method':request_m}
	
	def put(self):
		name = request.form['name']
		_id = request.form['_id']
		request_m = request.method
		request_url = request.url
		args = [_id,name]
		cursor.callproc("updateClient",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Clients',response=args,method=request_m,url=request_url)
			User.safe(resp)
			return {'Clients was updated id': _id,'method':request_m}
	
	def delete(self):
		name = request.form['name']
		request_m = request.method
		request_url = request.url
		args = [name]
		cursor.callproc("deleteClient",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Clients',response=args,method=request_m,url=request_url)
			User.safe(resp)
			return {'Client was deleted by name': name,'method':request_m}
	def safe(res):
		with open("result.json", "a") as op:
			json.dump(res, op)
			op.write("\n")

api.add_resource(User,'/getUsers','/getUsers/<string:user_id>')
if __name__ == "__main__":
	app.run()