#!/usr/bin/python
# Author:   @BlankGodd'

import ast
import os

    
def __init__(self):    
    print("Welcome to BlOs\n Login to continue")
    print("Enter L to login or S to signup")
    s = input(':')

    main_path = os.getcwd()
    os.chdir('..')
    sub_path = os.getcwd()
    os.chdir(main_path)
    acc = 'db\\accounts.txt'
    account_file = os.path.join(sub_path, acc)

    if s == 'l' or s == 'L':
        self.login()

def login(self):
    name = input("Username: ")
    password = input("Password: ")
    id = 0
    
    with open(account_file, 'r')as f:
        table = ast.literal_eval(f.read())
    
    names = [key for key in table.keys()] 
    cond = True
    while cond:
        if name in names:
            val = table[name]
            if val[0] == password:
                id = val[1]
                cond = False
            else:
                print('Incorrect password')
                # still to deal with forgot password
                password = input("Password: ")
        else:
            print('Username not recognised')
            print('To enter new username, type "E"\
            or type "S" to sign up. Type "e-x" to exit')
            c = input(":")
            if c == 'E' or c == 'e':
                name = input("Username: ")
                password = input("Password: ")
            elif c == 'e-x':

            else:
                cond = False
                self.signup()




