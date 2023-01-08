#Chapter 1 Exercises
#1. Print Strings
#This code prints the song "Twinkle Twinkle Little Star".
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2. Print the Version of Python 
#This code prints the current version of Python.
from argparse import Namespace
from math import pi
import sys
from typing import List
print ("Python version: ")
print (sys.version) #Statement prints the version number of the Python system.
print ("Version info: ")
print (sys.version_info) #Statement prints the version info of the Python system.

#3. Print date and Time
#This code prints the current time and date by importing the date and time from the PC.
import datetime
now = datetime.datetime.now()
print ("Current date and time: ")
print (now.strftime("%Y-%m-%d, %H:%M:%S")) #Statement prints the current date and time imported from the user's device.

#4. Strings Concatination; Write three strings in different variables and print the output as one string.
#This code combines 3 strings and prints the 3 strings together.
print("yes? " + "no? " + "maybe?")

#5. Compute area of Circle
#This code computes the area of a circle by asking the user to input the radius of a circle and then computing the area.
from math import pi
r = float(input ("Enter radius of circle : ")) #Input asks the user a question on what is the radius of the circle.
print ("The area of the circle is: " + str(pi * r**2)) #Statement prints the calculated area of the circle.