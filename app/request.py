from ast import Return
from turtle import title
from app import app
import urllib.request, json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        # print(get_news_response)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results       


def process_results(news_list):
    '''
    Function that processes the movie result and transform them to a list of Objects
    '''

    # print(news_list)
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')

        news_object = News(id, title, description, urlToImage, content, publishedAt)
        news_results.append(news_object)


    # print(news_results)

    return news_results


def get_news(id):
    get_news_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get ('id')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            urlToImage = news_details_response.get('urlToImage')
            content = news_details_response.get('content')
            publishedAt = news_details_response.get('publishedAt')

            news_object = News(id, title, description, urlToImage, content, publishedAt)

    return news_object            




