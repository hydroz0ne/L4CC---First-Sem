#Chapter 3 Exercises
#1. Name
#This code uses a list to list each name. The code then prints the different names from the list.
names = ["Sam", "Manly","Rosver"]
print(names[0])
print(names[1])
print(names[2])



#2. Greetings
#This code uses a list to list each name. The code then prints the different names from the list but with an included greeting.
names = ["Sam", "Manly","Rosver"]
msg = (f"Hello, {names[0].title()}!")
print(msg)
msg = (f"Hello, {names[1].title()}!")
print(msg)
msg = (f"Hello, {names[2].title()}!")
print(msg)



#3. Your Own List
#This code uses a list to list each type of transportation & brand.
brand = ["Subaru", "Ducati","BMX"]
transpo = ["car", "motorcycle","bike"]
#This part of the code prints out a sentence with the 3 different values from both lists.
msg = (f"I want to own a {brand[0]} {transpo[0]}.")
print(msg)
msg = (f"I want to own a {brand[1]} {transpo[1]}.")
print(msg)
msg = (f"I want to own a {brand[2]} {transpo[2]}.")
print(msg)



#4. Guest List
#This code uses a list to list each name. The code then prints the different names from the list with a invitation to dinner.
guests = ["Sam", "Manly","Rosver"]
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")



#5. Change Guest List
#This code uses a list to list each name. The code then prints the different names from the list with a invitation to dinner.
guests = ["Sam", "Manly","Rosver"]
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")

#One person couldn't make it to dinner so the code prints a message that a person is not able to join.
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

#This part of the code substitutes a value from the list as one of the guests cannot make it to the dinner.
del(guests[1])
guests.insert(1, 'Elizah')

#This part of the code reprints the guest list invitations.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")




#6. Shrinking Guest List 
#This code uses a list to list each name. The code then prints the different names from the list with a invitation to dinner.
guests = ["Sam", "Manly","Rosver"]
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")

#One person couldn't make it to dinner so the code prints a message that a person is not able to join.
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

#This part of the code substitutes a value from the list as one of the guests cannot make it to the dinner.
del(guests[1])
guests.insert(1, 'Elizah')

#This part of the code reprints the guest list invitations.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")

#This part of the code pops out all the guests except two other people.
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry {name.title()}, there's no room at the table.")

#This part of the code prints an invite for the two people remaining.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")

#This part of the code deletes the two people remaining to then print an empty guest list.
del(guests[0])
del(guests[0])

print(f"\n{guests}")    




#7. Seeing the World
#This code prints out five countries that I would like to visit someday, in different orders.
locations = ['Korea', 'Ghana', 'Japan', 'Brazil', 'Canada']

print("Original Order:")
print(locations)

#This part of the code prints the list in an alphabetical order, then prints the original order.
print("\nAlphabetical:")
print(sorted(locations))
print("Original Order:")
print(locations)

#This part of the code prints the list in an reversed alphabetical orde, then prints the original orderr.
print("\nReverse Alphabetical:")
print(sorted(locations, reverse = True))
print("Original Order:")
print(locations)

#This part of the code prints the list in an reversed order, then prints the original order.
print("\nReversed:")
locations.reverse()
print(locations)
print("Original Order:")
locations.reverse()
print(locations)

#This part of the code prints the list in an alphabetical order, then the reversed alphabetical order.
print("\nAlphabetical")
locations.sort()
print(locations)
print("Reverse Alphabetical")
locations.sort(reverse = True)
print(locations)