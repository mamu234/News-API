
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

    def __init__(self,sources,domains,from_param,to,language,sort_by):
        self.sources = sources
        self.domains = domains
        self.from_param = from_param
        self.to = to
        self.language = language
        self.sort_by = sort_by


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