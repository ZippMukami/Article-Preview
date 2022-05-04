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
        self.new_bulletin = Bulletin(1234,"Federal Reserve issues FOMC statement - Federal Reserve", "Although overall economic activity edged down in the first quarter, household spending and business fixed investment remained strong. Job gains have been robus","","Although overall economic activity edged down in the first quarter, household spending and business fixed investment remained strong. Job gains have been robust in recent months, and the unemployment… [+2268 chars]","2022-05-04T18:08:44Z")

        def test_instance(self):
            self.asserTrue(isinstance(self.new_bulletin, Bulletin))


if __name__ == '__main__':
    unittest.main()            