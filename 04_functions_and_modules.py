import random

# Function basics

def greet(name):
    return f"Hello, {name}!"

print(greet("Zameer"))

# Keyword arguments

def describe(person, age):
    return f"{person} is {age} years old"

print(describe(age=21, person="Zameer"))

# Variable scope
value = 10

def change_value():
    global value
    value = 20

change_value()
print(value)

# *args and **kwargs

def print_items(*args, **kwargs):
    print(args)
    print(kwargs)

print_items(1, 2, 3, name="Zameer")

# String format
print("My name is {} and I am {} years old".format("Zameer", 21))

# Random number
print(random.randint(1, 10))

# Module example
# This file itself is a practice example of module-style grouping.
