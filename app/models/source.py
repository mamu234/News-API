class Source:

    all_sources = []

    def __init__(self,id,title,imageurl,name):
        self.news_id = id
        self.title = title
        self.imageurl = imageurl
        self.name= name


    def save_source(self):
        Source.all_sources.append(self)


    @classmethod
    def clear_sources(cls):
        Source.all_sources.clear()