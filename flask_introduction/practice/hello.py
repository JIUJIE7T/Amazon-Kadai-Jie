from flask import Flask,request,Response,g
from flask_httpauth import HTTPBasicAuth #authentication
import re
import sqlite3

app = Flask(__name__) 

#question 2 Authentication ------------------------------------
users = {
	"amazon":"candidate"
}

auth = HTTPBasicAuth() #authentication
@auth.get_password
def get_pw(username):
	if username in users:
		return users.get(username)
	else:
		return 401
	return None

#--------------------------------------------------------------

#question 1----------------------------------------------------

@app.route('/')
def hello_world():
    return 'AMAZON'

#question 2-----------------------------------------------------

@app.route('/secret/')
@auth.login_required
def index():
	return "SUCCESS"

#question 3-----------------------------------------------------
@app.route('/calc')
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
	# function = request.args.get('function')
	# name = request.args.get('name')
	# amount = request.args.get('amount')
	# price = request.args.get('price')
	cursor.execute("INSERT INTO STORAGE (NAME,AMOUNT,SALES)\
		VALUES('asdf',3,0);")
	conn.commit()
	conn.close()

	return "YES"

# 	if function == "addstock":
# 		cursor.execute("INSERT INTO STORAGE (NAME,AMOUNT)\
# 			VALUES("+name+","+amount+")")

# # 	if function == "checkstock":
# # 		#do something
# # 	if function == "sell" :
# # 		#do something
# # 	if function == "checksales":
# 		#do something
	
# 	if function == "deleteall":
# 		cursor.execute("DELETE FROM STORAGE")
# 	else:
# 		return "INPUT ERROR"



# def getfunction():
# 	#get function name
# 	function = request.args.get('function')

# 	#check function type
# 	if function == 'addstock':
# 		name = request.args.get('name')
# 		amount = request.args.get('amount')
# 		#check input 
# 		if name is None:
# 			return "Parameter Missing"
# 		if amount is None:
# 			amount = 1
# 			print(amount)
# 		else:
# 			print(amount)


# 			#return "ojbk"#delete this line later



# 	if function == 'checkstock':
# 		name = request.args.get('name')
# 		if name is None:
# 			return "Parameter Missing"
# 		else:
# 			return "ojbk"#delete this line later

# 	if function == 'sell':
# 		name = request.args.get('name')
# 		amount = request.args.get('amount')
# 		price = request.args.get('price')
# 		if name is None or amount is None or price is None:
# 			return "Parameter Missing"
# 		else:
# 			return "ojbk"

# 	if function == 'checksales':
# 		return function

# 	if function == 'deleteall':
# 		return function

# 	else:
# 		return "input ERROR"


#Start server----------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=8080)
