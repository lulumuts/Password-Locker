import unittest #Importing the unittest module
from locker import User #Importing the class locker


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

    def test_save_account(self):
        '''
        test to see whether you account has been account_saved
        '''
        self.new_account.save_account() #saving the new account
        self.assertEqual(len(User.account_list),1)

    def test_find_account_by_login(self):
        '''
        test to check if we can find an account by login name
        '''

        self.new_account.save_account()
        test_account = User("lulumuts","VXg@!9")#new accounts
        test_account.save_account()

        found_account=User.find_account_by_login("VXg@!9")

        self.assertEqual(found_account.login,test_account.login)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list=[]



if __name__ == '__main__':
    unittest.main()
