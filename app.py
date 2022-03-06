from flask import Flask, render_template 
from newsapi import NewsApiClient
from pip import main

app = Flask(__name__)

@app.route('/')
def home():
 

    newsapi =NewsApiClient(api_key='6cc037b2e9984d0b995fb8d87f06d897')


    top_headlines = newsapi.get_top_headlines(sources='bbc-news')  #sources is where news comes into the app

    # for all the  sources
    all_articles = newsapi.get_everything(sources='bbc-news')

    t_articles = top_headlines['articles']  #fetching all the articles of top headlines  news

    #fetching all articles news  
    a_articles = all_articles['articles']


     # making a list  of news contant  to store  the value on the list
    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []


     #fetching  all the cotent using for loop

    for i in range(len(t_articles)):
        a_article = t_articles[i]

        #append all th content in to each of list 

        news_all.append(a_article['title'])
        desc_all.append(a_article ['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article ['publishedAt'])
        url_all.append(a_article ['url'])


        #making a zip to access th contant directly

        contents = zip(news_all,desc_all, img_all ,p_date_all ,url_all)

        # pass the zip  into the render file
    
        all = zip(news_all, desc_all,img_all,p_date_all,url_all)

    return render_template('home.html',contents = contents, all = all)


if __name__ == '__main__':
    app.run(debug=True)


