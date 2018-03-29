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
