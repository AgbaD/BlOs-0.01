#!/usr/bin/python
# Author:   @BlankGodd
# Phone classes

import os, time
import ast
from pyfiglet import Figlet
import sys
from random import choice


# Home
# Menu
# Messages
# Contacts
# Settings
# Calculator
# Games


class Home:

    def __init__(self, iden):
        self.iden = iden
        self.main()

    def main(self):
        banner = Figlet(font='standard')
        print("---------------------------------------------")
        print(banner.renderText('B'))
        print("---------------------------------------------")
        print()
        print("This is the home page")
        print("Enter one of the following commands")
        print("M for Menu")
        print("S for settings")
        print("H for Help")
        print("L to Logout")
        command = input(": ")
        print()
        print("---------------------------------------------")

        if command == 'l' or command == 'L':
            print("Are you sure Y/N")
            c = input(": ")
            if c == 'y' or c == "Y":
                print('Shuting down...')
                print("---------------------------------------------")
                time.sleep(3)
                sys.exit()
            elif c == 'n' or c == 'N':
                self.__init__(self.iden)
            else:
                print("Invalid command")
                print()
                print("---------------------------------------------")
                self.__init__(self.iden)
        elif command == 'h' or command == 'H':
            main_path = os.getcwd()
            os.chdir('..')
            sub_path = os.getcwd()
            os.chdir(main_path)
            help_file = os.path.join(sub_path, 'README.md')
            with open(help_file, 'r') as f:
                h = f.readlines()
            print("---------------------------------------------")
            print()
            for line in h:
                print(line)
                time.sleep(0.5)
            print("---------------------------------------------")
            self.__init__(self.iden)
        elif command == 's' or command == 'S':
            Settings(self.iden)
        elif command == 'm' or command == 'M':
            Menu(self.iden)
        else:
            print("Command not recognised")
            print("---------------------------------------------")
            self.__init__(self.iden)
    
    def f_logout(self):
        sys.exit()


class Menu:

    def __init__(self, iden):
        print("---------------------------------------------")
        print()
        print("Enter 'e-x' to exit at any point")
        print("'M' for Messages")
        print("'C' for Contacts")
        print("'Ca' for Calculator")
        print("'G' for Games")
        print("'S' for Settings")
        print("---------------------------------------------")
        self.iden = iden
        self.main()

    def main(self):
        c = input(': ')
        if c == 'e-x':
            Home(self.iden)
        elif c == 'm' or c == 'M':
            Message(self.iden)
        elif c == 'c' or c == 'C':
            Contacts(self.iden)
        elif c == 'ca' or self.c == 'Ca':
            Calculator(self.iden)
        elif c == 'g' or c == 'G':
            Games(self.iden)
        elif c == 's' or c == 'S':
            Settings(self.iden)
        else:
            print("Invalid command")
            print("---------------------------------------------")
            self.__init__(self.iden)


class Message:
    # when message is instatiated, it takes with it a refrence to the
    # menu so as to be able to exit when needed

    def __init__(self, iden):
        print("---------------------------------------------")
        print()
        print("Create message[C]")
        print("Inbox[I]")
        print("Drafts[D]")
        print("Outbox[O]")
        print("Sent[S]")
        print("Exit[e-x]")
        print("---------------------------------------------")
        self.iden = iden
        self.main()

    def main(self):
        command = input("Enter your command\n")
        if command == 'e-x':
            Menu(self.iden)
            return
        elif command == 'C' or command == 'c':
            self.create_message()
        elif command == 'I' or command == 'i':
            self.inbox()
        elif command == "D" or command == 'd':
            self.drafts()
        elif command == "O" or command == 'o':
            self.outbox()
        elif command == "S" or command == 's':
            self.sent()
        else:
            print("Invalid command")
            print("---------------------------------------------")
            self.main()

    def exit(self):
        self.menu()
        # i might have to remove the '.__init__' eventually though
        # if it works without it


    def create_message(self):
        print("At any point in the begining of an input, enter 'e-x' to\
        exit")

        print("---------------------------------------------")
        print()
        to = input("Enter contact name or id\n")
        if to == 'e-x':
            self.__init__(self.iden)

        print("---------------------------------------------")
        message = input("Enter your message. 'Enter' means you are done\n")
        if message == 'e-x':
            self.__init__(self.iden)

        print("---------------------------------------------")
        command = input("Enter 'send' to send, 'save' to save to drafts\
        'back' to go back\n")

        if command == "back" or command == 'e-x':
            self.__init__(self.iden)
        
        iden = ''
        if command == "send":
            # pick up iden

            # This is for the contact to keep being prompted as long as they
            # keep making a mistake unless they opt to exit
            cond = True
            while cond:
                if to == 'e-x':
                    self.__init__(self.iden)
                try:
                    # since all inputs are strings
                    if int(to):
                        iden = to
                        cond = False
                except:
                    main_path0 = os.getcwd()
                    os.chdir('..')
                    sub_path0 = os.getcwd()
                    os.chdir(main_path0)
                    contacts = 'db\\contacts.txt'
                    cont_file = os.path.join(sub_path0, contacts)
                    if not os.path.exists(cont_file):
                        print('Contacts Empty!! Enter valid Id')
                        to = input("Enter contact id\n")
                        print("---------------------------------------------")
                    else:
                        with open(cont_file, 'r') as cf:
                            ctab = ast.literal_eval(cf.read())
                        ctable = {}
                        try:
                            ctable = ctab[self.iden]
                        except:
                            print('Contacts Empty!! Enter valid Id')
                            to = input("Enter contact id\n")
                            print("---------------------------------------------")
                        clok = [key for key in ctable.keys()]   
                        # check for name in contacts.txt and get id
                        # if name in contacts; get id
                        if to in clok:
                            iden = ctable[to]
                            cond = False
                        else:
                            print("Name is not in contact list. Enter the proper\
                            name of enter id")
                            to = input("Enter contact name or id\n")
                            print("---------------------------------------------")

            # got to the inbox of id
            # go to inbox.txt and check for the id
            """Check if the id is on the server. The server is where all ID's
            are saved as a table key and the value is the objective instance of the 
            mobile phone instantiated with the id
            """
            # add message to inbox and create notification
            # once sending is done, return to self.__init__

        if command == 'save':
            main_path = os.getcwd()
            os.chdir('..')
            sub_path = os.getcwd()
            os.chdir(main_path)
            draft = 'db\\drafts.txt'
            draft_file = os.path.join(sub_path, draft)
            if not os.path.exists(draft_file):
                drafts = {}
                table = {}
                table[to] = message
                drafts[self.iden] = table
                with open(draft_file, 'w') as f:
                    f.write(str(drafts))
            else:
                with open(draft_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                a = table[self.iden]
                a[to] = message
                table[self.iden] = a
                with open(draft_file, 'w') as f:
                    f.write(str(table))
            os.chdir(main_path)
            self.__init__(self.iden)
            # save to drafts file
            # need to work on repeated savings to same name or id
            # repeated inboxes to
            # should be dealt with by using the time factor
        
        # An idea is to create unique ids for each phone so messages 
        # can be sent between local phones
    
    def inbox(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        main_path = os.getcwd()
        os.chdir('..')
        # since this script will be in a seperate folder from the db folder
        sub_path = os.getcwd()
        os.chdir(main_path)
        box = 'db\\inbox.txt'
        inbox_file = os.path.join(sub_path, box)
        if not os.path.exists(inbox_file):
            print('Inbox Empty!!')
            print()
            print("---------------------------------------------")
            self.__init__(self.iden)
        else:
            with open(inbox_file, 'r') as f:
                inboxes = ast.literal_eval(f.read())
            table = {}
            try:
                table = inboxes[self.iden]
            except:
                print("Inbox Empty!")
                return
            lok = []
            for key, value in table.items():
                print(key)
                lok.append(key)
            
            print("---------------------------------------------")
            print()
            command = input('Enter name or id to view message\n')
            # id would be numbers but as a string like such; '342'
            if command == 'e-x':
                self.__init__(self.iden)
            if command in lok:
                print("---------------------------------------------")
                print(table[command])
                print("---------------------------------------------")
                time.sleep(3)
                cd = input('Ready to exit?: ')
                if cd == 'e-x':
                    self.__init__(self.iden)
                else:
                    self.inbox()
            else:
                print('No message from {0}'.format(command))
                self.inbox()

    def drafts(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        draft = 'db\\drafts.txt'
        draft_file = os.path.join(sub_path, draft)
        if not os.path.exists(draft_file):
            print('Draft Empty!!')
            print("---------------------------------------------")
            self.__init__(self.iden)
        else:
            with open(draft_file, 'r') as f:
                drafts = ast.literal_eval(f.read())
            table = {}
            try:
                table = drafts[self.iden]
            except:
                print("Draft Empty!")
                print("---------------------------------------------")
                return
            lok = []
            # to keep track of message name or id
            for key, value in table.items():
                print(key)
                lok.append(key)
            
            command = input('Enter name or id to view message\n')
            # id would be numbers but as a string like such; '342'
            if command == 'e-x':
                self.__init__(self.iden)
            if command in lok:
                print("---------------------------------------------")
                print()
                print(table[command])
                print("---------------------------------------------")
                time.sleep(3)
                cd = input('Ready to exit?: ')
                if cd == 'e-x':
                    self.__init__(self.iden)
                else:
                    self.drafts()
            else:
                print('No message to {0}'.format(command))
                self.drafts()

    def outbox(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        obox = 'db\\outbox.txt'
        outbox_file = os.path.join(sub_path, obox)
        if not os.path.exists(outbox_file):
            print('Outbox Empty!!')
            print("---------------------------------------------")
            self.__init__(self.iden)
        else:
            with open(outbox_file, 'r') as f:
                outboxes = ast.literal_eval(f.read())
            table = {}
            try:
                table = outboxes[self.iden]
            except:
                print("Outbox Empty!")
                print("---------------------------------------------")
                return
            lok = []
            # to keep track of message name or id
            for key, value in table.items():
                print(key)
                lok.append(key)
            
            command = input('Enter name or id to view message\n')
            # id would be numbers but as a string like such; '342'
            if command == 'e-x':
                self.__init__(self.iden)
            if command in lok:
                print("---------------------------------------------")
                print()
                print(table[command])
                print("---------------------------------------------")
                time.sleep(3)
                cd = input('Ready to exit?: ')
                if cd == 'e-x':
                    self.__init__(self.iden)
                else:
                    self.outbox()
            else:
                print('No message to {0}'.format(command))
                self.outbox()
            
    def sent(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        sbox = 'db\\sent.txt'
        sent_file = os.path.join(sub_path, sbox)
        if not os.path.exists(sent_file):
            print('Sent Empty!!')
            print("---------------------------------------------")
            self.__init__(self.iden)
        else:
            with open(sent_file, 'r') as f:
                sents = ast.literal_eval(f.read())
            table = {}
            try:
                table = sents[self.iden]
            except:
                print("Sent Empty!")
                print("---------------------------------------------")
                return
            lok = []
            # to keep track of message name or id
            for key, value in table.items():
                print(key)
                lok.append(key)
            
            command = input('Enter name or id to view message\n')
            # id would be numbers but as a string like such; '342'
            if command == 'e-x':
                self.__init__(self.iden)
            if command in lok:
                print("---------------------------------------------")
                print()
                print(table[command])
                print("---------------------------------------------")
                time.sleep(3)
                cd = input('Ready to exit?: ')
                if cd == 'e-x':
                    self.__init__(self.iden)
                else:
                    self.sent()
            else:
                print('No message to {0}'.format(command))
                self.sent()


class Contacts:
    # when contact is instatiated, it takes with it a refrence to the
    # menu so as to be able to exit when needed

    def __init__(self, iden):
        print("---------------------------------------------")
        print()
        print("Add Contact[A]")
        print("View Contacts[V]")
        print("Message contact[M]")
        print("Exit[e-x]")
        print("---------------------------------------------")
        # self.menu = menu
        self.iden = iden
        self.main()

    def main(self):
        command = input("Enter your command\n")
        if command == 'e-x':
            Menu(self.iden)
        elif command == 'M' or command == 'm':
            self.cont_create_message()
        elif command == 'V' or command == 'v':
            self.view_contacts()
        elif command == 'A' or command == 'a':
            self.add_contact()
        else:
            print("Invalid command")
            print("---------------------------------------------")
            self.main()
    
    def exit(self):
        self.menu()
        # i might have to remove the '.__init__' eventually though
        # if it works without it

    def cont_create_message(self):
        m = Message(self.iden)
        m.create_message()
        print("---------------------------------------------")
        print('CONTACTS')
        self.__init__(self.iden)

    def view_contacts(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        contacts = 'db\\contacts.txt'
        cont_file = os.path.join(sub_path, contacts)
        if not os.path.exists(cont_file):
            print("Contacts Empty")
            cd = input("Enter 'A' to add contacts or any other key to go back\n")
            print("---------------------------------------------")
            if cd == 'A' or cd == 'a':
                self.add_contact()
            else:
                self.__init__(self.iden)
        else:
            with open(cont_file, 'r') as f:
                contactts = ast.literal_eval(f.read())
            table = {}
            try :
                table = contactts[self.iden]
            except:
                print("Contacts Empty")
                print("---------------------------------------------")
                return
            for key, value in table.items():
                print(key, ':\t', value)
            command = input("Enter 'M' to message contact or any other key to go back\n")
            if command == 'M' or command == 'm':
                self.cont_create_message()
            else:
                self.__init__(self.iden)

    def add_contact(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        print("---------------------------------------------")
        print()
        name = input("Enter contact's name\n")
        if name == 'e-x':
            self.__init__(self.iden)

        iden = input("Enter contact's id\n")
        print("---------------------------------------------")
        if iden == 'e-x':
            self.__init__(self.iden)

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        contacts = 'db\\contacts.txt'
        cont_file = os.path.join(sub_path, contacts)
        if not os.path.exists(cont_file):
            contactts = {}
            table = {}
            table[name] = iden
            contactts[self.iden] = table
            with open(cont_file, 'w') as f:
                f.write(str(contactts))
        else:
            with open(cont_file, 'r') as f:
                table = ast.literal_eval(f.read())
            x =table[self.iden]
            x[name] = iden
            # to deal with multiple contacts with same names
            table[self.iden] = x
            with open(cont_file, 'w') as f:
                f.write(str(table))
        os.chdir(main_path)
        self.view_contacts()
        self.__init__(self.iden)
    

class Settings:

    def __init__(self, iden):
        self.iden = iden

    def logout(self):
        print("---------------------------------------------")
        print()
        print("Are you sure Y/N")
        c = input(": ")
        if c == 'y' or c == "Y":
            sys.exit()
        elif c == 'n' or c == 'N':
            self.__init__(self.iden)
        else:
            print("Invalid command")
            print("---------------------------------------------")
            self.__init__(self.iden)
        

class Calculator:

    def __init__(self, iden):
        self.iden = iden


class Games:
    
    def __init__(self, iden):
        self.iden = iden


