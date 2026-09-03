from functools import reduce

# Lambda
square = lambda x: x * x
print(square(5))

# Sort
nums = [4, 2, 7, 1]
print(sorted(nums))

# Map
mapped = list(map(lambda x: x * 2, nums))
print(mapped)

# Filter
filtered = list(filter(lambda x: x % 2 == 0, nums))
print(filtered)

# Reduce
product = reduce(lambda a, b: a * b, nums)
print(product)

# List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# Dictionary comprehension
pairs = {x: x * 2 for x in range(1, 4)}
print(pairs)

# Zip
names = ["Zameer", "Mahesh", "Pavan"]
ages = [21, 22, 23]
print(list(zip(names, ages)))
