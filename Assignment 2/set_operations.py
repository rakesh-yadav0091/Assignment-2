# This program performs set operations between two sets.

set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# Union
union_set = set1 | set2
print("Union length:", len(union_set))

# Intersection
print("Intersection:", set1 & set2)

# Symmetric Difference
print("Symmetric difference:", set1 ^ set2)

# Add 40 to set1
before = set1.copy()
set1.add(40)
print("Set changed after adding 40:", set1 != before)

# Remove 20 from set2
set2.discard(20)
print("Ste2 after removing 20:", set2)