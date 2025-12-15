# BANKING PROGRAM
def Acct_balance():
    print("Your balance is #", balance,"\n")


def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount > 0:
        print("Your deposit is #", amount)
        print("deposit successful\n")
        return amount

    else:
        print("Please enter a positive number\n")
        return deposit()


def withdraw():
    amount = float(input("Enter the amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds\n")
        return withdraw()
    elif amount < 0:
        print("Enter a positive number\n")
        return withdraw()
    else:
        print("Your withdraw is #", amount)
        print("withdraw successful \n")
        return amount





balance = 0
running = True


while running:
    print("Welcome to My Banking System")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        Acct_balance()
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance = balance - withdraw()
    elif choice == 4:
        running = False
    else:
        print("Please enter a valid choice")

print("Your final balance is #", balance)
print("Thank you for banking with us")