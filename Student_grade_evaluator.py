from xml.dom.minidom import ProcessingInstruction

NumberOfStudent = int(input("How many students are to be processed: "))
passed = 0
failed = 0
excellent = 0
for i in range(NumberOfStudent):

    name = str(input("Enter student's name: "))

    score1 = float(input("Enter score for Subject 1 (0-100): "))
    score2 = float(input("Enter score for Subject 2 (0-100): "))
    score3 = float(input("Enter score for Subject 3 (0-100): "))
    average = (score1 + score2 + score3)/3
    if average >= 80 :
        excellent = excellent + 1
        print("you are excellent.")
    elif average >= 50 :
        passed = passed + 1
        print("you passed.")

    else:
        failed = failed + 1
        print("you failed.")
    print(average)

print("EVALUATION SUMMARY")
print()
print("The total number of students with excellent =", excellent)
print()
print("The total number of students with passed =", passed)
print()
print("The total number of students with failed =", failed)
print()
