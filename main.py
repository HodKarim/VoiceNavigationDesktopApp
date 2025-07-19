#iterable - an object/collection that can b iterated thru a loop
import time
#lists [], tuples (), sets {} are all iterable
#strings are also iterable
#dictionaries are iteranbe

#membership operators (in or not in) (string, list, tuple, set, dict)

#list comprehension in python = concise way to create lists
#for every value in an interable check if works

#formula = expression for value in iterable if condition <- optiona;

#matchcase statements or switch: execute code if value == case
#match name: case 1: .... case 2: .... case _: ...

#modules: a file containing code u want in ur program
#eg import time, math, etc

#variable scope: LEGB (local, enclosed, global, built in)

#if name==main:..if we dont run this program directly, dont do it

#object = a bundle of related attributes (variables) and 
#  methods (functions)
# object =  cup is object (liquid inside, temperature, attributes)
#           methods for cup is fill, drink and empty.
#           class is a blueprint used to design the structure and layout of object


import sys #system, gives access to vars used by python interpretor
from PyQt5.QtWidgets import QApplication 
from gui_windows.welcome_screen import WelcomeScreen  # adjust import path based on your folder structure

def main():
    app = QApplication(sys.argv)
    #remember if else statement for running welcome or main
    window = WelcomeScreen()
    #window.show()  # optional if you're already calling showMaximized() in the constructor
    sys.exit(app.exec())

if __name__ == "__main__":
    main()