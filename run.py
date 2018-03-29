#!/usr/bin/env python3.6
from locker import User
from password import Password

def create_account(login,password):
    '''
    Function to create new account
    '''
    new_account=User(login,password)
    return new_account
