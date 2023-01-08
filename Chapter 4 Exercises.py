#Chapter 4 Exercises
#1. Alien Colors #1
#Passing - This code gives the user 5 points if the alien shot is green.
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

#Failing - This code gives the user 5 points if the alien shot is green but the alien color is red, printing a blank result.
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")

#2. Alien Colors #2
#If Block - This code gives the user 5 points if the alien shot is green. If the alien isn't green, the user earns 10 points.
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#Else Block - This code gives the user 5 points if the alien shot is green. If the alien isn't green, the user earns 10 points.
alien_color = 'blue'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#3. Alien Colors #3
#This code gives the user 15 points as the color of the alien shot is red.
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

#This code gives the user 10 points as the color of the alien shot is yellow.
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("You just earned 10 points!")

#This code gives the user 5 points as the color of the alien shot is green.
alien_color = 'green'
if alien_color == 'red':
    print("You just earned 15 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 5 points!")

#4. Stages of Life
#This code prints a different message based on your age.
age = 25
#This part of the code proceeds to print a message if they are one of the six choices based on the user's age.
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

#5. Favorite Fruit
#This code prints the three different fruits from the list with the message saying that the user loves the fruit.
favorite_fruits = ['banana', 'apricot', 'avocado']
#This part of the code prints a message for each fruit that the user. 
#If a specific fruit isn't in the list, the message for the specific fruit will not be printed.
if 'banana' in favorite_fruits:
    print("You really like banana!")
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'apricot' in favorite_fruits:
    print("You really like apricot!")
if 'avocado' in favorite_fruits:
    print("You really like avocado!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapple!")