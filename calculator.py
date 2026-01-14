# Calculator with History
# Scenario: A basic calculator that remembers past results.
# Instructions:
# - Show options: Add, Subtract, Multiply, Divide, View History, Exit
# - Use input to take two numbers and perform operation
# - Store each operation and result in a list
# - Show history with index numbers
# - Use functions for operations and error handling for divide-by-zero
# calculator.py
from typing import List, Dict, Optional

# History list: each entry is a dict with operation name, operands, and result
history: List[Dict[str, float]] = []

def get_number(prompt: str) -> float:
    """Prompt until a valid number is entered; returns the float value."""
    while True:
        raw = input(prompt).strip()
        raw = raw.replace(",", "")  # allow commas like "1,234.56"
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Return a / b or None if divide-by-zero occurs."""
    if b == 0:
        return None
    return a / b

def perform_operation(op_name: str) -> None:
    """
    Read two numbers, perform the requested operation, handle errors,
    store the result in history and print the outcome.
    """
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if op_name == "Add":
        result = add(a, b)
        symbol = "+"
    elif op_name == "Subtract":
        result = subtract(a, b)
        symbol = "-"
    elif op_name == "Multiply":
        result = multiply(a, b)
        symbol = "*"
    elif op_name == "Divide":
        result = divide(a, b)
        symbol = "/"
        if result is None:
            print("Error: Division by zero is not allowed.")
            # Still record the attempted operation with result as None
            history.append({"op": op_name, "a": a, "b": b, "result": None})
            return
    else:
        print("Unknown operation.")
        return

    # Store successful result in history
    history.append({"op": op_name, "a": a, "b": b, "result": result})
    print(f"Result: {a} {symbol} {b} = {result}")

def view_history() -> None:
    """Print the stored operations with index numbers and results."""
    if not history:
        print("History is empty.")
        return

    print("\nHistory:")
    for idx, entry in enumerate(history, start=1):
        a = entry["a"]
        b = entry["b"]
        op = entry["op"]
        res = entry["result"]
        if res is None:
            res_text = "Error (e.g., divide by zero)"
        else:
            res_text = str(res)
        # Choose a human\-friendly operator display
        symbol = {
            "Add": "+",
            "Subtract": "-",
            "Multiply": "*",
            "Divide": "/"
        }.get(op, "?")
        print(f"{idx}. {op}: {a} {symbol} {b} = {res_text}")
    print("")  # blank line for spacing

def main() -> None:
    """Main menu loop."""
    menu = (
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. View History\n"
        "6. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            perform_operation("Add")
        elif choice == "2":
            perform_operation("Subtract")
        elif choice == "3":
            perform_operation("Multiply")
        elif choice == "4":
            perform_operation("Divide")
        elif choice == "5":
            view_history()
        elif choice == "6":
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()