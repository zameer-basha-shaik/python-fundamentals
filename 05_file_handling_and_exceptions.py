import os

# Exception handling
try:
    num = int(input("Enter a number: "))
    print(1 / num)
except ValueError:
    print("Only numbers!")
except ZeroDivisionError:
    print("Can't divide by 0")
except Exception:
    print("Something went wrong")
else:
    print("Success")
finally:
    print("Done!")

# File detection
filepath = "test.txt"
if os.path.exists(filepath):
    print("File exists")
if os.path.isfile(filepath):
    print("This is a file")

# Write file
with open("demo_output.txt", "w") as file:
    file.write("This is written from the learning repository.\n")

# Read file
with open("demo_output.txt", "r") as file:
    content = file.read()
    print(content)

# Copy file example
# This is intentionally minimal and kept aligned to the course content.
