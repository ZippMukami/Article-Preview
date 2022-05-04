from curses import tigetflag
from email import message
from turtle import title
from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - welcome to Article Review!'
    return render_template('index.html', title = title)

@app.route('/bulletin/<int:bulletin_id>')    
def bulletin(bulletin_id):
    '''
    View bulletin page function that returns the bulletin page and its dat
    '''

    return render_template('bulletin.html', id = bulletin_id)