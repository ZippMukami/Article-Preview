from email import message
from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    message = "Articles Review Page"
    return render_template('index.html', message = message)

@app.route('/bulletin/<bulletin_id>')    
def bulletin(bulletin_id):
    '''
    View bulletin page function that returns the bulletin page and its dat
    '''
    return render_template('bulletin.html', id = bulletin_id)