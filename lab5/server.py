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
app.config['MYSQL_DATABASE_DB'] = 'pp_lab2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# RESTful Classes
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
		# User.safe(resp)
		return resp

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
			# User.safe(resp)
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
			# User.safe(resp)
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
			# User.safe(resp)
			return {'Client was deleted by name': name,'method':request_m}
	def safe(res):
		with open("result.json", "a") as op:
			json.dump(res, op,indent=2)
			op.write("\n")
class Order(Resource):
	def get(self,order_id=None):
		if order_id is None:
			cursor.callproc("getOrders")
			data = cursor.fetchall()
		else:
			args = [order_id]
			cursor.callproc("getOrder",args)
			data = cursor.fetchone()
		request_url = request.url
		request_m = request.method
		resp = dict(table='Orders',response=data,method=request_m,url=request_url)
		# Order.safe(resp)

	def post(self):
		order_date = request.form['date']
		client_id = request.form['client_id']
		request_m = request.method
		request_url = request.url
		args = [order_date,client_id]
		cursor.callproc("addOrder",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders',response=args,method=request_m,url=request_url)
			#Order.safe(resp)
			return {'Created new order by args': args,'method':request_m}
	
	def put(self):
		id_order = request.form['id_order']
		id_client = request.form['client_id']
		order_date = request.form['date']
		request_m = request.method
		request_url = request.url
		args = [id_order,order_date,id_client]
		cursor.callproc("updateOrder",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders',response=args,method=request_m,url=request_url)
			#Order.safe(resp)
			return {'Orders was updated id': id_order,'method':request_m}
	
	def delete(self):
		id_order = request.form['id_order']
		request_m = request.method
		request_url = request.url
		args = [id_order]
		cursor.callproc("deleteOrder",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders',response=args,method=request_m,url=request_url)
			#Order.safe(resp)
			return {'Order was deleted by id': id_order,'method':request_m}
	def conv(o):
		if isinstance(o, datetime.datetime):
			return "{}-{}-{}".format(o.year, o.month, o.day)
	def safe(res):
		with open("result.json", "a") as op:
			json.dump(res, op,indent=2,default=Order.conv)
			op.write("\n")
class Service(Resource):
	def get(self,service_id=None):
		if service_id is None:
			cursor.callproc("getServices")
			data = cursor.fetchall()
		else:
			args = [service_id]
			cursor.callproc("getService",args)
			data = cursor.fetchone()
		request_url = request.url
		request_m = request.method
		resp = dict(table='Services',response=data,method=request_m,url=request_url)
		#Service.safe(resp)
		return resp

	def post(self):
		name = request.form['name']
		price = request.form['price']
		request_m = request.method
		request_url = request.url
		args = [name,price]
		cursor.callproc("addService",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Services',response=args,method=request_m,url=request_url)
			#Service.safe(resp)
			return {'Created new service by args': args,'method':request_m}
	
	def put(self):
		id_service = request.form['id_service']
		name = request.form['name']
		price = request.form['price']
		request_m = request.method
		request_url = request.url
		args = [id_service,name,price]
		cursor.callproc("updateService",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Services',response=args,method=request_m,url=request_url)
			#Service.safe(resp)
			return {'Service was updated by id': id_service,'method':request_m}
	
	def delete(self):
		id_service = request.form['id_service']
		request_m = request.method
		request_url = request.url
		args = [id_service]
		cursor.callproc("deleteService",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders',response=args,method=request_m,url=request_url)
			#Service.safe(resp)
			return {'Service was deleted by id': id_service,'method':request_m}
	def conv(o):
		if isinstance(o, datetime.datetime):
			return "{}-{}-{}".format(o.year, o.month, o.day)
	def safe(res):
		with open("result.json", "a",encoding="utf-8") as op:
			json.dump(res, op,indent=2,default=Order.conv,ensure_ascii=False)
			op.write("\n")
class Orders_Services(Resource):
	def get(self,os_id=None):
		if os_id is None:
			cursor.callproc("getOSS")
			data = cursor.fetchall()
		else:
			args = [os_id]
			cursor.callproc("getOS",args)
			data = cursor.fetchone()
		request_url = request.url
		request_m = request.method
		resp = dict(table='Orders & Services',response=data,method=request_m,url=request_url)
		#Orders_Services.safe(resp)

	def post(self):
		order_id = request.form['order_id']
		service_id = request.form['service_id']
		quentity = request.form['quentity']
		request_m = request.method
		request_url = request.url
		args = [order_id,service_id,quentity]
		cursor.callproc("addOS",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders & Services',response=args,method=request_m,url=request_url)
			#Orders_Services.safe(resp)
			return {'Created new OS by args': args,'method':request_m}
	
	def put(self):
		order_id = request.form['order_id']
		service_id = request.form['service_id']
		quentity = request.form['quentity']
		OS_id = request.form['OS_id']
		request_m = request.method
		request_url = request.url
		args = [order_id,service_id,quentity,OS_id]
		cursor.callproc("updateOS",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders & Services',response=args,method=request_m,url=request_url)
			#Orders_Services.safe(resp)
			return {'OS was updated id': OS_id,'method':request_m}
	
	def delete(self):
		id_OS = request.form['id_OS']
		request_m = request.method
		request_url = request.url
		args = [id_OS]
		cursor.callproc("deleteOS",args)
		response = cursor.fetchall()
		if len(response)==0:
			conn.commit()
			resp = dict(table='Orders & Services',response=args,method=request_m,url=request_url)
			#Orders_Services.safe(resp)
			return {'OS was deleted by id': id_OS,'method':request_m}
	def conv(o):
		if isinstance(o, datetime.datetime):
			return "{}-{}-{}".format(o.year, o.month, o.day)
	def safe(res):
		with open("result.json", "a") as op:
			json.dump(res, op,indent=2,default=Order.conv,ensure_ascii=False)
			op.write("\n")

# Adding routing to REST
api.add_resource(User,'/getUsers','/getUsers/<string:user_id>')
api.add_resource(Order,'/getOrders','/getOrders/<string:order_id>')
api.add_resource(Service,'/getServices','/getServices/<string:service_id>')
api.add_resource(Orders_Services,'/getOS','/getOS/<string:os_id>')

if __name__ == "__main__":
	app.run()