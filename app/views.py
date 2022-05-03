from email import message
from re import A
from flask import render_template
from app import app

#views
@app.route('/')
def index():
     message = "Better luck this time"
     return render_template ('index.html', message = message)