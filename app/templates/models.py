class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,sources,category,langauge,country):
        self.sources = sources
        self.category = category
        self.langauge = langauge
        self.country = country



class Articles:

    all_articles = []

    def __init__(self,sources,domains,from_param,to,language,sort_by):
        self.sources = sources
        self.domains = domains
        self.from_param = from_param
        self.to = to
        self.language = language
        self.sort_by = sort_by


    def save_review(self):
        Articles.all_articles.append(self)


    @classmethod
    def clear_articles(cls):
        Articles.all_articles.clear()

    @classmethod
    def get_articles(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response