import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,"independent","Met Gala 2022 - live: Nicki Minaj, Kim Kardashian and more hit the red carpet for Gilded Glamour theme - The Independent",
        "The Met Gala 2022 live stream and red carpet news","https://static.independent.co.uk/2022/05/02/23/newFile-1.jpg?quality=75&width=1200&auto=webp",
        "The 2022 Met Gala red carpet was full of gilded glamour as guests attended fashions most-anticipated event of the year. \r\nFrom Blake Lively to Kim Kardashian, the best-dressed stars of the Met Gala s… [+6426 chars]",
        "2022-05-03T06:36:26Z" )

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()            
