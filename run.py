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
                    unx=input()

                    print("Type your password")
                    psx=input()

                    #save_account(create_account(username,password))#create and save new contact
                    ob = User()
                    ob.save_account(unx, psx)

                    print("testme",ob.username)
                    print('\n')
                    print(f"New Account created!")
                    print('\n')

            elif short_code == 'yes':
                    print("Enter your log in details")
                    print("-"*10)

                    print("Username")
                    username=input()

                    print("Password")
                    password=input()

                    print('\n')
                    print(f"Hello {username}. Lets get you started.")
                    print('\n')
                    #break

    #while True:
            print("Navigation: new - generate new password, exit-exit the service")

            nav_bar=input().lower()

            if nav_bar == "new":
                    print("set your limit for your password")

                    mynum = []
                    inp = int(input("Enter your pw length: "))

                    allstr = 'A1bc23'

                    print("length of allstr = ", len(allstr))
                    print("range of inp")
                    print(range(inp))
                    print("start for loop")

                    for i in range(inp):
                        print("i", i)
                        thisnum = int(random.randint(0,len(allstr)))
                        print("thisnum", thisnum)
                        mynum.append(thisnum)
                        print("mynum",mynum)

                    print("end for loop")
                    print("final mynum object is...", mynum)


                    #allstr[mynum]
                    pasw = ''
                    print("this is pasw", pasw)

                    for x in mynum:
                        pasw = str(pasw) + str(allstr[x])

                    print("pasw", pasw)




            elif nav_bar == "exit":
                    print("Come back soon!")
                    #break

            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
