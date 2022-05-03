from email import message
from re import A
from flask import render_template
from app import app

#views
@app.route('/')
def index():
     message = "Better luck this time"
     return render_template ('index.html', message = message)


@app.route('/news/<int:news_id>')
def news(news_id):

     return render_template('news.html', id = news_id)