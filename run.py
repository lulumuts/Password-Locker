#!/usr/bin/env python3.6
from locker import User
# from password import Password

def create_account(login,password):
    '''
    Function to create new account
    '''
    new_account=User(login,password)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()

def find_account_by_login(login):
    '''
    Function that finds a account by login
    '''
    return User.find_account_by_login(login)

def check_exisiting_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)


def main():
    print("Welcome to Password locker! Do you have an account with us?")
    print('\n')

    print("y/n")
    while True:
            print("Navigation: yes, no)
            reponse=input()

            short_code == 'yes':
                print("Enter your log in details")

                search_login=input()
                if



    print(f"Hello {login}. Lets get you started.")
    print('\n')

    while True:
            print("Navigation: new - generate new password, exit-exit the service")

            short_code=input().lower()
            if short_code == 'new':
                    print("set your limit for your password")

            elif short_code == "exit":
                    print("Come back soon!")
                    break

            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
