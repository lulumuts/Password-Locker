import unittest #Importing the unittest module
from password import Password #Importing the class password

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_password= Password("LMT936!") #generate new password


    def test_init(self):
        '''
        Set up method to run before each test cases.
        '''

        self.assertEqual(self.new_password.random_password,"LMT936!")


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Password.password_list=[]





if __name__ == '__main__':
    unittest.main()
