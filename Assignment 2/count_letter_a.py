# This program counts how many times the letter 'a' appears in a list of names.

names = input("Enter names separated by commas: ").split(",")
joined = "".join(names).lower()
count_a = joined.count('a')
print("The letter 'a' appears", count_a, "times.")