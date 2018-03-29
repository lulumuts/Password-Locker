class User:
    """
    Class that generate new accounts using a login and password.
    """

    account_list = [] #Empty account list

    def __init__(self,username,password):

        self.username = username
        self.password = password


    def save_account(self):
        '''
        save_account method saves the account objects in account_list
        '''

        User.account_list.append(self)

    def find_account_by_login(self):
        '''
        Method that takes in the password in the form of a number and returns account
        details

        Args:
         login: name to search before
        Returns:
         Account of person that matches the name.
        '''
        for user in cls.account_list:
            if contact.login == login:
                return login

    
