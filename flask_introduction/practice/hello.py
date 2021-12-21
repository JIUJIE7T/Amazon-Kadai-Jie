from flask import Flask,request,Response,g
from flask_httpauth import HTTPDigestAuth #authentication
import re
import sqlite3

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'SECRET KEY HERE'

#question 2 Authentication ------------------------------------
users = {
	'aws':'candidate'
}

auth = HTTPDigestAuth() #authentication
@auth.get_password
def get_pw(username):
	if username in users:
		return users.get(username)
	else:
		return "SUCCESS"
	return None

#--------------------------------------------------------------

#question 1----------------------------------------------------

@app.route('/')
def hello_world():
    return 'AWS'

#question 2-----------------------------------------------------

@app.route('/secret/')
@auth.login_required
def index():
	return "SUCCESS"

#question 3-----------------------------------------------------
@app.route('stocks')
def calculation():
    input = request.query_string
    if re.match('^[0-9\+\-\*\/\(\)]+$',input):
    	result = str(eval(input))
    	return result
    else:	
    	return "ERROR"

#question 4-----------------------------------------------------
@app.route('/stocker')
def storage():
	conn = sqlite3.connect("storage.db")
	cursor = conn.cursor()
	function = request.args.get('function')
	name = request.args.get('name')
	amount = request.args.get('amount')
	price = request.args.get('price')

	if amount is None:
		amount = 1

	try:
		amount = int(amount)
	except ValueError:
		return "ERROR"

	if function == "addstock":
		#check if the thing is already in the stock
		if name is None:
			return "ERROR"
		else:
			cursor.execute("""SELECT NAME FROM STORAGE WHERE NAME = ? """,(name,))
			exist = cursor.fetchone()
			if exist:
				cursor.execute("""UPDATE STORAGE SET AMOUNT = AMOUNT + ? WHERE NAME = ? """,(amount,name))
				conn.commit()
				conn.close()
				return "EXISTING add sucessfully"

			else:
				#add a new product
				cursor.execute("""INSERT INTO STORAGE (NAME,AMOUNT,SALES) VALUES(?,?,0);""",(name,amount))
				conn.commit()
				conn.close()
				return "Operation Success"

	if function == "checkstock":
		if name is None:
			#print all stocks and sort
			stock = conn.execute("""SELECT NAME,AMOUNT FROM STORAGE """).fetchall() #get all stocks
			stock.sort(key = lambda l :(l[0]))	#sorting
			good = ""
			for goods in stock:
				good = good + "%s: %s\n"%(goods[0],goods[1])
			return good 
		else:
			#check if the thing is already in the stock
			cursor.execute("""SELECT NAME FROM STORAGE WHERE NAME = ? """,(name,))
			exist = cursor.fetchone()

			if exist:
				cursor.execute("""SELECT AMOUNT FROM STORAGE WHERE NAME = ? """,(name,))
				stock = cursor.fetchall()
				for amount in stock:
					return "%s:%d\n"%(name,amount[0])
				conn.close()
			else:
				return "%s:0"%(name)

	if function == "sell" :
		if name is None:
			return "ERROR"
		else:
			if price is None:
				cursor.execute("""UPDATE STORAGE SET AMOUNT = AMOUNT - ? WHERE NAME = ? """,(amount,name))
				conn.commit()
				conn.close()
				return "SUCCESS"
			if price <0:
				return "ERROR"				
			else:
				try:
					price = float(price)
				except ValueError:
					return "ERROR"
				sales_amount = amount * float(price)
				cursor.execute("""UPDATE STORAGE SET AMOUNT = AMOUNT - ?, SALES = SALES + ? WHERE NAME = ? """,(amount,sales_amount,name))
				conn.commit()
				conn.close()
				return "SUCCESS"

	if function == "checksales":
	 	sales = cursor.execute("""SELECT SALES FROM STORAGE""").fetchall()
		flattened = []
		for sublist in sales:
			for elements in sublist:
				flattened.append(elements)
		return "sales: %s"%(int(sum(flattened)))


	if function == "deleteall":
		cursor.execute("DELETE FROM STORAGE")
		conn.commit()
		conn.close()
		return "Operation Success"
	else:
		return "INPUT ERROR"


#Start server----------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=8080)
