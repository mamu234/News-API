from app import app, render_template
from templates.requests import News, get_news
from templates.requests import get_news,get_news,search_news



# Views
@app.route('/news/<int:id>')
def news(id):
    news = get_news(id)
    title = f'{news.title}'

@app.route('/search/<news_name>')
def search(news_name):


 news_name_list = news_name.split(" ")
 news_name_format = "+".join(news_name_list)
 searched_news = search_news(news_name_format)
 title = f'search results for {news_name}'
    
 return render_template('search.html',movies = searched_news)

