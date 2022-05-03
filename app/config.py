from distutils.debug import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=6721828ddfd14070b08e9d6d1e968e50'

class ProdConfig(Config):
    '''
    Production configuration child class
    '''

    pass


class DevConfig(Config): 
    '''
    Development configuration child class
    '''

    DEBUG = True