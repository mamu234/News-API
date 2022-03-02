from flask import render_template,request,redirect,url_for
from app import app
from templates.requests import get_news,get_news,search_news

@app.route('/')
def index():
    latest_news = get_news('latest')
    breaking_news = get_news('breaking_news')
    now_showing_news = get_news('now_showing')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
     return redirect(url_for('search',news_name=search_news))
    else:
     return render_template('index.html', title = title, latest = latest_news, breaking = breaking_news, now_showing = now_showing_news )

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)