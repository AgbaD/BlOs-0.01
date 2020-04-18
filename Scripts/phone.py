#!/usr/bin/python
# Author:   @BlankGodd
# Home page

from pyfiglet import Figlet
import os, sys
import menu
from random import choice
# import settings


class Home:

    def __init__(self, iden):
        self.iden = iden
        banner = Figlet(font='standard')
        a = ['B','L','A','N','K']
        b = choice(a)
        print(banner.renderText(b))
        print("Enter one of the following commands")
        print("M for Menu")
        print("S for settings")
        print("H for Help")
        print("L to Logout")
        command = input(": ")

        if command == 'l' or command == 'L':
            print("Are you sure Y/N")
            c = input(": ")
            if c == 'y' or c == "Y":
                sys.exit()
            elif c == 'n' or c == 'N':
                self.__init__(self.iden)
            else:
                print("Invalid command")
                self.__init__(self.iden)
        elif command == 'h' or command == 'H':
            main_path = os.getcwd()
            os.chdir('..')
            sub_path = os.getcwd()
            os.chdir(main_path)
            help_file = os.path.join(sub_path, help.txt)
            with open(help_file, 'r') as f:
                h = f.read()
            print(h)
        elif command == 's' or command == 'S':
            settings.Settings(self.iden)
        elif command == 'm' or command == 'M':
            menu.Menu(self.iden)
        else:
            print("Command not recognised")
            self.__init__(self.iden)

