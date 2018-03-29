class User:
    """
    Class that generate new accounts using a login and password.
    """

    account_list = [] #Empty account list

    def __init__(self,username,password):

        self.username = username
        self.password = password


class Password:
    """
    Class that generates new passwords.

    password_list = []
    """
