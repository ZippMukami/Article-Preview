import unittest
from models import bulletin
Bulletin = bulletin.Bulletin

class BulletinTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Bulletin class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_bulletin = Bulletin(1234)

        def test_instance(self):
            self.asserTrue(isinstance(self.new_bulletin, Bulletin))


if __name__ == '__main__':
    unittest.main()            