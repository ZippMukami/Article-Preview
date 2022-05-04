from curses import tigetflag
from email import message
from turtle import title
from flask import render_template
from app import app
from .request import get_bulletins, get_bulletin


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

@app.route('/bulletin/<int:id>')    
def bulletin(id):
    '''
    View bulletin page function that returns the bulletin page and its dat
    '''

    bulletin = get_bulletin(id)
    title = f'{bulletin.title}'

    return render_template('bulletin.html', title = title, bulletin = bulletin)