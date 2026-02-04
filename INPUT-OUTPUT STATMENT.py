# INPUT-OUTPUT STATMENT

#OUTPUT STATEMENT:-

# The print() statement
print("Hello")

# The print(string) statement
str = "Anagha"
print("Hello", str)


# The print(variable list) statement
a = 10
b = 20
print(a, b)

# The print(object) statement
lst = [1,2,3,4,5]
print(lst)

# The print("string", variable list) statement
p = "Anagha"
age = 22
print("Name", p, "Age ", age)


# The print(formatted string) statement
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Sum of {x} and {y} is {x+y}")


# INPUT STATEMENT:-

# Accepting single Input
name = input("Enter your name: ")
print("Hello", name)


# Accepting multiple Input in the same line
a, b = input("Enter two numbers: ").split()   # write value (5, 4)
print(a, b)
   # input() → reads the entire line as a string
   # split() → breaks the string at spaces and returns a list
   # Values are assigned to variables from left to right.


# Command Line Argument (For input statement)
# - Command line arguments are values passed while running the program from terminal, not during input().

import sys

Arguments: ['demo.py', '10', '20', '30']
a = sys.argv[1]
b = sys.argv[2]

print("First =", a)
print("Second =", b)
