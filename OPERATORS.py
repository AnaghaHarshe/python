OPERATORS IN PYTHON

# 1. Write a program to calculate the area and perimeter of a rectangle, given its length and width. Use the addition, multiplication, and subtraction operators.

length = float(input("Length of rectangle: "))
width = float(input("Width of rectangle: "))

area = length * width   # multiplication
print("Area of rectangle", area)

perimeter = 2 * (length + width)  # addition
print("Perimeter of rectangle", perimeter)

difference = length - width  # difference / substraction
print("Difference of rectangle", difference)


# 2. Write a program to increment the value of a variable by 5 using the addition assignment operator (+=).
a = int(input("Enter a number: "))
a +=5
print("After increment by 5:-",a)


# 3. Write a program to check if a specific character exists within a given string using the in operator.
s = input("Enter a string:")
ch = input("Enter a character:")

if ch in s:
    print("Given character is present in the string", ch)
else:
    print("Given character is not present in the string", ch)


# 4. Write a program to check if two variables refer to the same object in memory using the is operator.
identify operator
a = [1,2,3]
b = a        # both refer to same object
c = [1,2,3]  # new object with same values

print("a is b", a is b)  # True - same memory
print("a is c", a is c) # false - different memory


# 5.Write a program to compute the remainder when one number is divided by another using the modulus operator (%).
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

r = p % q
print("Reminder when", p,  "is divided by", q," then reminder is =", r)


# 6. Create a program that converts a given number of minutes into hours and minutes.
m = int(input("Enter minutes:"))
hours = m //60
minutes = m % 60
print("hours:",hours)
print("minutes:",minutes)


# 7. Develop a script that determines if a value exists in a predefined list of numbers.
num =[10, 20, 30, 40, 50]

value = int(input("Enter a number to search:-"))

if value in num:
    print("Found")
else:
    print("Not found")
