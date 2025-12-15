# Modules are python files that contains your variables, functions, and classes. They are basically your python scripts
# They can be included in  another python script

# 2 kinds of importation
# Entire module Importation
# Specific Importation
# To carry out an entire importation we simply use the keyword import followed by the module names
# For specific we simply use the keyword from module name import specific func/var/classes
#  Types of module
# Custom modules
# Builtin modules
# Third-party modules
# IMPORTING CUSTOM MODULE
import mod
# from mod import greetings, age
# a = greetings("VELI")
# print(a)
# b = age(210)
# print(b)
# r =dir(mod)
# print (r)
# using json........................REMEMBER
import random
import json
from mod import menu
# USING DICT
score={
    "addition": 0,
    "subtraction": 0,
    "multiplication": 0,
}
# CONVERTING DICTIONARY TO JSON
# dict_conversion =json.dumps(score)
json_form= ""
try:
    with open("score.json","r") as file:
        json_form = json.load(file)
        print(type(json_form))
    # actual_value = json.loads(json_form)
    # print(actual_value)

# score_1 = [0,1,2,3,4,5,6,7,8,9]
# with open("score.json","w") as file:
#     json.dump(score_1,file)
except:
    with open("score.json", "w") as file:
        json_form= json.dump(score, file)
        json_form = json_form
print(json_form)






while True:
    menu()

