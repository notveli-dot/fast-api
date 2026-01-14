# Student Management System
# Goal: Build a program to store student names and their scores using lists/dictionaries.
# Core Features:
# - Add new students (with 3 subject scores)
# - Show all students with average and performance status
# - Search for a student by name
# - Use functions for actions
# - Use error handling for invalid inputs
# python
def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty. Try again.")
# This function `input_nonempty(prompt)` repeatedly asks the user for input until they type a non\-empty string (ignoring leading/trailing whitespace).
#
# Step\-by\-step:
# - Calls `input(prompt)` and immediately applies `.strip()` to remove surrounding whitespace.
# - If the stripped string is non\-empty (`if s:`) it is returned.
# - If empty, it prints `"Input cannot be empty. Try again."` and loops to prompt again.
#
# Result: the function always returns a trimmed, non\-empty string entered by the user.

def input_score(subject):
    # Prompt repeatedly for a numeric score for `subject` until a valid float between 0 and 100 is entered.
    #
    # Behavior:
    # - Prompts: uses `input` with `f"Enter score for {subject} (0-100): "` and strips whitespace.
    # - Parsing: converts the trimmed input to `float`; if conversion raises `ValueError`, informs the user and repeats.
    # - Validation: accepts and returns the value only if `0 <= score <= 100`; otherwise informs the user and repeats.
    #
    # Returns:
    # - A `float` in the inclusive range [0, 100].
    while True:
        try:
            val = input(f"Enter score for {subject} (0-100): ").strip()
            score = float(val)
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid number. Enter a numeric score.")

def performance_status(avg):
    if avg >= 85:
        return "Excellent"
    if avg >= 70:
        return "Good"
    if avg >= 50:
        return "Average"
    return "Poor"

def add_student(students):
    name = input_nonempty("Student name: ")
    key = name.lower()
    if key in students:
        print("Student already exists. Use a different name.")
        return
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    scores = [input_score(s) for s in subjects]
    students[key] = {"name": name, "scores": scores}
    print(f"Added student {name}.")

def show_all_students(students):
    #
    #     Display a formatted table of all students with their scores, average and performance.
    #
    #     Parameters:
    #     - students (dict): maps lowercase name -> {'name': original_name, 'scores': [float, ...]}
    #
    #     Behavior:
    #     - If `students` is empty, prints a message and returns.
    #     - Prints a header row and a divider.
    #     - For each student entry:
    #         - Computes average = sum(scores) / len(scores)
    #         - Determines status via `performance_status(avg)`
    #         - Formats scores with one decimal and average with two decimals
    if not students:
        print("No students available.")
        return
    print(f"{'Name':30} {'Scores':25} {'Average':7} {'Status'}")
    print("-" * 75)
    for entry in students.values():
        scores = entry["scores"]
        avg = sum(scores) / len(scores)
        status = performance_status(avg)
        scores_str = ", ".join(f"{s:.1f}" for s in scores)
        print(f"{entry['name']:30} {scores_str:25} {avg:7.2f} {status}")

def search_student(students):
    # Prompt for the student name and ensure it's non-empty
    name = input_nonempty("Search student name: ")
    # Keys in `students` are stored as lowercase names, so normalize input
    key = name.lower()
    # Try exact match first
    found = students.get(key)
    if not found:
        # If no exact match, try partial case-insensitive matching against stored keys
        matches = [v for k, v in students.items() if name.lower() in k]
        # If still nothing, inform the user and return early
        if not matches:
            print("Student not found.")
            return
        # If there are matches, pick the first match (could be extended to show all)
        found = matches[0]
    # Retrieve the student's scores
    scores = found["scores"]
    # Compute the average score
    avg = sum(scores) / len(scores)
    # Determine performance label using helper function
    status = performance_status(avg)
    # Print formatted student details
    print(f"Name: {found['name']}")
    for i, s in enumerate(scores, 1):
        # Each subject score shown with one decimal place
        print(f"  Subject {i}: {s:.1f}")
    # Average shown with two decimal places
    print(f"  Average: {avg:.2f}")
    # Performance status string
    print(f"  Status: {status}")

def main():
    # Initialize empty dictionary to store students.
    # Key: lowercase student name -> Value: {'name': original_name, 'scores': [...]}
    students = {}

    # Menu actions mapping: option -> (description, function)
    actions = {
        "1": ("Add new student", add_student),
        "2": ("Show all students", show_all_students),
        "3": ("Search student by name", search_student),
        "4": ("Exit", None),  # Exit has no handler function
    }

    # Main loop: show menu, read choice, execute corresponding action
    while True:
        print("\nStudent Management System")
        # Print each menu line using the description from actions
        for k, (desc, _) in actions.items():
            print(f"{k}. {desc}")

        # Read user choice and remove surrounding whitespace
        choice = input("Choose an option: ").strip()

        # Handle the explicit exit option
        if choice == "4":
            print("Exiting.")
            break

        # Look up the chosen action; returns None if key not found
        action = actions.get(choice)
        if not action:
            # Invalid menu selection: inform user and repeat loop
            print("Invalid choice. Try again.")
            continue

        # Call the selected action function, passing the students state
        # action is a tuple (description, function) so index 1 is the function
        action[1](students)

if __name__ == "__main__":
    main()