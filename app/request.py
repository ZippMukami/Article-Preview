from ast import Return
from multiprocessing import process
from turtle import title
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
    

def get_bulletin(id):
    get_bulletin_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_bulletin_details_url) as url:
        bulletin_details_data = url.read()
        bulletin_details_response = json.loads(bulletin_details_data)

        bulletin_object = None
        if bulletin_details_response:
            id = bulletin_details_response.get('id')
            title = bulletin_details_response.get('title')
            description = bulletin_details_response.get('description')
            urlToImage = bulletin_details_response.get('urlToImage')
            content = bulletin_details_response.get('content')
            publishedAt = bulletin_details_response.get('publishedAt')

            bulletin_object = Bulletin(id, title, description, urlToImage, content, publishedAt)
   
    return bulletin_object


def search_bulletin(bulletin_name):
    search_bulletin_url = 'https://newsapi.org/v2/everything?api_key={}&query={}'.format(api_key,bulletin_name)
    with urllib.request.urlopen(search_bulletin_url) as url:
        search_bulletin_data = url.read()
        search_bulletin_response = json.loads(search_bulletin_data)

        search_bulletin_articles = None

        if search_bulletin_response['articles']:
            search_bulletin_list = search_bulletin_response['articles']
            search_bulletin_articles = process_articles(search_bulletin_list)

    return search_bulletin_articles
