#C L A S S E S / O O P   I N   P Y T H O N
# CLASSES ARE BASICALLY BLUEPRINT FOR CREATING OBJECTS
# N/B ARE USED TO MODEL REAL WORLD ENTITIES(things that can have attributes and actions)
# CLASSES ARE USED TO GROUP RELATED ATTRIBUTES AND ACTIONS TOGETHER
#
#C L A S S OFFERS INHERITANCE, ENCAPSULATION, ADAPTABILITY,
# class classname:
#     info
#     design
#     design
#     design
#     design
# #
# #
#           B A N K   A C C O U N T
# bankname = input()
# banklocation1 = input()
# user_services = input("deposit, withdraw, save")
#
# Account_balance1 = 1000
# Account_name = "Alice"
# Account_balance2 = 2000
# def withdraw(account_balance2, amount, account_name):
#     return "new account balance"
# class bank_account():
#     def add_money(self):
#         pass
#
# account1= bank_account() #instance of our custom class
# # print(type(account))
# account1.add_money()
# account2 = bank_account()
# account2.add_money()
# print(account1)
# print(account2)



#  C L A S S E S   I N   P Y T H O N
class BankAccount:
    def __init__(self, name, age,phone, email=""):
        self.name = name
        self.age = age
        self.email = name + ".company@gmail.com"
        self.accountNumber = phone[11]
        self.accountBalance = 0
    # BankAccount Methods
    def check_balance(self):
        print("Your Account balance is .....")

    def deposit(self, amount):
        print(self)
         # Actual printing
        self.accountBalance = self.accountBalance + amount
        print("Your deposited amount is ", amount)

    def withdraw(self, amount):
        print("Your withdrawn amount is ", amount)




# x = "hello".endswith("s")
# # x.upper()
# y = "house"
# z = BankAccount()
# z.deposit(1000)
# z.withdraw(50)
# z.check_balance()
# z.name = "Saviour" #Position affects the code
# y = BankAccount()
# y.name = "KodeCamp"
# y.deposit(20)
# print(z.name)
# x.check_balance()
x = BankAccount(input("Enter your name"),input("Enter your age"),input("Enter your phone number"))
# y = BankAccount(input("Enter your name"),input("Enter your age"),input("Enter your phone number"))
# z = BankAccount(input("Enter your name"),input("Enter your age"),input("Enter your phone number"))
print(x.name)
# print(y.name)
print()
print(x.accountNumber)
print(x.accountBalance)
x.deposit(10000)