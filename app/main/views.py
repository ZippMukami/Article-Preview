from curses import tigetflag
from email import message
from turtle import title
from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_bulletins, get_bulletin, search_bulletin
from ..models import Review
from .forms import ReviewForm


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting headlines
    top_headlines = get_bulletins('headlines')
    everything = get_bulletins('everything')
    
    title = 'Home - welcome to Article Review!'

    search_bulletin = request.args.get('bulletin_query')

    if search_bulletin:
        return redirect(url_for('search', bulletin_name = search_bulletin))
    else:

        return render_template('index.html', title = title, headlines = top_headlines, everything = everything)

@main.route('/bulletin/<int:id>')    
def bulletin(id):
    '''
    View bulletin page function that returns the bulletin page and its dat
    '''

    bulletin = get_bulletin(id)
    title = f'{bulletin.title}'

    return render_template('bulletin.html', title = title, bulletin = bulletin)


@main.route('/search/<bulletin_name>')
def search(bulletin_name):
    ''''
    View function to display the search results
    '''

    bulletin_name_list = bulletin_name.split(" ")
    bulletin_name_format = "+".join(bulletin_name_list)
    searched_bulletins = search_bulletin(bulletin_name_format)
    title = f'search articles for {bulletin_name}'
    return render_template('search.html', bulletins = searched_bulletins)
   


@main.route('/bulletin/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    bulletin = get_bulletin(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(bulletin.id, title, bulletin.urlToImage, review)
        new_review.save_review()
        return redirect(url_for('bulletin', id = bulletin.id))

    title = f'{bulletin.title} review'
    return render_template('new_review.html', title = title, review = form, bulletin = bulletin)
