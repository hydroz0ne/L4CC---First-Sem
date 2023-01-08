#Chapter 2 Exercises
#1. Variables.
#This part of the code prints a variable.
txt = "Creative Computing is good."
print(txt)
#This part of the code then replaces the first variable and prints the new variable.
txt = "Coding is nice."
print(txt)

#2. Variables (Quote)
#This code prints a quote from a famous person.
print (""""Get busy living or get busy dying." - Stephen King.""")

#3. Stripping Names
name = "\tMorissey Monyl Carolino\n"

#This part prints the unchanged variable.
print("Normal text:")
print(name)

#The "lstrip()" returns a new string with removed spaces from the 'left' side of the string.
print("\nUsing lstrip():")
print(name.lstrip())

#The "rstrip()" returns a new string with removed spaces from the 'right' side of the string.
print("\nUsing rstrip():")
print(name.rstrip())

#The "strip()" returns a new string after removing any blank spaces, including tabs.
print("\nUsing strip():")
print(name.strip())

#4. Favorite Number
#This code prints out the user's given number with the message stating what is the favorite number.
fav_num = 10
favnum = (f"My favorite number is {fav_num}.")
print(favnum)

#5. USB Shopper
#This code shows an answer of a problem asking on how much USB sticks can be bought & how many pounds will have left.
#The code uses arithmetic operations to compute for the answer. 
a = 50 // 6
b = 50 % 6
print ("The girl can buy", a , "USB sticks with", b , "euro for change.") #Statement prints the answer which is listed in a sentence.