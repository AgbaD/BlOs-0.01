#!/usr/bin/python
# calculator class
# Author:   @BlankGodd

import math
import os
from menu import Menu

class Calculator(Menu):
    
    def __init(self, iden):
        # self.menu = menu
        self.iedn = iden
        self.main()

    def main(self):
        self.command = input("Enter your command\n")
        for i in self.command:
            pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b
        
    def div(self, a, b):
        return a / b