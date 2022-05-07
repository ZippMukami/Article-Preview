import os

class Config:
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=keyword&apiKey=6721828ddfd14070b08e9d6d1e968e50'



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}    