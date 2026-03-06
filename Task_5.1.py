#Demonstrate scope of inner and outer functions.
def outer_function():
    x = 10

    def inner_function():
        y = 5
        print("Inside inner function:")
        print("X = ", x)
        print("Y = ", y)

    inner_function()

    print("Inside outer function:")
    print("X =",x)

outer_function()

#-------------------------------------------------------------------------------------------------
# Pass a function as an argument to another function.
def add(a, b):
    return a + b
def operate(func, x, y):
    return func(x, y)

print(operate(add, 4, 6))

#-------------------------------------------------------------------------------------------------
# Write a calculator function that accepts operation functions.
#Use returned functions for custom operations.
#Return different functions based on conditions.


def calculator(a,b, operation):
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def multi(a,b):
        return a * b
    def divide(a,b):
        return a / b

    if operation == "+":
        return add(a,b)
    elif operation == "-":
        return sub(a,b)
    elif operation == "*":
        return multi(a,b)
    elif operation == "/":
        return divide(a,b)
    else:
        return "Invalid operation"

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
op = input("Enter operation(+, -, *,/) =")

result = calculator(num1, num2, op)
print("Result", result)


#-------------------------------------------------------------------------------------------------
#Use a function as a callback.

def demo(name):
    print("Hello", name)
def process_user(callback):
    name = input("Enter name:")
    callback(name)

process_user(demo)

#-------------------------------------------------------------------------------------------------
#Apply a function to each element of a list.

def square(num):
    return num * num

numbers = list(map(int, input("Enter numbers separated by space:").split()))

result = list(map(square, numbers))

print("original list:",numbers)
print("Square list:",result)

#-------------------------------------------------------------------------------------------------
#Create a custom function executor.
def executor(func, value):
    return func(value)

def square(num):
    return num * num

def cube(num):
    return num ** 3

number = int(input("Enter a number:"))
choice = input("choose operation(Square / cube):")

if choice == "square":
    result = executor(square, number)
elif choice == "cube":
    result = executor(cube, number)
else:
    result = "Invalid choice"

print("Result:", result)

#-------------------------------------------------------------------------------------------------
#Write a function that returns another function.
def out_func():
    def inner_func():
        print("Hello from inner function!")

    return inner_func
my_func = out_func()

my_func()

#-------------------------------------------------------------------------------------------------
#Create a multiplier function generator.
def multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

factor = int(input("Enter multiplier factor:"))
number = int(input("Enter number to multiply:"))

multiply_func = multiplier(factor)

result = multiply_func(number)

print("Result:",result)

#-------------------------------------------------------------------------------------------------
#Demonstrate closures using returned functions.

def outer(message):
    def inner():
        print("Message:", message)
    return inner

msg = input("Enter a message:")
my_function = outer(msg)

my_function()

#-------------------------------------------------------------------------------------------------
#Write a function using positional arguments.
def info(name, age):
    print("Name:", name)
    print("Age:", age)

name = input("Enter your name:")
age = input("Enter your age:")
info(name, age)

#-------------------------------------------------------------------------------------------------
#Demonstrate error when order of arguments changes.

def divide(a, b):
    return a / b

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

result1 = divide(num1, num2)
print("Correct order result:", result1)

result2 = divide(num2, num1)
print("Changed order result:", result2)

#-------------------------------------------------------------------------------------------------
#Write a function using keyword arguments. - order not matter
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

# Taking input from user
n = input("Enter name: ")
a = int(input("Enter age: "))
c = input("Enter course: ")


student_info(name=n, age=a, course=c)


#-------------------------------------------------------------------------------------------------
#Mix positional and keyword arguments.

def employee_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

n = input("Enter name: ")
a = int(input("Enter age: "))
d = input("Enter department: ")
 #Rule: Positional arguments must come before keyword arguments.
employee_info(n, age=a, department=d)

#-------------------------------------------------------------------------------------------------
#Write a function with default parameter values.

def calculate_bill(amount, tax=5):  #tax=5 is a default parameter.
    total = amount + (amount * tax / 100)
    print("Total bill:", total)

price = float(input("Enter amount:"))

calculate_bill(price)

tax_value = int(input("Enter tax percentage:"))
calculate_bill(price, tax_value)

#-------------------------------------------------------------------------------------------------
#Override default argument values.

def calculate_discount(price, discount = 10):
    final_price = price - (price * discount / 100)
    print("final_price:", final_price)

p = float(input("Enter product price:"))

calculate_discount(p)

d = float(input("Enter discount percentage:"))
calculate_discount(p,d)

#-------------------------------------------------------------------------------------------------
#Write a function using *args.
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sun:",total)

numbers = list(map(int, input("Enter numbers separated by space:").split()))

add_numbers(*numbers)


#-------------------------------------------------------------------------------------------------
#Write a function using **kwargs.

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key, ":", value)

name = input("Enter name:")
age = input("Enter age:")
course = input("Enter course:")

student_info(name = name,course = course, age = age)

#-------------------------------------------------------------------------------------------------
#Combine *args and **kwargs.
def display_info(*args, **kwargs):
    print("\nPositional arguments:-")
    for arg in args:
        print(arg)

    print("Keyword arguments:-")
    for key, value in kwargs.items():
        print(key,":",value)

name = input("Enter name:")
age = int(input("Age:"))
city = input("Enter city:")

display_info(name, age, city, course = "python", year = "2026")

#-------------------------------------------------------------------------------------------------
#Create a function that accepts any number of inputs.

def show_numbers(*numbers):
    for num in numbers:
        print(num)

nums = list(map(int,input("Enter numbers separated by comma:").split()))

show_numbers(*nums)

#-------------------------------------------------------------------------------------------------
#Demonstrate local variable scope.

def show_number():
    num = 10   # Local variable
    print("Number inside function:", num)

show_number()

#print(num)   # This will give an error

#-------------------------------------------------------------------------------------------------
#Demonstrate global variable access.

num = 20   # Global variable

def show_number():
    print("Number inside function:", num)

show_number()

print("Number outside function:", num)

#-------------------------------------------------------------------------------------------------
#Modify a global variable inside a function.

count = 0

def update_count():
    global count
    count = count + 1
    print("Count inside function", count)

update_count()

print("Count outside function", count)

#-------------------------------------------------------------------------------------------------
#Create name conflict between local and global variables.

num = 50   # Global variable

def show_value():
    num = 20   # Local variable with same name
    print("Value inside function:", num)

show_value()

print("Value outside function:", num)

#-------------------------------------------------------------------------------------------------
#Use the global keyword properly.

total = 10
def update_total():
    global total
    total = total + 10
    print("Total inside function:", total)

update_total()
print("Total outside function:", total)

#-------------------------------------------------------------------------------------------------
#Write a recursive function to calculate factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int (input("Enter a number:"))

result = factorial(num)
print(f"Factorial of {num} is:",result)

#-------------------------------------------------------------------------------------------------
#Write a recursive function for Fibonacci series.
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("Enter a number:"))
for i in range(1, num+1):
    print(fibonacci(i), end = " ")


#-------------------------------------------------------------------------------------------------
#Calculate sum of digits using recursion.

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)    #recursive call

num = int(input("Enter a number:"))
print("Sum of digits",sum_digits(num))


#-------------------------------------------------------------------------------------------------
#Reverse a string using recursion.

def reverse_str(s):
    if len(s) == 0:
        return s
    else:
        return  reverse_str(s[1:]) + s[0]

text = input("Enter a sting:")
print(reverse_str(text))

#-------------------------------------------------------------------------------------------------
#Find GCD of two numbers using recursion.
#gcd(48,18) = gcd(18,48 % 18 = 12) = gcd(12, 18 % 12 = 6) gcd(6,12 % 6 = 0)

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

result = gcd(num1, num2)
print("GCD: ",result)

#-------------------------------------------------------------------------------------------------
#Create a decorator to print function execution start and end.

def execution_decorator(func):
    def wrapper():
        print("Function execution started")
        func()
        print("Function execution finished")

    return wrapper()

@execution_decorator
def my_function():
    print("Inside the function")

my_function()

#-------------------------------------------------------------------------------------------------
#Write a decorator to measure execution time.

import time
def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper

@execution_time
def sample_function():
    for i in range(1000000):
        pass

sample_function()

#-------------------------------------------------------------------------------------------------
#Create a decorator to validate user input.

def vali_input(function):
    def wrapper(num):
        if num < 0:
            print("Invalid Input")
        else:
            return function(num)
    return wrapper

@vali_input
def print_num(num):
    print("You entered:",num)
num = int(input("Enter a number:"))

print_num(num)

#-------------------------------------------------------------------------------------------------
#Write a decorator for authentication simulation.

def authentication(func):
    def wrapper(username, password):
        if username == "Anagha" and password == "1234":
            print("Authentication Successful")
            func()
        else:
            print("Authentication failed")
    return wrapper

@authentication
def access_system():
    print("Access granted to the system")

access_system("Anagha","1234")
access_system("user", "1111")

#-------------------------------------------------------------------------------------------------
#Apply multiple decorators to a function.

import time

def start_end(func):
    def wrapper():
        print("function started")
        func()
        print("Function ended")
    return wrapper

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return wrapper

@start_end
@measure_time
def task():
    for i in range(1000000):
        pass
task()

#-------------------------------------------------------------------------------------------------
#Create a generator to generate numbers from 1 to n.

def generator_num(n):
    for i in range(n):
        yield i
n = int(input("Enter a number:"))

for num in generator_num(n):
    print(num)
#-------------------------------------------------------------------------------------------------
#Write a generator for Fibonacci numbers.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a #yield returns one Fibonacci number at a time.
        a, b = b, a + b

n = int(input("Enter number: "))

for num in fibonacci(n):
    print(num)

#-------------------------------------------------------------------------------------------------
#Generate even numbers using a generator.
def even(n):
    for i in range(2, n+1, 2): #range(2, n+1, 2) generates numbers starting from 2 with step 2.
        yield i

n = int(input("Enter a  number:"))

for num in even(n):
    print(num)

#-------------------------------------------------------------------------------------------------
#Compare generator vs list memory usage.

import sys

numbers_list = [i for i in range(10000)]

numbers_gen = (i for i in range(10000))

print("Memory used by list:", sys.getsizeof(numbers_list))
print("Memory used by generator:", sys.getsizeof(numbers_gen))

#-------------------------------------------------------------------------------------------------
#Use yield inside a loop.

def num_generator(n):
    for i in range(1, n+1):
        yield i    #ield inside a loop = produce values step-by-step during iteration.

n = int(input("Enter a number: "))

for num in num_generator(n):
    print(num)

#-------------------------------------------------------------------------------------------------
#Write a lambda to add two numbers.

add = lambda x, y: x + y

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

result = add(a, b)
print("Sum:",result)

#-------------------------------------------------------------------------------------------------
#Write a lambda to find square of a number.

square = lambda x: x * x
num = int(input("Enter a number: "))
print(f"Square of {num} is:",square(num))

#-------------------------------------------------------------------------------------------------
#Use lambda to sort a list of tuples.

data = [(1,9), (2,8), (3,7), (4,6)]
data.sort(key= lambda x : x[1])   #key=lambda x: x[1] tells Python to sort based on that element.

print("Sorted list", data)

#-------------------------------------------------------------------------------------------------##Replace a simple function with lambda.
#Store lambda in a variable.

multiply = lambda x, y: x * y

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = multiply(a, b)
print("Multiplication:", result)

#-------------------------------------------------------------------------------------------------
#Square all numbers in a list.

num = list(map(int, input("Enter num separated by space:- ").split()))

squares = list(map(lambda x: x ** 2, num))

print("Squared numbers:", squares)


#-------------------------------------------------------------------------------------------------
#Convert list of strings to uppercase.

str = input("Enter a string:- ")

up_case = str.upper()
print("Uppercase string:", up_case)

#-------------------------------------------------------------------------------------------------
#Apply GST calculation using map().

amounts = list(map(float, input("Enter amounts separated by space: ").split()))

gst_percent = float(input("Enter GST percentage: "))

gst_prices = list(map(lambda x: x + (x * gst_percent / 100), amounts))

print("Prices after GST:", gst_prices)


#-------------------------------------------------------------------------------------------------
#Convert Celsius list to Fahrenheit.

celsius_list = list(map(float, input("Enter Celsius values separated by space: ").split()))

fahrenheit_list = list(map(lambda c: (c * 9/5) + 32, celsius_list))

print("Fahrenheit values:", fahrenheit_list)

#-------------------------------------------------------------------------------------------------
#Add corresponding elements of two lists.

list1 = list(map(int, input("Enter elements of first list: ").split()))

list2 = list(map(int, input("Enter elements of second list: ").split()))

result = list(map(lambda x, y: x + y, list1, list2))

print("Result:", result)

#-------------------------------------------------------------------------------------------------
#Find sum of all elements using reduce().

from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = reduce(lambda x, y: x + y, numbers)

print("Sum of elements:", total)

#-------------------------------------------------------------------------------------------------
#Create a structured program for student management.
students = []


# Add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {"Name": name, "Roll": roll, "Marks": marks}
    students.append(student)
    print("Student added successfully!\n")


# Display students
def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for s in students:
            print(s)
        print()


# Search student
def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["Roll"] == roll:
            print("Student found:", s, "\n")
            return
    print("Student not found.\n")


# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")


# Main menu
while True:
    print("---- Student Management System ----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Try again.\n")
