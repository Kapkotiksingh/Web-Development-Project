# Step -1 (Exercise 1 - Data Types)

"""
Example Input
39

Example Output
3 + 9 = 12
12

"""

# Solved
s  = input("Type a two digit number: ")
v = int(s[0])+int(s[1])
print(v)

# Step -2 (Exercise 2 - BMI Calculator)

"""

Warning you should convert the result to a whole number.
Example Input

weight = 80
height = 1.75

Example Output

80 ÷ (1.75 x 1.75) = 26.122448979591837
26

"""

# Solved 

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

total = int(weight)/float(height)**2
print(int(total))

# Step -3 (Exercise 3 - Life in Weeks )

"""
Example Input

56

Example Output

You have 12410 days, 1768 weeks, and 408 months left.
"""

# Solved 

age = input("What is your current age? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


# Step -4 (Day 2 Project: Tip Calculator)


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


# Solved 

print("Welcome to the tip calculator.")

total_input = input("What was the total bill? ")
tip_percentage_input = input("Which percentage tip would you like to give? 10, 12, or 15? ")
people_input = input("How many people to split the bill? ")

total = float(total_input)
tip = int(tip_percentage_input)/100 + 1
people = int(people_input)

tip_per_person = round((total/people) * tip, 2)

print(f"Each person should pay: ${tip_per_person}")
