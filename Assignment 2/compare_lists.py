# This program compares two lists on length, sum, and common elements.

list1 = list(map(int, input("Enter integers for list 1: ").split()))
list2 = list(map(int, input("Enter integers for list 2: ").split()))

print("Same length:", len(list1) == len(list2))
print("Same sum:", sum(list1) == sum(list2))
print("Common elements:", set(list1) & set(list2))