#!/usr/bin/python
# calculator class
# Author:   @BlankGodd

import math
import os

class Calculator:
    
    def __init(self, menu):
        self.menu = menu
        self.main()

    def main(self):
        self.command = input("Enter your command\n")
        for i in self.command:
            try int(i)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b
        
    def div(self, a, b):
        return a / b