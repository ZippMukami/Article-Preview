from email import message
from re import A
from flask import render_template
from app import app
from .request import get_news

#views
@app.route('/')
def index():

    title = 'Home - Welcome to Article Review. This should be it!'
    return render_template ('index.html', title = title)


@app.route('/news/<int:news_id>')
def news(news_id):

     return render_template('news.html', id = news_id)