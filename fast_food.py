# WELCOME MESSAGE
from tarfile import OutsideDestinationError
customers = 0

print("Welcome to My Eatry")

while True:
  name = input("Please enter your name (or type 'quit' to exit): ").strip()
  if name.lower() == "quit":
      print("Thank you for visiting My Eatry")
      raise SystemExit

  # ORDER MESSAGE
  Burger = 5
  Fries = 2
  Drink = 1.5
  Burger_value = 0
  Fries_value = 0
  Drink_value = 0
  food_menu = "Burger $5\nFries $2\nDrink $1.5"

  program_exit = False
  while True:  # customer ordering loop (keeps asking menu until customer leaves or program exits)
      print("Hello", name, "What would you like to order\n", food_menu, "\nType 'done' to finish ordering for this customer or 'quit' to exit")
      order = input().strip().title()

      if order == "Burger":
          while True:
              try:
                  qty = int(input("How many Burgers do you need? "))
                  break
              except ValueError:
                  print("Please enter a valid number")
          Burger_value += qty
          print("Order confirmed \n", qty, "Burgers will be served shortly")
          reorder = input("Is that all you'd love to order? (Yes/No) ").strip().lower()
          if reorder == "no":
              continue

      elif order == "Fries":
          while True:
              try:
                  qty = int(input("How many Fries do you need? "))
                  break
              except ValueError:
                  print("Please enter a valid number")
          Fries_value += qty
          print("Order confirmed \n", qty, "Fries will be served shortly")
          reorder = input("Is that all you'd love to order? (Yes/No) ").strip().lower()
          if reorder == "no":
              continue

      elif order == "Drink":
          while True:
              try:
                  qty = int(input("How many Drinks do you need? "))
                  break
              except ValueError:
                  print("Please enter a valid number")
          Drink_value += qty
          print("Order confirmed \n", qty, "Drinks will be served shortly")
          reorder = input("Is that all you'd love to order? (Yes/No) ").strip().lower()
          if reorder == "no":
              continue

      elif order.lower() == "done":
          # proceed to billing
          pass
      elif order.lower() == "quit":
          print("Thank you for visiting My Eatry")
          program_exit = True
          break
      else:
          print("Item not available, please choose from the menu")
          continue

      # Billing
      print("Your bill will be ready shortly")
      bill = (Burger_value * Burger) + (Fries_value * Fries) + (Drink_value * Drink)
      print("Your total bill is $", bill)

      # After billing: allow adding more items for same customer, move to next customer, or quit
      next_action = input("Press Enter to continue ordering for the same customer, type 'next' for next customer, or 'quit' to exit: ").strip().lower()
      if next_action == "quit":
          print("Thank you for visiting My Eatry")
          customers += 1
          print("Total customers served today:", customers)
          program_exit = True
          break
      elif next_action == "next":
          customers += 1
          break  # leave inner loop; outer loop should ask name again
      else:
          # continue ordering for same customer; menu will be shown again and item counts are preserved
          continue

  if program_exit:
      raise SystemExit

  # request next customer's name (outer loop continues in original file)
  print("Total customers served today:", customers)

