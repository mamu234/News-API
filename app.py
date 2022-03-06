from flask import Flask, render_template 
from newsapi import NewsApiClient
from pip import main

app = Flask(__name__)

@app.route('/')
def home():
 

    newsapi =NewsApiClient(api_key='6cc037b2e9984d0b995fb8d87f06d897')


    top_headlines = newsapi.get_top_headlines(sources='bbc-news')

    #soruces is where news comes into the app

    t_articles = top_headlines['articles']
    #fetching all the articles of top headlines  news


     # making a list  of news contant  to store  the value on the list
    news = []
    desc = []
    img = []
    p_date = []
    url = []


     #fetching  all the cotent using for loop

    for i in range(len(t_articles)):
        main_article = t_articles[i]

        #append all th content in to each of list 

        news.append(main_article['title'])
        desc.append(main_article ['description'])
        img.append(main_article ['img'])
        p_date.append(main_article ['p_date'])
        url.append(main_article ['url'])


        #making a zip to access th contant directly

        contents = zip(news,desc, img ,p_date ,url)

        # pass the zip  into the render file
    

    return render_template('home.html',contents = contents)


if __name__ == '__main__':
    app.run(debug=True)


