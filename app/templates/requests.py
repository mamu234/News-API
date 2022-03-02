from unicodedata import category, name
from app import app
import urllib.request,json
from models import news

News = news.News


# api_key = None

# base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of  news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('original_name')
        description = news_item.get('description')
        url = news_item.get('url_path')
        category = news_item.get('category')
        langauge = news_item.get('langauge')
        country = news_item.get('country')

        if news:
            news_object = News(id,name,description,url,category,langauge,country)
            news_results.append(news_object)



    return news_results