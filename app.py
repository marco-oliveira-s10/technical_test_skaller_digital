# app.py
from flask import Flask
from routes.email import email_bp

app = Flask(__name__)
app.register_blueprint(email_bp)

if __name__ == '__main__':
    app.run(debug=True)