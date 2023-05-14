# That's a problom

# Step - 1 (Exercise 1 - Printing)
"""
Day 1 - Python Print Function
The function is declared like this:
print('what to print')


"""

# Solved  

print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")


# Step -2 (Exercise 2 - Debugging Practice)

"""
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.

"""

# Solved 

print('Day 1 - String Manipulation\nString Concatenation is done with the "+" sign.\ne.g. print("Hello " + "world")\nNew lines can be created with a backslash and n.')


# Step -3 (Exercise 3 - Input Function)
"""
Example Input
Angela

Example Output
6
"""

# Solved

var= input('What is your name? ')
print(len(var))


# Step -4 (Exercise 4 - Variables)

"""
Example Input
a: 3
b: 5

Example Output
a: 5
b: 3
"""

# Solved

a = input("a: ")
b = input("b: ")

c = []
c = a
a = b
b = c

print(a)
print(b)


# Day 1 Project: Band Name Generator

"""
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
"""

# Solved
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
