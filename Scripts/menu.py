#!/usr/bin/python
# Author:   @BlankGodd

from phone import Home
import message
import contacts
import calculator
# import games
# import settings


class Menu():

    def __init__(self, iden):
        print("Enter 'e-x' to exit at any point")
        print("'M' for Messages")
        print("'C' for Contacts")
        print("'Ca' for Calculator")
        print("'G' for Games")
        print("'S' for Settings")
        self.c = input(': ')
        self.iden = iden

    def main(self):
        if self.c == 'e-x':
            Home(self.iden)
            return
        elif self.c == 'm' or self.c == 'M':
            message.Message(self.iden)
        elif self.c == 'c' or self.c == 'C':
            contacts.Contacts(self.iden)
        elif self.c == 'ca' or self.c == 'Ca':
            calculator.Calculator(self.iden)
        elif self.c == 'g' or self.c == 'G':
            games.Games(self.iden)
        elif self.c == 's' or self.c == 'S':
            settings.Settings(self.iden)
        else:
            print("Invalid command")
            self.__init__(self.iden)