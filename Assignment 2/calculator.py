# This program defines arithmetic functions for calculator operations on two decimal numbers.

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"
def trunc_div(x, y): return x // y if y != 0 else "Cannot divise by zero"
def modulus(x, y): return x % y if y != 0 else "Cannot divide by zero"
def exponent(x, y): return x ** y

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Add:", add(a,b))
print("Subtract:", subtract(a, b))
print("Multiply:", multiply(a, b))
print("Divide:", divide(a, b))
print("Truncated division:", trunc_div(a, b))
print("Modulus:", modulus(a, b))
print("Exponent:", exponent(a, b))