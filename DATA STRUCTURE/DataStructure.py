# DATA TYPES
# int, float, str, bool,
# DATA STRUCTURES IN PYTHON
# list, dict, tuple, set
# DATA STRUCTURE are ways of organizing, storing and managing data efficiently to perform effectively
#
# name = "DataStructure"
# age = 100
# LIST DATA STRUCTURE(DATA TYPE IN PYTHON)
# How does list work???
# List is basically an ordered MUTABLE collection of items, separated by commas and enclosed in a square bracket.
# These items can be of any data type in python
# SYNTAX TO ACCESSING A SINGLE LIST ITEM
# print(list_name[index number])
#
# SYNTAX TO CHANGING ITEM IN A LIST
# ages[item_index] = new_item
# List supports duplication, because list is order and each item is unique
# ages = [20,30,40,50,60,70]
# mixed_types = [100, 17.5,True,"Learning"]
# print(ages)
# print()
# print(mixed_types)
# Item_count = len(ages)
# print(Item_count)
# ages[Item_count - 1] = 100
# print(ages)


# LIST METHOD
# SYNTAX
# list_name.method_name()
# ages.append(59)
# print(ages)
# APPEND IS MOSTLY USED TO ADD ITEMS TO THE LIST
# ages.copy()
# New_ages = ages.copy
# print(ages)
# HEAP MEMORY is an unorganized memory,but saves the reference in stack
# STACK MEMORY is a known fixed size memory,
# print(New_ages)
# New_ages.append("hello")
# print(New_ages)
# print(ages)


# TUPLE is basically an ordered immutable collection of items, separated by commas and enclosed in parentheses
# ACCESSING A LIST ITEM
# Syntax:
# TULE METHODS: count and index
# tuple_name[index]




# DICTIONARY is basically unordered collection of key value pairs separated by commas and enclosed in curly braces{
# These keys are unique and immutable
# You can have duplicate values but unique keys
# Keys are commonly strings or numbers or tuples
# gender = ("male","female","female", "male")
# print(gender[0])
# print(gender[1])
# print(gender[2])
# print(gender[3])
# print(gender.count("female\n\n\n"))


# ages = [20,30,40,50,60,70,70]
# final_result = 1
# for item in ages:
#     final_result = final_result * item
#     print(item)
#     print("hello")
#     print(final_result)
#     print("\n")

ages = {"person1":20, "person2":25, "person3":35}

# ACCESSING OF ITEMS
# SYNTAX
# dict_name[key]

print(ages["person1"])
# CHANGING DICT VALUES
# SYNTAX
# dict_name[key] = New_value
ages["person1"] = 50
print(ages["person1"])

# ADDING VALUE
# SYNTAX
# dict_name[key] = new _value

ages["person4"] = 40
print(ages)


# DICT METHODS
# dict_name.method_name()
print(ages.get("person2"))
print(ages.items())
print(ages.keys())
print(ages.values())

# SET