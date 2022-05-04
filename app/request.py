from multiprocessing import process
from unicodedata import category
from app import app
import urllib.request, json

from app.bulletin_test import Bulletin
from .models import bulletin

#Getting api key
api_key = app.config['BULLETIN_API_KEY']

#Getting the bulletin base url
base_url = app.config["BULLETIN_API_BASE_URL"]

def get_bulletins(category):
    ''''
    function that gets json response to our url request
    '''

    get_bulletins_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_bulletins_url) as url:
        get_bulletins_data = url.read()
        get_bulletins_response = json.loads(get_bulletins_data)

        bulletin_results = None

        if get_bulletins_response['articles']:
            bulletin_articles_list = get_bulletins_response['articles']
            bulletin_articles = process_articles(bulletin_articles_list)


    return bulletin_articles   



def process_articles(bulletin_list):
    '''
    function that processes the bulletin result and transform them to a list of objects
       Args:
        bulletin_list: A list of dictionaries that contain bulletin details

    Returns :
        bulletin_articles: A list of bulletin objects
    '''

    bulletin_articles = []
    for bulletin_item in bulletin_list:
        id = bulletin_item.get('id')
        title = bulletin_item.get('title')
        description = bulletin_item.get('description')
        urlToImage = bulletin_item.get('urlToImage')
        content = bulletin_item.get('content')
        publishedAt = bulletin_item.get('publishedAt')

        if urlToImage:
            bulletin_object = Bulletin(id, title, description, urlToImage, content, publishedAt)
            bulletin_articles.append(bulletin_object)

    return bulletin_articles
    


