class Password:
    '''
    Class that generates new passwords.
    '''

    password_list = [] #Empty password list
    password_length = []

    def __init__(self,random_password):

        self.random_password = random_password

    def save_password(self):
        '''
        save_password method saves password objects in password_list
        '''
        Password.password_list.append(self)

    def password_length(self):
        '''
        password_length method defines how many characters are permissible for
        '''

        for password in Password.password_length:
            if Password.password_length > 5:
                print("Please limit your password length to 5 characters")
