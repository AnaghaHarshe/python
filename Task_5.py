#Define a function to print “Hello, World”.
def hello():
    print("Hello World")
hello()

-------------------------------------------------------------------------------------------------
#Define a function to calculate the square of a number.

def square():
    n1 = int(input("Enter a number:"))
    return n1 * n1
print(square())
from IPython.testing.tools import help_all_output_test


#-------------------------------------------------------------------------------------------------
# Define a function to find the maximum of two numbers.

def max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter 1st num:"))
num2 = int(input("Enter 2nd num:"))

result = max(num1, num2)
print("Maximum number is:",result)

#-------------------------------------------------------------------------------------------------
# Define a function to check whether a number is even or odd.
def check_num(n):
    if n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

number = int(input("Enter number to check:"))
check_num(number)

#-------------------------------------------------------------------------------------------------
# Define a function to calculate the area of a circle.

import math
def cal_areaC(r):
    area = math.pi * r * r
    return area

r = float(input("Eneter radius:"))
result = cal_areaC(r)
print(f"Area of Circle whose radius {r} is ",result)

#-------------------------------------------------------------------------------------------------
# Write a function to add two numbers and call it from the main program.

def add_num(a, b):
    return a+b
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
result = add_num(num1, num2)
print(f"Sum of {num1} and {num2} is:",result)

#-------------------------------------------------------------------------------------------------
# Define a function to convert Celsius to Fahrenheit and call it.

def temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temp_C = float(input("Enter temp in Celsius: "))
temp_f = temp(temp_C)

print("Temperature in Fahrenheit:", temp_f)

#-------------------------------------------------------------------------------------------------
# Call a function multiple times with different inputs.
def greet(name):
    print("Hello",name,"!")
greet("Anagha")
greet("Ankita")
greet("Amita")
greet("Arohi")

#-------------------------------------------------------------------------------------------------
# Write a function and call it inside a loop.
def square(num):
    print("Square of", num,"is", num * num)
for i in range(1, 11):
    square(i)

#-------------------------------------------------------------------------------------------------
# Call one function from another function.
def func_one(name):
    print("Hello,", name)

def func_two():
    user_name = input("Enter your name:")
    func_one(user_name)

func_two()


#-------------------------------------------------------------------------------------------------
# Write a function that returns the sum of two numbers.

def sum(a, b):
    return a + b

a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))

result = sum(a, b)
print("Sum ", result)
#-------------------------------------------------------------------------------------------------
# Write a function that returns whether a number is prime.

def prime(num):
    if num <=1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter number:"))
if prime(n):
    print("Prime")
else:
    print("Not prime")

#-------------------------------------------------------------------------------------------------
# Create a function that returns the factorial of a number.

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
num = int(input("Enter a number: "))
print(f"Factorial of {num} is :",fact(num))

#-------------------------------------------------------------------------------------------------
# Write a function that returns the length of a string.

def len_str(s):
    return len(s)
text = input("Enter a string:")
result = len_str(text)
print(result)

#-------------------------------------------------------------------------------------------------
# Write a function that returns the largest element in a list.

def larg_ele(lst):
    return max(lst)

number = list(map(int, input("Enter a number by space: ").split()))
print("List of numbers:",number)
result = larg_ele(number)
print("Max num from list",result)

#-------------------------------------------------------------------------------------------------
# Write a function that returns sum and average of numbers.

def sum_avg(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

nums = list(map(int, input("Enter a number by space: ").split()))
total, avg = sum_avg(nums)

print("Sum=",total)
print("Average=",avg)
#-------------------------------------------------------------------------------------------------
# Create a function that returns quotient and remainder.

def qout_remin(a, b):
    quotient = a//b
    reminder = a%b
    return quotient, reminder

num1 = int(input("Enter divident:"))
num2 = int(input("Enter divisor:"))

q, r = qout_remin(num1, num2)
print("Quotient",q)
print("Reminder",r)

#-------------------------------------------------------------------------------------------------
# Write a function that returns min and max from a list.

def elements(lst):
    return max(lst),min(lst)

number = list(map(int, input("Enter a number by space: ").split()))
print("List of numbers:",number)
max_num, min_num = elements(number)
print("Max num from list",max_num)
print("Min num from list",min_num)

#-------------------------------------------------------------------------------------------------
# Return both uppercase and lowercase versions of a string.

def str(s):
    return s.upper(), s.lower()

string = input("Enter a string:")
upper, lower = str(string)

print("Upper case string",upper)
print("Lower case string",lower)

#-------------------------------------------------------------------------------------------------
# Write a function that returns area and perimeter of a rectangle.

import math
def rectangle(length, width):
    area = length * width
    perimeter = 2 *(length + width)
    return area, perimeter

l = int(input("Enter a length:"))
w = int(input("Enter a width:"))

area, perimeter = rectangle(l, w)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

#-------------------------------------------------------------------------------------------------
# Assign a function to a variable and call it.

def greet(name):
    return "Hello " + name

say_hello = greet  # Assign function to variable
print(say_hello("Anagha")) #calling function using new variable

#-------------------------------------------------------------------------------------------------
# Store multiple functions in a list and call them.

def add(a, b):
    return "Addition:", a + b
def substract(a, b):
    return "Substraction", a - b
def multiply(a, b):
    return "Multipication:", a * b

operations =[add, substract, multiply]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for func in operations:
    print(func(num1, num2))

#-------------------------------------------------------------------------------------------------
# Pass a function reference without parentheses.
def greet():
    print("Passing function without parentheses.")

def call_function(func):
    func()
call_function(greet)

#-------------------------------------------------------------------------------------------------
# Swap two function references.

def hello():
    return "Hello"
def goodbye():
    return "Goodbye"

func1 = hello
func2 = goodbye

func1, func2 = func2, func1

print(func1())
print(func2())
#-------------------------------------------------------------------------------------------------
# Check the type of a function variable. Assign a function to a variable and call it.

def greet(name):
    return "Hello " + name

my_function = greet

print("Type of My_function", type(my_function))

print(my_function("Anagaha"))

#-------------------------------------------------------------------------------------------------
# Write a function inside another function.
def outer_func():
    print("outer_function")

    def inner_func():
        print("Inner function")

    inner_func()
outer_func()

#-------------------------------------------------------------------------------------------------
#Access an inner function from an outer function.

def out_func():
    print("outer function called")

    def inner_func():
        return "Inner function called"

    return inner_func

my_function = out_func()

print(my_function())

#-------------------------------------------------------------------------------------------------
#Create a nested function to validate input.

def get_num():
    def is_positive(num):
        return num > 0      #inner function
    number = int(input("Enter a number:"))

    if is_positive(number):
        print("Valid input! Number is positive.")

    else:
        print("Invalid input! Number is negative.")

get_num()

#-------------------------------------------------------------------------------------------------
# Write a function that uses an inner helper function.

def calc_square(number):

    def helper(num):
        return num * num

    result = helper(number)
    print("Square is:", result)

calc_square(5)
