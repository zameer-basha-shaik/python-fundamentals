# Simple condition example
if 18 >= 18:
    print("Adult")
else:
    print("Minor")

# While loop
count = 0
while count < 5:
    print("count =", count)
    count += 1

# For loop
for i in range(1, 6):
    print(i)

# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Break statement
for num in range(1, 11):
    if num == 5:
        break
    print(num)

# Continue statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Pass statement
for letter in "abc":
    if letter == "b":
        pass
    print(letter)
