
from itertools import count


class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,sources,category,langauge,country):
        self.sources = sources
        self.category = category
        self.langauge = langauge
        self.country = country



class Sources:

    all_sources = []

    def __init__(self,id,name,description,language,poster,category,country):
        self.id = id
        self.name = name 
        self.description = description
        self.poster = poster
        self.category = category
        self.language = language
        self.country = country
    
           


    def save_source(self):
        Sources.all_sources.append(self)


    @classmethod
    def clear_sources(cls):
        Sources.all_sources.clear()

    @classmethod
    def get_sources(cls,id):

        response = []

        for source in cls.all_sources:
            if source.news_id == id:
                response.append(source)

        return response