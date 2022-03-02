from flask import render_template,request,redirect,url_for
from app import app

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

