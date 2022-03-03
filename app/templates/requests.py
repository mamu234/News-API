from unicodedata import category
import urllib.request,json
from  models import news
from app import app


News = news.News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
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
    
def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=6cc037b2e9984d0b995fb8d87f06d897'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = search_news_results(search_news_list)
    
    return search_news_results



   