from app import app, render_template
from templates.requests import get_news

# Views
@app.route('')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   # Getting latest news
    latest_news= get_news('latest')
    breaking_news = get_news('breaking_news')
    now_showing_news = get_news('now playing')
    title = 'Home - Welcome to The best news  Website Online'
    return render_template('index.html', title = title,latest = latest_news,breaking_news = breaking_news, now_showing_news = now_showing_news)

