import unittest
from app.models import news


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = news(1234,"El Mundo",'Noticias, actualidad, álbumes, debates, sociedad, servicios, entretenimiento y última hora en España y el mundo.'/"http://www.elmundo.es",'general','es', 'es')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,news))

if __name__ == '__main__':
    unittest.main()