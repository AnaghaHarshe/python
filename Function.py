#FUNCTIONS IN PYTHON

# Defining a Functions
# A function in python is block of reusable code that performs a specific task. functions help make
# programs organized, readable, and reusable.

# syntax
def function_name(parameter):
    # function body
    return parameter #(parameter is value)

#def - keyword to define a function
#function_name - name of the function
#parameter - inputs(optional)

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Calling a Function  -- after defining a function, you must call it to execute the code inside it.

# Syntax
# function_name(agrumentes)

def greet():
    print("Hello Welcome!")

greet()  #calling function

def greet2():
    print("Hello Anagha")
greet2()
greet2()
greet2() # calling function multiple times

def greet(name):
    print("Hello",name)
user_name = input("Enter your name: ")
greet(user_name)


# calling function inside another function

def massage():
    print("Learning python function")
def call_Massage():
    massage()
    print("calling function inside another function")
call_Massage()
#------------------------------------------------------------------------------------------------------------------------------------------------

# Returning Results from a Function

def add(p,q):
    return p+q
result = add(3, 4)
print(result)

# M2
def text(name):
    return "Hello "+ name

msg = text("Anagha")
print(msg)
#------------------------------------------------------------------------------------------------------------------------------------------------

#Returning Multiple Values from a Function

def operations(a, b):
    return a + b, a-b, a * b

num1 = int(input("Enter first number:"))
num2 = int(input("enter second number:"))

result, result2, result3 = operations(num1, num2)
print("Sum:", result)
print("Sub:", result2)
print("Multiplication:", result3)

# M2 calling string

def text(name):
    return "Hello " + name

t1 = input("Enter a text:")
print(text(t1))

#------------------------------------------------------------------------------------------------------------------------------------------------

# Functions are First Class Objects:- Function as variable, Function inside function, Function as argument, Function returns function

# 1. Function as variable

def greet(name):
    return "Hello " + name

massage = greet
print(massage("Anagha"))


# 2. function inside function

def outer():
    print("This is Outer function")

    def inner():
        print("This is Inner function")

    inner()

outer()


# 3. Function as argument
def add(a, b):
    return a + b
def operate(func, x, y):
    return func(x, y)

print(operate(add, 4, 6))


# 4. Function returns function
def outer():
    def inner():
        print("Inner function called ")
    return inner() # return function, NOT inner()

# func = outer()  # func now stores the inner function
# func()   # calling inner function

#------------------------------------------------------------------------------------------------------------------------------------------------
# Formal and Actual Arguments:- Positional, Keyword, Default, Variable length

def add(s,t):   # S & t are formal args
    return s + t
sum = add(5, 3)   #5 & 3 are actual ars
print(sum)


# 1 Positional ags
def student(name, age):
    print("Name: ",name)
    print("Age: ",age)
student("Anagha", 21)

# Keyword agrs

def stud(name, age):
    print("Name:",name)
    print("Age:",age)
stud(age=22, name="Ankita")

#3. Default args
def greet(name="Guest"):
    print("Hello "+name)
greet("Anagha")
greet()


# 4 variable - Length Arguments

#(a) *args – Non-keyword Variable Length
def add(*numbers):
    print(numbers)
    total = sum(numbers)
    print(total)

add(1, 2, 3, 4, 5)

#(b) **kwargs – Keyword Variable Length
def students(**details):
    print(details)
students(name="Anagah", age=22, course="AI")


def demo(a, b=10, *args, **kwargs):
    print("a:",a)
    print("b:",b)
    print("args:",args)
    print("kwargs:",kwargs)
demo(5, 20, 30, 40, name ="Ankita", age =22)

#------------------------------------------------------------------------------------------------------------------------------------------------
# Local and Global Variables

#1. Local variable

def myfunction():
    x = 10  #Local
    print("Inside function:",x)
myfunction()


#❌ Accessing Outside (Error)
def my_function():
    x = 20
my_function()
print(x)


# 2. Global variables

x=50  # this variable is run for both inside and outside function
def show():
    ##x = 50  # here show error for outside function
    print("Inside function:",x)

show()
print("Outside function:",x)


# 3️. Local vs Global Example
x = 40

def demo():
    x = 20
    print("local:",x)

demo()
print("global:",x)


# 4️. Modifying Global Variable Inside Function
#y = 10
#def demo2():
#    x = x + 5
#    print(x)
#demo2()    ## UnboundLocalError


y = 10
def demo2():
    global y
    y = y + 5
    print("Inside function",y)
demo2()
print("Outside function",y)

# 6. Final Example (Interview Favorite)

s = 40
def demo3():
    global s
    s = 50
    p = 20
    print("Inside function",s,p)

demo3()
print("Outside function",s)

#------------------------------------------------------------------------------------------------------------------------------------------------
# Recursive Functions

# Basic Structure of Recursion

# def function_name(parameters):
#     if base_condition:
#        return result
#     else:
#      return function_name(smaller_problem)


# factorial num

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
num = int(input("Enter a number: "))
print(f"Factorial of {num} is :",fact(num))

#------------------------------------------------------------------------------------------------------------------------------------------------
# Function Decorators

## Basic Decoder example
def decorator_func(original_fun):
    def wrapper():
        print("Before function execution")
        original_fun()
        print("After function execution")
    return wrapper

def say_hello():
    print("Hello !")

#Applying decorator manually
decorated = decorator_func(say_hello)
decorated()


# 2 ️. Using @ Decorator Syntax (Pythonic Way) -Instead of calling manually, we use @ symbol.
def decorator_fun(original_func):
    def wrapper():
        print("before execution")
        original_func()
        print("After execution")
    return wrapper

@decorator_fun
def say_hello():
    print("Hello!")
say_hello()

#------------------------------------------------------------------------------------------------------------------------------------------------
#Generators

# Normal function  VS  General function
#def normal_func():  |  def gen_func():
#   return 1         |      yield 1
#   return 2         |      yield 2


#1️ Basic Generator Example
def simple_generator():
    yield 1
    yield 2
    yield 4

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))


# 2️. Using Generator with Loop
def count_up_to(n):
    for i in range(1, n+1):
        yield i

for num in count_up_to(6):
    print(num)

# Example: Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

#------------------------------------------------------------------------------------------------------------------------------------------------
# Anonymous Functions or Lambdas

add = lambda a,b: a+b
n1 = int(input("Enter 1st num:"))
n2 = int(input("Enter 2nd num:"))
print("Addition:",add(n1,n2))

# 2️ Lambda with One Argument
square = lambda x: x * x
n3 = int(input("Enter value:"))
print(f"Square of {n3} is",square(n3))

#------------------------------------------------------------------------------------------------------------------------------------------------
# Using Lambdas with filter() Function

numbers = [1,2,3,4,5,6,7,8,9,10]

even_num = list(filter(lambda x: x % 2 == 0, numbers))
print(even_num)
odd_num = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_num)


# Filter Strings with Length > 4
names = ["Anagha", "Ankita", "Riya", "Amita", "Arohi" ]
long_names = list(filter(lambda names: len(names) >1,names))
print(long_names)

#------------------------------------------------------------------------------------------------------------------------------------------------
# Using Lambdas with map() Function
names = ["anagha", "Ankita", "Arohi"]

upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)

#------------------------------------------------------------------------------------------------------------------------------------------------
# Using Lambdas with reduce() Function

from functools import reduce

numbers = [1,2,3,4,5]
result = reduce(lambda x, y: x+y, numbers)
print(result)

#Find Maximum Value
from functools import reduce
nums = [10, 25, 7, 40, 15]
maximum = reduce(lambda a,b: a if a>b else b, nums)
print(maximum)

# All map, filter, reduce functions
from functools import reduce

nums = [1, 2, 3, 4]

mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
reduced = reduce(lambda x, y: x + y, nums)

print(mapped)   # [2, 4, 6, 8]
print(filtered) # [2, 4]
print(reduced)  # 10
#------------------------------------------------------------------------------------------------------------------------------------------------
#Structured Programming
#Structured programming is a programming paradigm that organizes code into well-defined control structures such as sequence,
# selection, and iteration, promoting clarity, modularity, and maintainability of programs.
