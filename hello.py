from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<luqman>")
def hello(luqman):
    return f"Hello,{escape(luqman)}!"

@app.route('/testing')
def testing():
    return 'saya, perintah testing'
