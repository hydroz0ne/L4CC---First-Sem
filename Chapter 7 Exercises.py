#Chapter 7 Exercises
#1. Message
#This code prints a sentence about what I am learning about in the subject. 
def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning variables, data structures, control flow, dictionaries, loops, and functions."
    print(msg)
display_message()

#2. Favorite Book
#This code prints a sentence about what is my favorite book to read . 
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books to read.")
favorite_book('Diary of a Wimpy Kid: The Last Straw')

#3. T-Shirt
#This code prints 2 sentences that gives the size of the shirt and the message that is printed on it.
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('The print will say, "' + message + '"')
make_shirt('large', 'I love sports!')
make_shirt(size = 'medium', message = "Games are fun to play!")

#4. Large Shirts
#This code prints 2 sentences that gives the size of the shirt and the message that is printed on it.
def make_shirt(size = 'large', message = 'I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('The print will say, "' + message + '"')
make_shirt()
make_shirt(size = 'medium')
make_shirt('small', 'I love food!')

#5. Cities
#This code print a simple sentence about three cities and which country they are in.
def describe_city(city, country='brazil'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)
describe_city('rio de janeiro')
describe_city('shinjuku', 'japan')
describe_city('salvador')