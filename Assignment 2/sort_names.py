# This program accepts a list of names and returns the sorted order of names.

def sort_names(name_list):
    return sorted(name_list)

names = input("Enter names separated by commas: ").split(",")
sorted_list = sort_names(names)
print("sorted names:", sorted_list)