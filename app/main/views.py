from flask import render_template,request,redirect,url_for
from app import app
from templates.requests import get_news,get_news,search_news
from templates.models import News, Sources, source
from app.forms import SourceForm
Source= source.Source

all_sources = []

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


@app.route('/news/source/new/<int:id>', methods = ['GET','POST'])
def new_source(id):
    form = SourceForm()
    movie = get_news(id)

    if form.validate_on_submit():
        title = form.title.data
        source = form.source.data
        new_source = Source(News.id,title,News.poster,source)
        new_source.save_source()
        return redirect(url_for('news',id = News.id ))

    title = f'{News.title} source'
    return render_template('new_source.html',title = title, source_form=form, news=News)

@classmethod
def get_reviews(cls,id):

        response = []

        for source in cls.all_sources:
            if source.news_id == id:
                response.append(source)

        return response


@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'
    sources = Sources.get_sources(sources.id)

    return render_template('news.html',title = title,news = news,sources = sources)