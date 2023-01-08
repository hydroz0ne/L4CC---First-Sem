#Chapter 6 Exercises
#1. Pizza Toppings
#This code is a loop that asks the user to enter different pizza toppings until they enter 'quit' to quit from the program. 
prompt = "\nHello! What topping would you like to add on your pizza?"
prompt += "\nEnter 'quit' when you are done: " #When the user wants to stop the program, the user can type 'quit' so they can quit the program.

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("I'll add " + topping + " on the pizza.")
    else:
        break

#2. Movie Tickets
#This code prints a loop in which the user enters their age then prints the cost of their movie ticket.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are done: " #When the user wants to stop the program, the user can type 'quit' so they can quit the program.

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("You get in for free!")
    elif age < 13:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

#3. Infinity
#This code is the code from exercise 2 in chapter 6, although there will be no prompt to quit from the code.
#With no prompt to quit, the user cannot quit the infinite loop of the code asking the question to the user.
while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 3:
        print("You get in for free!")
    elif age < 13:
        print("Your ticket costs $10.") 
    else:
        print("Your ticket costs $15.")

#4. Deli
#This code shows a process of a deli doing their sandwich orders.
#The list for the sandwich orders has 4 values which are 'egg', 'grilled cheese', 'turkey', and 'roasted beef'.
sandwich_orders = ['egg', 'grilled cheese', 'turkey', 'roasted beef']
finished_sandwiches = [] 

#This part of the code tells the user that their sandwiches are currently being made.
while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print("I am making your " + current_sandwich + " sandwich.")
        finished_sandwiches.append(current_sandwich)

print("\n") #This adds space from the process of making the sandwich.
#This part of the code then tells the user than the sandwiches has been made.
for sandwich in finished_sandwiches:
        print("I made you a " + sandwich + " sandwich!")

#5. No Pastrami 
#The list for the sandwich orders has 5 values which are 'egg', 'grilled cheese', 'turkey', 'pastrami', and 'roasted beef'.
sandwich_orders = ['pastrami', 'egg', 'grilled cheese', 'pastrami','turkey', 'pastrami', 'roast beef']
finished_sandwiches = []

#This part of the code removes the value 'pastrami' from the list.
print("I'm sorry but there's no more pastrami.")
while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

print("\n") #This adds space from the process of making the sandwich.
#This part of the code tells the user that their sandwiches are currently being made.
while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print("I am making your " + current_sandwich + " sandwich.")
        finished_sandwiches.append(current_sandwich)

print("\n") #This adds space from the process of making the sandwich.
#This part of the code then tells the user than the sandwiches has been made.
for sandwich in finished_sandwiches:
        print("I made you a " + sandwich + " sandwich!")