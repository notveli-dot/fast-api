# open(file location, mode) is used to open a text document (.txt file)
# r read
# w write(overwrite existing text)
# a append( adds to the existing text)
# x create(if fail to exist)

# FIRSTLY Open the file
# Read the file
# .read() reads the entire file    .readline() reads the first line    .readlines() reads all the line into a list
# .strp()
# file =open("json.txt")
# init_reading =file.readlines()
# stripped_reading= []
# for line in init_reading:
#     stripped_reading.append(line.strip())
# print(stripped_reading)
# file.close()
# with open("json.txt") as file:
#     a = file.read()
#     aa =[]
#     for line in a.split(): #.slipt() runs the file based on the number of lines available slipting them without the \n
#         print(line)
#     for line in a.capitalize(): #.capitalize runs each line of the file element on a new line
#         print(line)
#     for line in a.encode(): #.encode runs the text by the number of characters in the file
#         print(a)


# WRITING TO FILE
# .write("") Writes a string to the file
# .writeline = writes a list of strings
with open("json.txt", "a") as file:
    file.write("Person 5\nPerson6\nPerson7\nPerson8\nPerson9\nPerson10\n")


with open("json.txt", "r") as file:
    print(file.read())
# JSON is used to store a structured data
# JSON is an acronym for JavaScript Object Notation
# It is a standardized means of storing and exchanging and storing structured data
# JSON is similar to a dictionary
# {"name":"kodecamp:
# "age": 50
# "is_active = true
# }
# JSON structure doesn't support boolean value: it uses true instead of True
