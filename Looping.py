# LOOPING is repetition of code
# TYPES OF LOOP
# FOR LOOP is the type of loop that repeats a portion of code based on the number of items in  a structure
# WHILE LOOP is thr type of loop that repeats a number of code based on conditioner
# FOR LOOP SYNTAX
#  for variable_name in structure:
#       portion of code to execute
#       portion of code to execute
#       portion of code to execute


# WHILE LOOP SYNTAX
# While condition:
#       portion of code to execute
#       portion of code to execute
#       portion of code to execute

# LOOP KEYWORDS:These are keywords that ulter the default behaviour of a loop
# Break: terminates the loop before time
# continue:Skips the current iteration to a new one
#
grand_total = 0
a = int(input("Enter your desired repition:"))
for item in range(a):
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    result = num1 + num2
    grand_total = grand_total + result
    continue
    print("The addition of", num1, "and", num2, "is", result)
    print()
print(grand_total)
if result > 100:
    print("That's too high")

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
#
# while a>b:
#     print("You are good to go")
#     break
#

# a = 6
# b = 3
# while a > b:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter another number:"))
#     result = num1 + num2
#     print("the addition of",num1,"and",num2,"is",result)
#     print()
#     b =b + 1
#     print("The end")
#     break

