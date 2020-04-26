#!/usr/bin/python
# Author:   @BlankGodd'

import ast
import os, sys
import time
import random
from pyfiglet import Figlet
from phone import Home


class Start:

    def __init__(self):
        banner = Figlet(font='standard')
        print(banner.renderText("Blank Os - 0.01"))

        self.start()

    def start(self):
        starting = 'Starting:[                    ]'
        for i in range(103):
            time.sleep(0.05)
            if i < 101:
                sys.stdout.write('\r' + starting + '{0}%'.format(i))
            else:
                sys.stdout.write('\r' + starting + '100%')
            if i==10 or i==20 or i==30 or i==40 or i==50 or i==60 or i==70 or \
            i==80 or i==90 or i==100:
                starting = starting.replace('  ','::',1)
            sys.stdout.flush()


class Entry:

    def __init__(self):   
        print()
        print() 
        print("---------------------------------------------")
        print()
        print("Welcome to Blank Os")
        print("Enter L to login or S to signup")
        print("Enter 'e-x' at any input point to exit")
        print()
        print("---------------------------------------------")
        print()
        s = input(':')
        if s == 'e-x':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        acc = 'db\\accounts.txt'
        ser = 'db\\server.txt'
        self.account_file = os.path.join(sub_path, acc)
        self.server_file = os.path.join(sub_path, ser)

        if s == 'l' or s == 'L':
            self.login()
        elif s == 's' or s == 'S':
            self.signup()
        else:
            print("Invalid Entry")
            self.__init__()

    def login(self):
        print("---------------------------------------------")
        print()
        print("Enter login details")
        name = input("Username: ")
        if name == 'e-x':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()

        password = input("Password: ")
        print()
        print("---------------------------------------------")
        if password == 'e-x':
            print('Shuting down...')
            time.sleep(3)
            sys.exit()

        iden = ''

        try:
            with open(self.account_file, 'r')as f:
                table = ast.literal_eval(f.read())
        except:
            print("Login Error!!!")
            print()
            print("---------------------------------------------")
            time.sleep(1)
            print()
            self.__init__()
    
        names = [key for key in table.keys()] 
        cond = True
        while cond:
            if name in names:
                # val 0 is password
                # val 1 is iden
                # val 2 is security question
                # val 3 is answer
                val = table[name]
                if val[0] == password:
                    iden = val[1]
                    cond = False
                else:
                    print()
                    print('Incorrect password')
                    print()
                    print("---------------------------------------------")
                    # still to deal with forgot password
                    name = input("Username: ")
                    if name == 'e-x':
                        print('Shuting down...')
                        print("---------------------------------------------")
                        time.sleep(3)
                        sys.exit()
                    password = input("Password: ")
                    print()
                    print("---------------------------------------------")
                    if password == 'e-x':
                        print('Shuting down...')
                        print()
                        print("---------------------------------------------")
                        time.sleep(3)
                        sys.exit()
            else:
                print()
                print("---------------------------------------------")
                print('Username not recognised')
                print('To enter new username, type "E"')
                print('type "S" to sign up. Type "e-x" to exit')
                c = input(":")
                print()
                print("---------------------------------------------")
                if c == 'E' or c == 'e':
                    name = input("Username: ")
                    if name == 'e-x':
                        print()
                        print('Shuting down...')
                        print()
                        print("---------------------------------------------")
                        time.sleep(3)
                        sys.exit()
                    password = input("Password: ")
                    print()
                    print("---------------------------------------------")
                    if password == 'e-x':
                        print('Shuting down...')
                        print()
                        print("---------------------------------------------")
                        time.sleep(3)
                        sys.exit()
                elif c == 's' or c == 'S':
                    cond = False
                    self.signup()
                else:
                    cond = False
                    print('Shuting down...')
                    print()
                    print("---------------------------------------------")
                    time.sleep(3)
                    sys.exit()

        if iden == '':
            pass
        else:
            Home(iden)
    
    def signup(self):
        print()
        print("---------------------------------------------")
        print()
        name = input("Username: ")
        if name == 'e-x':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()

        password = input('Password: ')
        print()
        print("---------------------------------------------")
        if password == 'e-x':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()
        print()
        print("Enter security question and answer")
        que = input("Question: ")
        if que == 'e-x':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()
        
        ans = input("Answer: ")
        print()
        print("---------------------------------------------")
        print()
        if ans == 'e-x':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()

        if os.path.exists(self.account_file):

            cond1 = True
            while cond1:  
                try:
                    with open(self.account_file, 'r')as f:
                        table = ast.literal_eval(f.read())
                    names = [key for key in table.keys()]
                except:
                    table = {}
                    names = []
                if name in names:
                    print("---------------------------------------------")
                    print()
                    print("Username already taken!")
                    print("Input new username")
                    name = input("Username: ")
                    print()
                    print("---------------------------------------------")
                    if name == 'e-x':
                        print('Shuting down...')
                        print()
                        print("---------------------------------------------")
                        time.sleep(3)
                        sys.exit()
                else:
                    # generate id first
                    a = ['0','1','2','3','4','5','6','7','8','9']
                    iden = ''
                    for i in range(3):
                        iden += random.choice(a)
                    print()
                    print("Your phone ID is: {0}".format(iden))
                
                    # save details to accounts.txt
                    table[name] = [password, iden, que, ans]
                    with open(self.account_file, 'w') as f:
                        f.write(str(table))
                    cond1 = False

                    # add id to server list
                    lst = []
                    try:
                        with open(self.server_file, 'r') as f:
                            lst = ast.literal_eval(f.read())
                    except:
                        pass
                    lst.append(iden)
                    with open(self.server_file, 'w') as f:
                        f.write(str(lst))

                    self.login()


