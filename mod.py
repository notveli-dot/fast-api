from mod2 import addition as add
import random
import json
addition = 0
subtraction = 0
multiplication = 0

def menu():
    print("___________________________________________")
    print("___________________________________________")
    print("        WELCOME TO MY CHILDREN GAME        ")
    print("___________________________________________")
    print("___________________________________________")
    print("     Which game do you want to play?       ")
    print("                1. Addition                ")
    print("             2. Subtraction                ")
    print("             3. Multiplication             ")
    print("___________________________________________")
    print()
    while True:
        try:
            option = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a Valid number")
            print()
            continue
#                A D D I T I O N
    if option == 1:
        for item in range(10):
            print()
            num1 = random.randint(1,20)
            num2 = random.randint(1,20)
            print(f"What is The addition of {num1} + {num2}")
            while True:
                try:
                    answer = int(input("Enter: "))
                    break
                except ValueError:
                    print("Please enter a Valid number")
                    print()
                    continue
            if answer == (num1 + num2):
                print("Correct Answer")
                global addition
                addition += 1




            else:
                print("Incorrect Answer")


            if item == 9:
                print()
                print("Your total score for addition is ", addition)
                print()
                print()
                json_form = None
                try:
                    with open("score.json", "r") as file:
                        json_form = json.load(file)
                        print(type(json_form))
                    # actual_value = json.loads(json_form)
                    # print(actual_value)

                # score_1 = [0,1,2,3,4,5,6,7,8,9]
                # with open("score.json","w") as file:
                #     json.dump(score_1,file)
                except:
                   print("No previous score file found, creating new one")
                else:
                    json_form["addition"] = addition
                    with open("score.json", "w") as file:
                        json_form =json.dump(json_form, file)
                    print("Score updated successfully")



    if option == 2:
        for item in range(10):
            print()
            num1 = random.randint(1,20)
            num2 = random.randint(1,20)

            print(f"What is The subtraction of {num1} - {num2}")
            while True:
                try:
                    answer = int(input("Enter: "))
                    break
                except ValueError:
                    print("Please enter a Valid number")
                    print()
                    continue
            if answer == (num1 - num2):
                print("Correct Answer")
                global subtraction
                subtraction += 1



            else:
                print("Incorrect Answer")


            if item == 9:
                print()
                print("Your total score for subtraction is ", subtraction)
                print()
                print()
                json_form = None
                try:
                    with open("score.json", "r") as file:
                        json_form = json.load(file)
                        print(type(json_form))
                    # actual_value = json.loads(json_form)
                    # print(actual_value)

                # score_1 = [0,1,2,3,4,5,6,7,8,9]
                # with open("score.json","w") as file:
                #     json.dump(score_1,file)
                except:
                   print("No previous score file found, creating new one")
                else:
                    json_form["subtraction"] = subtraction
                    with open("score.json", "w") as file:
                        json_form =json.dump(json_form, file)
                    print("Score updated successfully")
    if option == 3:
        for item in range(10):
            print()
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)

            print(f"What is The multiplication of {num1} * {num2}")
            while True:
                try:
                    answer = int(input("Enter: "))
                    break
                except ValueError:
                    print("Please enter a Valid number")
                    print()
                    continue
            if answer == (num1 * num2):
                print("Correct Answer")
                global multiplication
                multiplication += 1



            else:
                print("Incorrect Answer")


            if item == 9:
                print()
                print("Your total score for multiplication is ", multiplication)
                print()
                print()
                json_form = None
                try:
                    with open("score.json", "r") as file:
                        json_form = json.load(file)
                        print(type(json_form))
                    # actual_value = json.loads(json_form)
                    # print(actual_value)

                # score_1 = [0,1,2,3,4,5,6,7,8,9]
                # with open("score.json","w") as file:
                #     json.dump(score_1,file)
                except:
                   print("No previous score file found, creating new one")
                else:
                    json_form["multiplication"] = multiplication
                    with open("score.json", "w") as file:
                        json_form =json.dump(json_form, file)
                    print("Score updated successfully")
print("Your total scores are:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

  
