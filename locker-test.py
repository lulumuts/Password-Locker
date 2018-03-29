import unittest #Importing the unittest module
# from User import User #Importing the class locker
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
        self.new_account("lulumuts","VXg@!9") #create account

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list=[]

    def test_account_init(self):
        '''
        test_init test cases to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.Username,"lulumuts")
        self.assertEqual(self.new_account.Password,"VXg@!9")

if __name__ == '__main__':
    unittest.main()
