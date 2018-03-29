import unittest #Importing the unittest module
from locker import User #Importing the class locker
# from password import Password #Importing the class password

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account= User("lulumuts","VXg@!9") #create account



    def test_init(self):
        '''
        test_init test cases to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.username,"lulumuts")
        self.assertEqual(self.new_account.password,"VXg@!9")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list=[]

if __name__ == '__main__':
    unittest.main()
