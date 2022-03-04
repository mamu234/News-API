import urllib.request,json
from .models import News




# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(id):
    get_news_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
         news_details_data = url.read()
         news_details_response = json.loads(news_details_data)

         news_object = None
         if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            poster = news_details_response.get('poster')
            category= news_details_response.get('category')
            langauge = news_details_response.get('language')
            country = news_details_response.get('country')

         news_object = News(id,name,description,poster, category, langauge,country)
    
def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/everything?api_key={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = search_news_results(search_news_list)
    
    return search_news_results



   