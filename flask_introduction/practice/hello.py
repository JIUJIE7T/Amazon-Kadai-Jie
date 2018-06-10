from flask import Flask,request,Response
from flask_httpauth import HTTPBasicAuth #authentication
import re

app = Flask(__name__) 
auth = HTTPBasicAuth() #authentication


users = {
	"amazon":"candidate"
}

@auth.get_password
def get_pw(username):
	if username in users:
		return users.get(username)
	else:
		return 401
	return None


@app.route('/')
def hello_world():
    return 'AMAZON'


@app.route('/secret/')
@auth.login_required
def index():
	return "SUCCESS"


@app.route('/calc')
def calculation():
    input = request.query_string
    if re.match('^[0-9\+\-\*\/\(\)]+$',input):
    	result = str(eval(input))
    	return result
    else:	
    	return "ERROR"


@app.route('/stocker')




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=8080)
