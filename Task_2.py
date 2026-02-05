#INPUT OUTPUT STATEMENT

# 1. Take your name as input and print: Hello, <name>!
a= input("Enter a string: ")
print("Hello", a)


# 2. Input name and age, and print: "Hi <name>, you are <age> years old."
name= input("Enter a name: ")
age= input("Enter a age: ")
print("Hi", name, "you are", age, "years old")


# 3. Input a number and print its square.
num = int(input("Enter a number: "))
square = num * num
print(f"square of {num} is {square}")


# 4. Input first name and last name, and print full name.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name, last_name)


# 5. Input length and breadth, and print the area.
length = float(input("\nEnter length: "))
breadth = float(input("Enter breadth: "))
area= length * breadth
print("The area of the rectangle is:", area)


# 6. Input temperature in Celsius and convert to Fahrenheit
temp=int(input("\nEnter temperature: "))
fahrenheit=(temp*9/5)+32
print("The temperature in fahrenheit is: ", fahrenheit)


# 7. Input two numbers and print them after swapping.
a = int(input("\nEnter a number: "))
b = int(input("Enter another number: "))
temp = a
a = b
b = temp

print("After swapping:", a)
print("After swapping:", b)



# 8. Input principal, rate, and time, and print the simple interest
p = int(input("Principal amount: "))
r = float(input("Rate percent: "))
t = int(input("Time in years : ")) # take time in years

si = (p*r*t)/100
print("The total simple interest is:", si)
total_amount = (p + si)
print("The total amount is:", total_amount)


# 9. Input radius of a circle and print the circumference
radius = float(input("Enter radius: "))
pi = 3.14159
circumference = 2 * pi * radius
print("The circumference of the circle is:", circumference)


# 10. Input age and print whether the person is eligible to vote (18+).
age1 = int(input("Enter age: "))
if age1 >= 18:
    print("you are eligible")
else:
    print("you are not eligible")


# 11. Input a year and print whether it is a leap year.
year = int(input("Enter a year: "))

if year % 4 ==0 and year % 100 !=0 or year % 400 ==0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")


# 12. Input weight (kg) and height (m), and print the Body Mass Index.
weight = int(input("Enter a weight: "))
height = float(input("Enter a height: "))
bmi = weight / (height ** 2)
print("Body Mass Index is: ",bmi)


# 13. Write a Python program that takes input of names and marks of 5 students and stores them in a dictionary.Then display each student’s name along with their average marks.

students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = marks

print("\nStudent Average Marks")

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(name, ":", average)

# 14. Take a floating-point number as input and print it in: 2 decimal places, Scientific notation, Percentage format

number = float(input("Enter a number: "))

print("Scientific notation: {:.2e}".format(number))
print("Percentage: {:.2%}".format(number))
print("Two decimal places: {:.2f}".format(number))
