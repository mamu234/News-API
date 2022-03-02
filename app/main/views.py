from app import app, render_template
from templates.requests import News, get_news
from templates.requests import get_news,get_news

# Views
@app.route('/news/<int:id>')
def news(id):
    news = get_news(id)
    title = f'{news.title}'

    
    return render_template('news.html',title = title,news = news)

