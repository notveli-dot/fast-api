# introduction message
print("                   W E L C O M E  T O  M Y  Q U I Z                    ")
# Questions and their answers and their options
Questions = ("How many days are in a week",
             "What is 2 + 2",
             "What is the capital of Nigeria",
             "What planet are we in",
             "How many months are in a year",
             )
options = (("A. 7","B. 8","C. 9","D. 6"),
           ("A.9","B.3","C. 6","D. 4"),
           ("A. Lagos","B. Abuja","C. Akwa Ibom","D. Calabar"),
           ("A. Mercury","B. Venus","C. Earth","D. Saturn"),
           ("A. 11","B. 14","C. 13","D. 12"))
Answers = ("A", "D","B", "C", "D")
# User Input to enter the correct answer
Guesses = []
# Grading
Score = 0
Question_num = 0

#Main body of program where everything happens, all the iterations and conditions
for question in Questions:
    print("____________________________________________________________________")
    print(question)
    for option in options[Question_num]:
        print(option)

    Guess = input("Enter (A), (B), (C), (D)").upper()
    Guesses.append(Guess)
    if Guess == Answers[Question_num]:
        Score += 1
        print("Correct!")
    else:
        print("INCORRECT!")
        print(f"{Answers[Question_num]} was the correct answer!")
    Question_num += 1
print("____________________________________________________________________")
print("                          R E S U L T                               ")
print("____________________________________________________________________")

# Scoring the users guesses in percentage
Score = int(Score / len(Questions) * 100)
print("your score is", Score)
