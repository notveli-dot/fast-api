# CONTROL FLOW is the order of execution of our program
# Conditioners is the ability for our program to make choices
# 3 keywords are used to achieve conditioners
# If only executes your specified code only when a condition is true
# Else
# Elif is the short form of else if. It is used in conjunction with if statement to construct statement for other conditions
# Conditional operators: >, <, <=, >=, ==,!=
# LOGICAL OPERATORS: Can be used in conjunction with conditional operators to construct a more complex conditions
# Condition in programming refers to an expression that must evaluate to a boolean value(True/false)
# example 3 + 3 - 1
# name = "Gods power" (This is a statement not an expression)
# SYNTAX
# if condition:
#     your specified code to be executed
# print("HELLO WORLD")
# NESTING IN CONDITIONERS Nesting is having a conditional statement inside another conditional statement
name = str(input("Enter your name:"))
age = int(input("Enter your age:"))
minimumAge = 18
maximumAge = 49
if age >= minimumAge and age <= maximumAge:
    Gender = str(input("Enter your gender(Male/Female):"))
    if Gender == "Male":
        print("Hello Mr",name, "you are eligible for registration")
    elif Gender == "Female":
        print('Hello Mrs',name, "you are eligible for registration")
    else:
        print("Invalid gender")
elif age > maximumAge:
    print("You are too old \n")
    print("Sorry, you are not eligible")
else:
    print("You are not eligible \n")
    print("Apply after",minimumAge - age,"Years")

# print()
# name = input("Enter your name:")
# print()
# print("Hello!", name)
# print()
