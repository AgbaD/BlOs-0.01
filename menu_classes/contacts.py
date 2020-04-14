#!/usr/bin/python
#contact class

from message import Message
import ast
import os


class Contacts:
    # when contact is instatiated, it takes with it a refrence to the
    # menu so as to be able to exit when needed

    def __init__(self, menu):
        print("Add Contact[A]")
        print("View Contacts[V]")
        print("Message contact[M]")
        print("Exit[e-x]")
        self.menu = menu
        self.main()

    def main(self):
        command = input("Enter your command\n")
        if command == 'e-x':
            self.exit()
        elif command == 'M' or command == 'm':
            self.cont_create_message()
        elif command == 'V' or command == 'v':
            self.view_contacts()
        elif command == 'A' or command == 'a':
            self.add_contact()
        else:
            print("Invalid command")
            self.main()
    
    def exit(self):
        self.menu.__init__()
        # i might have to remove the '.__init__' eventually though
        # if it works without it

    def cont_create_message(self):
        m = Message()
        m.create_message()
        print('CONTACTS')
        self.__init__()

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
            if cd == 'A' or cd == 'a':
                self.add_contact()
            else:
                self.__init__()
        else:
            with open(cont_file, 'r') as f:
                table = ast.literal_eval(f.read())
            for key, value in table.items():
                print(key':\t' value)
            command = input("Enter 'M' to message contact or any other key to go back\n")
            if command == 'M' or command == 'm':
                self.cont_create_message()
            else:
                self.__init__()

    def add_contact(self):
        print("At any point in the begining of an input, enter 'e-x' to exit to message menu")

        name = input("Enter contact's name\n")
        if name == 'e-x':
            self.__init__()

        id = input("Enter contact's id\n")
        if id == 'e-x':
            self.__init__()

        main_path = os.getcwd()
        os.chdir('..')
        sub_path = os.getcwd()
        os.chdir(main_path)
        contacts = 'db\\contacts.txt'
        cont_file = os.path.join(sub_path, contacts)
        if not os.path.exists(cont_file):
            table = {}
            table[name] == id
            with open(cont_file, 'w') as f:
                f.write(str(table))
        else:
            with open(cont_file, 'r') as f:
                table = ast.literal_eval(f.read())
            table[name] = id
            with open(cont_file, 'w') as f:
                f.write(str(table))
        os.chdir(main_path)
        self.view_contacts()
        self.__init__()
    

