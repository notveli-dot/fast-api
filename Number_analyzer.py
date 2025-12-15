# Number Analyzer
# Scenario: Build a tool to analyze numbers entered by the user.
# Instructions:
# - Let the user enter up to 5 numbers (use a loop).
# - For each number:
#    - Check if it's even or odd.
#    - Check if it's positive, negative, or zero.
#    - Print the result for each.
# - After all entries, show how many:
#    - Were even
#    - Were odd
#    - Were negative
#    - Were zero
even_count = 0
odd_count = 0
negative_count = 0
zero_count = 0
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Check even or odd
    if num % 2 == 0:
        print(f"{num} is Even.")
        even_count += 1
    else:
        print(f"{num} is Odd.")
        odd_count += 1

    # Check positive, negative, or zero
    if num > 0:
        print(f"{num} is Positive.")
    elif num < 0:
        print(f"{num} is Negative.")
        negative_count += 1
    else:
        print(f"{num} is Zero.")
        zero_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
print("Negative numbers count:", negative_count)
print("Zero count:", zero_count)
