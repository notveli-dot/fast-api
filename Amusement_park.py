#  Amusement Park Entry Checker
#
# Scenario: Check multiple visitors' ticket prices.
#
# Instructions:
#
# - Use a loop to allow repeated entries.
#
# - For each visitor:
#
#      - Ask name and age (int).
#
#      - Based on age:
#
#      - < 5: Free
#
#      - 5-17: $5
#
#      - 18-59: $10
#
#      - 60+: $7
#
#      - Ask if they have a coupon (Yes/No). If yes, apply 20% discount.
#
#      - Show final price.
#
# # - Exit loop when a special name like 'done' is entered.

# WELCOME MESSAGE
print("Welcome to the Amusement Park Ticketing System")
while True:
    name = input("Enter visitor's name (or type 'done' to exit): ").strip()
    if name.lower() == 'done':
        print("Exiting the ticketing system. Have a great day!")
        break

    while True:
        try:
            age = int(input(f"Enter {name}'s age: "))
            break
        except ValueError:
            print("Please enter a valid age.")

    # Determine base ticket price based on age
    if age < 5:
        price = 0
    elif 5 <= age <= 17:
        price = 5
    elif 18 <= age <= 59:
        price = 10
    else:  # age 60+
        price = 7

    # Check for coupon
    has_coupon = input("Does the visitor have a coupon? (Yes/No): ").strip().lower()
    if has_coupon == 'yes':
        discount = price * 0.20
        price -= discount

    print(f"The final ticket price for {name} is: ${price:.2f}\n")


