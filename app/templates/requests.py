from unicodedata import category
import urllib.request,json
from .models import news
from app import app

News = news.News


api_key = None

base_url = None


api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
          news_details_data = url.read()
          news_details_response = json.loads(news_details_data)

          news_object = None
          if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('original_title')
            description = news_details_response.get('overview')
            poster = news_details_response.get('poster_path')
            category= news_details_response.get('vote_average')
            langauge = news_details_response.get('vote_count')
            country = news_details_response.response('country')

          news_object = News(id,name,description,poster, category, langauge,country)
    

    
    return news_object



   