#!/usr/bin/env python3.6
from locker import User
import sys
import random

import csv

# from password import Password

def create_account(username,password):
    '''
    Function to create new account
    '''
    new_account=User(username,password)
    return new_account

def save_accountx(username,password):
    '''
    Function to save account
    '''
    User.save_account(username,password)

def find_account_by_login(username):
    '''
    Function that finds a account by login
    '''
    return User.find_account_by_login(username)

def check_exisiting_contacts(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.account_exist(username)


def main():
    print("Welcome to Password locker! Do you have an account with us?")
    print('\n')

    #while True:
    if 1==1:
            print("Navigation: yes, no")

            short_code=input().lower()

            if short_code == 'no':

                    print("Create new account")
                    print("-"*10)

                    print("Choose your Username")
                    unx=input().strip(" ")

                    print("Type your password")
                    psx=input().strip(" ")

                    #save_account(create_account(username,password))#create and save new contact
                    ob = User()
                    ob.save_account(unx, psx, 1)

                    #print("testme",ob.username)
                    print('\n')
                    print(f"New Account created!")
                    print('\n')
                    print("please log in again to use our service")
                    short_code = 'yes'
                    #print("allusers:",ob.get_details())

            if short_code == 'yes':

                    print("Enter your log in details")
                    print("-"*10)

                    shyes = User()
                    #shyes.get_details()
                    print("Username")
                    username=input().strip(" ")

                    print("Password")
                    password=input().strip(" ")

                    paw = shyes.check_exist(username)

                    if paw == password:
                        print('\n')
                        print(f"Hello {username}. Lets get you started.")
                        print('\n')
                        print("Navigation: new - generate new password, exit-exit the service, view-view existing passwords")
                        nav_bar=input().lower().strip(" ")
                        if nav_bar == "new":
                            print("set your limit for your password")
                            newpw = shyes.randompw(username)
                            print("new password", newpw)
                        elif nav_bar == "exit":
                            print("Come back soon!")
                        elif nav_bar == "view":
                            shyes.returnpw(username)
                    elif paw == 'nonefound000':
                        print("user not found")
                    else:
                        print("Sorry {username}, that is the wrong password")



                    #print("allusers_:",ob.get_details())
                    #break

    #while True:





if __name__ == '__main__':
    main()
