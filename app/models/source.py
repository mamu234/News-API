class Source:
    '''
    News class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,language, country,poster):
        self.id =id
        self.name = name
        self.description = description
        self.url =  url
        self.category = category
        self.language = language
        self.country = country
        self.poster = poster 
    