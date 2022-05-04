from distutils.debug import DEBUG

from instance.config import BULLETIN_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    BULLETIN_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=6721828ddfd14070b08e9d6d1e968e50'

class ProdConfig(Config):
    '''
    Produuction configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
     Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
