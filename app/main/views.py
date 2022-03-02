from email import message
from flask import render_template, request,redirect,url_for
from  app  import main
from templates.requests import get_news,get_articles,serch_news
from  app.models import Articles

# Views
@main.route('')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Welcome to News search'
    return render_template('index.html',message = message)
