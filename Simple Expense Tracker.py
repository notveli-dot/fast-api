#  Simple Expense Tracker
# Scenario: Help users track their daily expenses.
# Instructions:
# - Let user enter multiple expenses: description + amount
# - Store as a list of dictionaries e.g., {"item": "Transport", "amount": 150.0}
# - Allow menu options:
#  - Add expense
#  - View all expenses
#  - Total and average
#  - Exit
# - Use try-except for amount input
# - Use loops and functions

from typing import List, Dict

# List to hold expense records: each is {"item": str, "amount": float}
expenses: List[Dict[str, float]] = []

def add_expense(expenses: List[Dict[str, float]]) -> None:
    """
    Prompt the user for an expense description and amount.
    Uses try-except to validate the amount input.
    Appends a dictionary to the expenses list.
    """
    description = input("Enter expense description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    while True:
        raw = input("Enter amount (e.g., 12.50): ").strip()
        # Allow commas in numbers (e.g., "1,234.56")
        raw = raw.replace(",", "")
        try:
            amount = float(raw)
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    expenses.append({"item": description, "amount": amount})
    print(f"Added: {description} - {amount:.2f}")

def view_expenses(expenses: List[Dict[str, float]]) -> None:
    """
    Print all recorded expenses with indices and formatted amounts.
    """
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAll expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['item']} - {exp['amount']:.2f}")
    print("")  # blank line for spacing

def total_and_average(expenses: List[Dict[str, float]]) -> None:
    """
    Compute and display the total and average expense amounts.
    """
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(exp["amount"] for exp in expenses)
    average = total / len(expenses)
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")

def main() -> None:
    """
    Main loop presenting the menu until the user exits.
    """
    menu = (
        "1. Add expense\n"
        "2. View all expenses\n"
        "3. Total and average\n"
        "4. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_and_average(expenses)
        elif choice == "4":
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 4.")

if __name__ == "__main__":
    main()