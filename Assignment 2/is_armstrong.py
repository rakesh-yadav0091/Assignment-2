# This program defines a function that checks wheather a number is an Armstrong number or not.

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

# Input from user
num = int(input("Enter a number: "))

# Output result
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")