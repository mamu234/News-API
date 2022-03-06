from flask import Flask, render_template 
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('home.html')

newsapi =NewsApiClient(api_key='6cc037b2e9984d0b995fb8d87f06d897')


top_headlines = newsapi.get_top_headlines(sources='bbc-news')

if __name__ == '__main__':
    app.run(debug=True)


