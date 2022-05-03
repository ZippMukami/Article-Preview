from email import message
from re import A
from turtle import title
from flask import render_template
from app import app
from .request import get_news, get_news

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting top headlines
    top_headlines = get_news('headlines')

    #Getting everything
    everything = get_news('everything')

    



    title = 'Home - Welcome to Article Review.'
    return render_template ('index.html', title = title, headlines = top_headlines, everything = everything)


@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'


    return render_template('news.html', title = title, news = news)