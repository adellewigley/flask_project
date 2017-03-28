from flask import Flask
from flask import render_template
from flask import request
import requests

key = 'key-dbbfdd32c5ffdc0cdb9577081f8ee6eb'
sandbox = 'sandboxfd3e228eeea14bf7b53c121ddb03a64a.mailgun.org'

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('hello.html')

@app.route("/<name>")
def hello_name(name):
		return render_template("hello.html",name=name.title())

@app.route('/404')
def error_404():
	return "you should not be here"

@app.route('/200')
def adelle():
	return "adelles page"

@app.route("/contact", methods=['POST'])
def contact():
		print("test")
		form_data= request.form

		name = form_data['name']
		message = form_data['message']
		email = form_data['Email']

		print(name, message, email)

		# email message
		subject = 'Hello from Adelle'
		body = 'Hello! This is a test.'

		sender = 'aw1n15@soton.ac.uk'

		# sending message
		request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)

		email_request = requests.post(request_url, auth=('api', key), data={
			'from': sender,
			'to': email,
			'subject': subject,
			'text': body
			})

		# checking email status
		print('status:{0}'.format(email_request.status_code))
		print('Body {0}'.format(email_request.text))

		return("Form works!")

if __name__ == "__main__":
	app.run()




