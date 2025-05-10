# This program performs multiple dictionary operations.

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = { 5:50, 6:60}

# Concatenate dictionaries
nums = {**dic1, **dic2, **dic3}

#Add new pair
nums[7] = 70

# Update key 3
nums[3] = 80

# Remove third item
if len(nums) >= 3:
    key_to_remove = list(nums.keys())[2]
    nums.pop(key_to_remove)

# Sum, Product, Max, Min
print("Sum:", sum(nums.values()))

product = 1
for v in nums.values():
    product *= v
print("Product:", product)

print("Max:", max(nums.values()))
print("Min:", min(nums.values()))