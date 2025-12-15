# WHAT IS FUNCTION
# Function is a collection of reusable code that perform a specific action
# Is a way of grouping source code, reuse the source code without rewriting the source code
# When using function, 2 steps are involved
# Creating/initializing a function
# Calling/Invoking a function

# CREATION
# HOW TO CREATE A FUNCTION
# USING THE KEYWORD def
# SYNTAX
# def function_name(optional parameters):
#       body
#
#
#      optional return statement

# The parameter takes in value, the return takes out values
# Use the return statement when you want to set out an end product
# CALLING A FUNCTION



# SYNTAX:
# function_name(optional argument)

# DIFFERENCE BETWEEN FUNCTION PARAMETERS AND ARGUMENTS
# Parameters are more like placeholders for the actual values
# Argument is the actual values
# Uses of function parameters
# VARIABLE SCOOPING
# Variable defined within a function is not accessible outside the function,it is local function
# Variable defined outside a function is called Global function
# A function can be a value for a variable
# num1 = 50
# num2 = 40

# def multiplication(num1, num2):
#     result = num1*num2
#     # answer = num1*num2
#     print(result)
#     return result, "Another value"
# def age_mult(age,multiplier):
#     mult = age*multiplier
#     print(mult)
#
# def first_function():
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 + num2
#     print(result)

# multiplication(30,50)
# a = multiplication(num1, num2)
# print(a)

# age_mult(20,multiplication(num1, num2))



# E R R O R  H A N D L I N G
# EXCEPTIONS IS A TYPE OF ERROR THAT OCCURS DURING EXECUTION
# TO HANDLE EXCEPTIONS IN PYTHON WE USE 2 KEYWORDS: try/except
# zerodivisionerror
# valueerror
# nameerror
# syntaxerror
# typeError
#finally/else
try:
    num3 = int(input("Enter a number: "))
    num4 = int(input("Enter another number: "))
    answer = num3/num4

except ZeroDivisionError:
    print("Error with dividing by zero")
    answer= 0
except ValueError:
    print("Error with input")
    answer= 0

print(answer)
print("code")
print("another code")