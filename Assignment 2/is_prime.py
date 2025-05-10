# This program defines a function that checks wheather a number is prime or not.

def is_prime(n):
    if n <= 1:
        return False   # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number: "))

# Output result
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")