# app.py
from flask import Flask
from flask_restx import Api
from routes.email import email_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='Email Service API', description='A simple API for sending emails')

# Register namespaces
api.add_namespace(email_ns, path='/email')

if __name__ == '__main__':
    app.run(debug=True)
