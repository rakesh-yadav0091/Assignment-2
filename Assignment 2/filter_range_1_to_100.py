# This program accepts integers and stores only those between 1 and 100 in a list.

numbers = list(map(int, input("Enter integers separated by space: ").split()))
filtered =  [num for num in numbers if 1 <= num <= 100]
print("Filtered list:", filtered)