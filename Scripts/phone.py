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
        command = input(": ").lower()
        print()
        print("---------------------------------------------")

        if command == 'l':
            print("Are you sure Y/N")
            c = input(": ").lower()
            if c == 'y':
                print('Shuting down...')
                print()
                print("---------------------------------------------")
                time.sleep(3)
                sys.exit()
            elif c == 'n':
                self.__init__(self.iden)
            else:
                print("Invalid command")
                print()
                print("---------------------------------------------")
                self.__init__(self.iden)
        elif command == 'h':
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
        elif command == 's':
            Settings(self.iden)
        elif command == 'm':
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
        c = input(': ').lower()
        if c == 'e-x':
            Home(self.iden)
        elif c == 'm':
            Message(self.iden)
        elif c == 'c':
            Contacts(self.iden)
        elif c == 'ca':
            Calculator(self.iden)
        elif c == 'g':
            Games(self.iden)
        elif c == 's':
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
        command = input("Enter your command\n").lower()
        if command == 'e-x':
            Menu(self.iden)
            return
        elif command == 'c':
            self.create_message()
        elif command == 'i':
            self.inbox()
        elif command == 'd':
            self.drafts()
        elif command == 'o':
            self.outbox()
        elif command == 's':
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
        'back' to go back\n").lower()

        if command == "back" or command == 'e-x':
            self.__init__(self.iden)
        
        if command == "send":
            iden = ''
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

            # check if id is on the server
            main_path1 = os.getcwd()
            os.chdir('..')
            sub_path1 = os.getcwd()
            os.chdir(main_path1)
            server = 'db\\server.txt'
            inboxx = 'db\\inbox.txt'
            outbox = 'db\\outbox.txt'
            sent = 'de\\sent.txt'
            inboxx_file = os.path.join(sub_path1, inboxx)
            server_file = os.path.join(sub_path1, server)
            outbox_file = os.path.join(sub_path1, outbox)
            sent_file = os.path.join(sub_path1, sent)

            with open(server_file, 'r')as f:
                lst = ast.literal_eval(f.read())
            cond = False
            while not cond:
                if iden in lst:
                    cond = True
                else:
                    print("ID input does not exist. Input new ID")
                    print("Enter e-x to exit")
                    comm = input(": ")
                    try:
                        if int(comm):
                            idea = comm
                    except:
                        print("Saving to outbox")
                        cond = True
                        if not os.path.exists(outbox_file):
                            outboxx = {}
                            table = {}
                            table[iden] = message
                            outboxx[self.iden] = table
                            # add message to outbox
                            with open(outbox_file, 'w') as f:
                                f.write(str(outboxx))
                        else:
                            with open(outbox_file, 'r') as f:
                                table = ast.literal_eval(f.read())
                            try:    
                                a = table[self.iden]
                                a[iden] = message
                                table[self.iden] = a
                            except:
                                a = {}
                                a[iden] = message
                                table[self.iden] = a
                            with open(outbox_file, 'w') as f:
                                f.write(str(table))
                        os.chdir(main_path1)
                        self.__init__(self.iden)

            # go to inbox.txt and check for the id

            if not os.path.exists(inboxx_file):
                inbox = {}
                table = {}
                table[self.iden] = message
                inbox[iden] = table
                # add message to inbox and create notification
                with open(inboxx_file, 'w') as f:
                    f.write(str(inbox))
            else:
                with open(inboxx_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                try:    
                    a = table[iden]
                    a[self.iden] = message
                    table[iden] = a
                except:
                    a = {}
                    a[self.iden] = message
                    table[iden] = a
                with open(inboxx_file, 'w') as f:
                    f.write(str(table))
            os.chdir(main_path1)
            if not os.path.exists(sent_file):
                sentt = {}
                table = {}
                table[iden] = message
                sentt[self.iden] = table
                # add message to sent
                with open(sent_file, 'w') as f:
                    f.write(str(sentt))
            else:
                with open(sent_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                try:    
                    a = table[self.iden]
                    a[iden] = message
                    table[self.iden] = a
                except:
                    a = {}
                    a[iden] = message
                    table[self.iden] = a
                with open(sent_file, 'w') as f:
                    f.write(str(table))
                        
            self.__init__(self.iden)
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
                try:    
                    a = table[self.iden]
                    a[to] = message
                    table[self.iden] = a
                except:
                    a = {}
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
                cd = input('Enter R to reply or any other key to exit: ').lower()
                if cd == 'e-x':
                    self.__init__(self.iden)
                elif cd == 'r':
                    self.create_message()
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
        command = input("Enter your command\n").lower()
        if command == 'e-x':
            Menu(self.iden)
        elif command == 'm':
            self.cont_create_message()
        elif command == 'v':
            self.view_contacts()
        elif command == 'a':
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
            cd = input("Enter 'A' to add contacts or any other key to go back\n").lower()
            print("---------------------------------------------")
            if cd == 'a':
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
            command = input("Enter 'M' to message contact or any other key to go back\n").lower()
            if command == 'm':
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
            try:
                x =table[self.iden]
                x[name] = iden
                # to deal with multiple contacts with same names
                table[self.iden] = x
            except:
                x = {}
                x[name] = iden
                table[self.iden] = x
            with open(cont_file, 'w') as f:
                f.write(str(table))
        os.chdir(main_path)
        self.view_contacts()
        self.__init__(self.iden)
    

class Settings:

    def __init__(self, iden):
        self.iden = iden
        print("---------------------------------------------")
        print()
        print("Enter G to get ID")
        print("Enter CM to clear messages")
        print("Enter L to logout")
        print("Enter CC to clear contacts")
        print("Enter D to delete account")
        print()
        self.main()

    def main(self):
        command = input(": ").lower()
        if command == 'e-x':
            Menu(self.iden)
        elif command == 'g':
            self.get_id()
        elif command == 'cm':
            self.clear_messages()
        elif command == 'l':
            self.logout()
        elif command == 'cc':
            self.clear_contacts()
        elif command == 'd':
            self.del_account()
        else:
            print("Invalid Entry")
            self.__init__(self.iden)


    def get_id(self):
        print("---------------------------------------------")
        print(self.iden)
        self.__init__(self.iden)

    def clear_messages(self):
        print("---------------------------------------------")
        print()
        a = {'Inbox': "I", 'Outbox':'O', "Sent": 'S', "Drafts": 'D'}
        for k, v in a.items():
            print(k,':',v)
        b ={'i':'db\\inbox.txt','o':'db\\outbox.txt','s':'db\\sent.txt','d':'db\\drafts.txt'}
        print()
        bo = input("Enter which box to clear e.g 'I' for Inbox: \n").lower()
        kks = [i for i in b.keys()]
        if bo not in kks:
            self.__init__(self.iden)
        print()
        cd = input("Are you sure you want to delete all messages y/n \n").lower()
        if cd == 'n' or cd == 'e-x':
            self.__init__(self.iden)
        elif cd == 'y':
            main_path = os.getcwd()
            os.chdir('..')
            sub_path = os.getcwd()
            os.chdir(main_path)
            dbox = b[bo]
            del_file = os.path.join(sub_path, dbox)
            if not os.path.exists(del_file):
                print()
                print('Box Empty!!')
                print("---------------------------------------------")
                self.__init__(self.iden)
            else:
                with open(del_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                try:
                    my = table[self.iden]
                    dell = table.pop(self.iden)
                except:
                    print()
                    print("Box Empty!")
                    print("---------------------------------------------")
            self.__init__(self.iden)
        else:
            print()
            print("Invalid command!")
            print()
            print("---------------------------------------------")
            self.__init__(Self.iden)

    def logout(self):
        print("---------------------------------------------")
        print()
        print("Are you sure Y/N")
        c = input(": ").lower()
        if c == 'y':
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()
        elif c == 'n':
            self.__init__(self.iden)
        else:
            print("Invalid command")
            print("---------------------------------------------")
            self.__init__(self.iden)

    def clear_contacts(self):
        print("---------------------------------------------")
        print()
        cd = input("Are you sure you want to delete all contacts y/n \n").lower()
        if cd == 'n' or cd == 'e-x':
            self.__init__(self.iden)
        elif cd == 'y':
            main_path = os.getcwd()
            os.chdir('..')
            sub_path = os.getcwd()
            os.chdir(main_path)
            cbox = 'db\\contacts.txt'
            del_file = os.path.join(sub_path, cbox)
            if not os.path.exists(del_file):
                print()
                print('Box Empty!!')
                print("---------------------------------------------")
                self.__init__(self.iden)
            else:
                with open(del_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                try:
                    my = table[self.iden]
                    dell = table.pop(self.iden)
                except:
                    print()
                    print("Contacts Empty!")
                    print("---------------------------------------------")
            self.__init__(self.iden)
        else:
            print()
            print("Invalid command!")
            print()
            print("---------------------------------------------")
            self.__init__(Self.iden)
        
    def del_account(self):
        print("WARNING!!! Account will be deleted permanently!")
        print("Proceed with caution!")
        c = input("Delete Account y/n \n").lower()
        if c == 'y':
            # check contacts, messages
            # check server and accounts
            main_path = os.getcwd()
            os.chdir('..')
            sub_path = os.getcwd()
            os.chdir(main_path)
            contacts = 'db\\contacts.txt'
            inbox = 'db\\inbox.txt'
            drafts = 'db\\drafts.txt'
            sent = 'db\\sent.txt'
            outbox = 'db\\outbox.txt'
            server = 'db\\server.txt'
            accounts = 'db\\accounts.txt'
            contacts_file = os.path.join(sub_path, contacts)
            draft_file = os.path.join(sub_path, drafts)
            inbox_file = os.path.join(sub_path, inbox)
            sent_file = os.path.join(sub_path, sent)
            outbox_file = os.path.join(sub_path, outbox)
            server_file = os.path.join(sub_path, server)
            account_file = os.path.join(sub_path, accounts)

            if os.path.exists(contacts_file):
                with open(contacts_file, 'r') as c:
                    table = ast.literal_eval(c.read())
                try:
                    dell = table.pop(self.iden)
                except:
                    pass
                with open(contacts_file, 'w') as c:
                    if table != {}:
                        c.write(str(table))
                    else:
                        os.remove(contacts_file)

            if os.path.exists(draft_file):
                with open(draft_file, 'r') as c:
                    table = ast.literal_eval(c.read())
                try:
                    dell = table.pop(self.iden)
                except:
                    pass
                with open(draft_file, 'w') as c:
                    if table != {}:
                        c.write(str(table))
                    else:
                        os.remove(draft_file)
            
            if os.path.exists(inbox_file):
                with open(inbox_file, 'r') as c:
                    table = ast.literal_eval(c.read())
                try:
                    dell = table.pop(self.iden)
                except:
                    pass
                with open(inbox_file, 'w') as c:
                    if table != {}:
                        c.write(str(table))
                    else:
                        os.remove(inbox_file)

            if os.path.exists(sent_file):
                with open(sent_file, 'r') as c:
                    table = ast.literal_eval(c.read())
                try:
                    dell = table.pop(self.iden)
                except:
                    pass
                with open(sent_file, 'w') as c:
                    if table != {}:
                        c.write(str(table))
                    else:
                        os.remove(sent_file)
            
            if os.path.exists(outbox_file):
                with open(outbox_file, 'r') as c:
                    table = ast.literal_eval(c.read())
                try:
                    dell = table.pop(self.iden)
                except:
                    pass
                with open(outbox_file, 'w') as c:
                    if table != {}:
                        c.write(str(table))
                    else:
                        os.remove(outbox_file)

            if os.path.exists(server_file):
                with open(server_file, 'r') as f:
                    lst = ast.literal_eval(f.read())
                lst.remove(self.iden)
                with open(server_file, 'w') as f:
                    if lst != []:    
                        f.write(str(lst))
                    else:
                        os.remove(server_file)
                        open(server_file, 'x')

            if os.path.exists(account_file):
                with open(account_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                a = {}
                for k, v in table.items():
                    a[v[1]] = k
                for k, v in a.items():
                    if k == self.iden:
                        dell = table.pop(v)
                        break
                with open(account_file, 'w') as f:
                    if table != {}:
                        f.write(str(table))
                    else:
                        os.remove(account_file)
                        open(account_file, 'x')
                        
            print('Shuting down...')
            print()
            print("---------------------------------------------")
            time.sleep(3)
            sys.exit()
        else:
            self.__init__(self.iden)
                    


class Calculator:

    def __init__(self, iden):
        self.iden = iden
        print("---------------------------------------------")
        print("Please select the type of operation you would like to perform!")
        print("Enter 'e-x' at any point to exit")
        print()

        operations = {'Addition': 'A','Division': 'D','Exponent': 'E',
        'Multiplication': 'M','Modulus': 'Mod','Subtraction': 'S',}

        for k, v in operations.items():
            print(k,':',v)

        print()
        print("---------------------------------------------")
        print()
        self.calc()

    def calc(self):
        print("Input operation type letter e.g 'M' for multiplication")
        operation = input(': ').upper()
        if operation == 'e-x':
            Menu(self.iden)
        number1= int(input('First Number: '))
        if number1 == 'e-x':
            Menu(self.iden)
        number2 = int(input('Second Number: '))
        if number2 == 'e-x':
            Menu(self.iden)

        print()
        print("---------------------------------------------")
        print()
        
        if operation == 'M':
            print('{0} * {1} =   '.format(number1, number2),number1 * number2)
        elif operation == 'D':
            print('{0} / {1} =   '.format(number1, number2),number1 / number2)
        elif operation == 'A':
            print('{0} + {1} =   '.format(number1, number2),number1 + number2)
        elif operation == 'E':
            print('{0} exp {1} =   '.format(number1, number2),number1 ** number2)
        elif operation == 'MOD':
            print('{0} mod {1} =   '.format(number1, number2),number1 % number2)
        elif operation == 'S':
            print('{0} - {1} =   '.format(number1, number2),number1 - number2)
        else:
            print("Invalid operation!")
            self.__init__(self.iden)
            
        print()
        print("---------------------------------------------")
        self.__init__(self.iden)


class Games:
    
    def __init__(self, iden):
        self.iden = iden


