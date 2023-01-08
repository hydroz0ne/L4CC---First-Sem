#Chapter 5 Exercises
#1. Person
#This code is a dictionary with the details of a person such as their name, age, and city of residence.
person = {'first_name': 'Tenzid', 'last_name': 'Rajesh', 'age': 16, 'city': 'Abu Dhabi'}
#This part of the code then prints out each part of the dictionary.
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#2. Glossary
#This code is a "glossary" which is also a dictionary with the details of different terms in Python.
glossary = {
    'string': 'A sequence of unicode characters.', 'comment': 'A line in the Python program whcih explains the code.',
    'list': 'A collection of items in a variable.', 'loop': 'Used for repeating a program or a part of a program multiple times.', 
    'dictionary': "An sorted collection of different keys and values as pairs."
    }

#This part of the code prints the word and the meaning of the word that was listed in the dictionary.
word = 'string'
print("\n" + word.title() + ": " + glossary[word])
word = 'comment'
print("\n" + word.title() + ": " + glossary[word])
word = 'list'
print("\n" + word.title() + ": " + glossary[word])
word = 'loop'
print("\n" + word.title() + ": " + glossary[word])
word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])

#3. Glossary #2
#This code is a continuation of the previous exercise the details of different terms in Python.
glossary = {
    'string': 'A sequence of unicode characters.', 'comment': 'A line in the Python program whcih explains the code.', 
    'list': 'A collection of items in a variable.', 'loop': 'Used for repeating a program or a part of a program multiple times.', 
    'dictionary': "An sorted collection of different keys and values as pairs.", 'object': 'A collection of data and methods.', 
    'nested loop': 'A loop within another loop.', 'loader': 'An object that loads a module that is being imported.', 
    'module': 'A file consisting of Python code.', 'set': 'An unordered collection of data that allows only unique values.'
    }

#Instead of having the dictionary use a separate line of code per word and meaning, there will be a loop that prints the word and its meaning.
#The program will end once every key and value has been printed by the loop.
for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

#4. Rivers
#This code is a dictionary with different rivers and the country where each river runs through.
rivers = {'Nile': 'Egypt', 'Amazon River': 'South America', 'Huang Ho River': 'China',}
#This part of the code is a loop prints a message about each river.
for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")
#This part of the code is a loop which prints each river in the dictionary.
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())
#This part of the code is a loop which prints each country in the dictionary.
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())

#5. Pets
pets = []
#This code is a dictionary with the details of a pet from the animal type, name, the owner, it's weight, and what their pets eat.
pet = {'Name': 'Hachi', 'Animal type': 'Rabbit', 'Owner': 'John', 'Weight': 2, 'Food type': 'Carrots'}
pets.append(pet)
pet = {'Name': 'Mochi', 'Animal type': 'Hamster', 'Owner': 'Angela', 'Weight': 2, 'Food type': 'Seeds'}
pets.append(pet)
pet = {'Name': 'Boomer', 'Animal type': 'Dog', 'Owner': 'Moris', 'Weight': 37, 'Food Type': 'Beef'}
pets.append(pet)

#This part of the code displays the information about each pet and their owner.
for pet in pets:
    print("\nHere's what I know about " + pet['Name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))