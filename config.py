import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=keyword&apiKey=6cc037b2e9984d0b995fb8d87f06d897'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}