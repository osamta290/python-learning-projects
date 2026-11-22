# Age Checker
# Ask the user for their name and age, then check whether they are an adult.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Welcome {name}! You are an adult. Your age is {age}.")
else:
    print(f"Welcome {name}! You are under 18. Your age is {age}.")
