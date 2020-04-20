#!C:\Python\Python37\python.exe
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')
