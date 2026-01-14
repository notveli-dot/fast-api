# Shopping Cart System
# Scenario: Simulate a mini-store system.
# Instructions:
# - Show a list of available items with prices (use a dictionary)
# - Let the user "add to cart" by entering item name and quantity
# - Store cart in a list of dictionaries:
#  {"item": "Rice", "quantity": 2, "price": 400}
# - Calculate total bill
# - Option to remove an item or clear cart
# - Loop until user exits
# - Handle invalid inputs and missing items

available_items = {
    "rice": {"name": "Rice", "price": 400.0},
    "beans": {"name": "Beans", "price": 120.0},
    "sugar": {"name": "Sugar", "price": 80.0},
    "oil": {"name": "Cooking Oil", "price": 250.0},
    "bread": {"name": "Bread", "price": 30.0},
}

# Cart is a list of dicts: {"item": "Rice", "quantity": 2, "price": 400.0}
cart = []

def show_items():
    """Display available items and prices."""
    print("\nAvailable items:")
    for key, info in available_items.items():
        print(f"- {info['name']} (code: {key}) : {info['price']:.2f}")
    print("")  # spacing

def find_cart_index(item_name):
    """Return index in cart for item_name (case-insensitive), or None if not found."""
    for idx, entry in enumerate(cart):
        if entry["item"].lower() == item_name.lower():
            return idx
    return None

def add_to_cart():
    """Prompt user to add an item and quantity to the cart."""
    name = input("Enter item name or code to add: ").strip()
    if not name:
        print("No item entered.")
        return

    key = name.lower()
    # Accept either the display name or the code (both map to the item if present).
    if key not in available_items:
        # Try to match by display name
        matched = None
        for k, info in available_items.items():
            if info["name"].lower() == key:
                matched = k
                break
        if matched is None:
            print("Item not found in available items.")
            return
        key = matched

    # Prompt for quantity
    raw_qty = input("Enter quantity (positive integer): ").strip()
    if not raw_qty:
        print("Quantity not entered.")
        return
    # Validate quantity as integer > 0
    try:
        qty = int(raw_qty)
        if qty <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return

    info = available_items[key]
    price = info["price"]
    display_name = info["name"]

    # If already in cart, increase quantity
    idx = find_cart_index(display_name)
    if idx is not None:
        cart[idx]["quantity"] += qty
        print(f"Updated {display_name} quantity to {cart[idx]['quantity']}.")
    else:
        cart.append({"item": display_name, "quantity": qty, "price": price})
        print(f"Added {display_name} x{qty} to cart.")

def view_cart():
    """Show cart contents with per-item totals and overall total."""
    if not cart:
        print("Cart is empty.")
        return
    print("\nCurrent cart:")
    for i, entry in enumerate(cart, start=1):
        item = entry["item"]
        qty = entry["quantity"]
        price = entry["price"]
        subtotal = qty * price
        print(f"{i}. {item} - qty: {qty} - unit: {price:.2f} - subtotal: {subtotal:.2f}")
    total = calculate_total()
    print(f"Total bill: {total:.2f}\n")

def calculate_total():
    """Return the total bill as float."""
    total = 0.0
    for entry in cart:
        total += entry["quantity"] * entry["price"]
    return total

def remove_item():
    """Remove a single item from the cart by index or name."""
    if not cart:
        print("Cart is empty.")
        return
    view_cart()
    choice = input("Enter item number or name to remove (or leave blank to cancel): ").strip()
    if not choice:
        print("Removal cancelled.")
        return
    # Try by index
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(cart):
            removed = cart.pop(idx)
            print(f"Removed {removed['item']} from cart.")
            return
        else:
            print("Invalid item number.")
            return
    except ValueError:
        # Not an integer, try by name
        idx = find_cart_index(choice)
        if idx is not None:
            removed = cart.pop(idx)
            print(f"Removed {removed['item']} from cart.")
        else:
            print("Item not found in cart.")

def clear_cart():
    """Clear all items from the cart after confirmation."""
    if not cart:
        print("Cart is already empty.")
        return
    confirm = input("Are you sure you want to clear the cart? (y/n): ").strip().lower()
    if confirm == "y":
        cart.clear()
        print("Cart cleared.")
    else:
        print("Clear cancelled.")

def checkout():
    """Display total and ask the user to finalize purchase (which clears cart)."""
    if not cart:
        print("Cart is empty.")
        return
    total = calculate_total()
    print(f"Your total bill is: {total:.2f}")
    confirm = input("Proceed to checkout and clear cart? (y/n): ").strip().lower()
    if confirm == "y":
        cart.clear()
        print("Checkout complete. Thank you for your purchase.")
    else:
        print("Checkout cancelled.")

def main():
    """Main loop for the shopping cart system."""
    menu = (
        "1. Show available items\n"
        "2. Add to cart\n"
        "3. View cart\n"
        "4. Remove item from cart\n"
        "5. Clear cart\n"
        "6. Checkout (show total and clear)\n"
        "7. Exit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            show_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            clear_cart()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Exiting. Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 7.")

if __name__ == "__main__":
    main()