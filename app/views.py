from curses import tigetflag
from email import message
from turtle import title
from flask import render_template
from app import app
from .request import get_bulletins


# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting headlines
    top_headlines = get_bulletins('headlines')
    everything = get_bulletins('everything')
    
    title = 'Home - welcome to Article Review!'
    return render_template('index.html', title = title, headlines = top_headlines, everything = everything)

@app.route('/bulletin/<int:bulletin_id>')    
def bulletin(bulletin_id):
    '''
    View bulletin page function that returns the bulletin page and its dat
    '''

    return render_template('bulletin.html', id = bulletin_id)