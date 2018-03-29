class Password:
    '''
    Class that generates new passwords.
    '''

    password_list = [] #Empty password list

    def __init__(self,random_password):

        self.random_password = random_password

    def save_password(self):
        '''
        save_password method saves password objects in password_list
        '''
        Password.password_list.append(self)
