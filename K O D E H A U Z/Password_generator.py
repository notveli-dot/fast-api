import random
generator = True
while generator:
    print("Password Generator")
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ")
    use_numbers = input("Include numbers? (yes/no): ")
    use_special_chars = input("Include special characters? (yes/no): ")
    chars = 'abcdefghijklmnopqrstuvwxyz'
    if use_uppercase.lower() == "yes":
      chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers.lower() == "yes":
      chars += '0123456789'
    if use_special_chars.lower() == "yes":
      chars += '!@#$%^&*()_+-={}:<>?'
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password: " + password)
    break