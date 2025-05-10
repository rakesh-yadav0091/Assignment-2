# This program defines a function that counts the number of uppercase and lowercase letters in a string.

def count_case(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

# Ask user for input
user_input = input("Enter a string: ")
uppercase, lowercase = count_case(user_input)

# Output the result
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)