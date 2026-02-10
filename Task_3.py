# #1. Check whether a number is positive, negative, or zero.

# num = int(input("Enter a number: "))
#
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Number is zero")

##---------------------------------------------------------------------------

## 2. Check whether a given number is even or odd.

# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

##---------------------------------------------------------------------------------------------

## 3. Check whether a person is eligible to vote (age ≥ 18).

# age = int(input("Enter age number: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


##--------------------------------------------------------------------------------
## 4. Find the greater of two numbers.

# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))
# if a > b:
#     print("Greater number is ", a)
# elif a < b:
#     print("Greater number is ", a)
# else:
#     print("Both numbers are equal")

##--------------------------------------------------------------------------------

## 5. Check whether a number is divisible by 5.
# p = int(input("Enter a number: "))
# if p % 5 == 0:
#     print(p, "is divisible by 5")
# else:
#     print(p, "is not divisible by 5")

##--------------------------------------------------------------------------------

## 6. Check whether a character is a vowel or consonant.
# c = input("Enter character: ")
# if c in "aeiouAEIOU":
#     print("vowels")
# else:
#     print("consonants")

##--------------------------------------------------------------------------------

## 7. Check whether a year is a leap year.
# year = int(input("Enter year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

##--------------------------------------------------------------------------------

## 8. Check whether a student has passed or failed (pass ≥ 40).
# marks = int(input("Enter marks: "))
#
# if marks >= 40:
#     print("Student is PASSED")
# else:
#     print("Student is FAILED")

##--------------------------------------------------------------------------------

## 9. Check whether a number is a multiple of both 3 and 7.
# d = int(input("Enter a number "))
# if d % 3 == 0 and d % 7 ==0:
#     print(d,"is divisible by both 3 and 7")
# else:
#     print(d,"is not divisible by both 3 and 7")
##--------------------------------------------------------------------------------

## 10. Check whether a given character is uppercase or lowercase.

# ch = input("Enter a character: ")
# if ch.isupper():
#      print(ch,"is uppercase")
# elif ch.islower():
#     print(ch,"is lowercase")
# else:
#     print(ch,"it is not alphabet")

##--------------------------------------------------------------------------------

## 11. Find the largest of three numbers.
#
# p = input("Enter 1st number: ")
# q = input("Enter 2nd number: ")
# r = input("Enter 3rd number: ")
#
# if p > q and p > r:
#     print("p grater than both")
# elif q > p and q > r:
#     print("q grater than both")
# else:
#     print("r grater than both")

##--------------------------------------------------------------------------------

## 12. Calculate grade based on marks (A, B, C, Fail).
# marks = int(input("Enter marks: "))
#
# if marks >= 80 and marks <= 100:
#     print("Grade A")
#
# elif marks >= 60 and marks < 80:
#     print("Grade B")
#
# elif marks >= 40 and marks < 60:
#     print("Grade C")
#
# elif marks >= 0 and marks < 40:
#     print("Fail")
#
# else:
#     print("Invalid Marks")

##--------------------------------------------------------------------------------

## 13. Display the day of the week based on day number (1–7).

# day = int(input("Enter the day(1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input")

##--------------------------------------------------------------------------------

## 14. Create a simple calculator using if-elif (add, subtract, multiply, divide).

# s = int(input("Enter 1st number: "))
# t = int(input("Enter 2nd number: "))
# op = input("Enter operation(+, - , *, /) : ")
#
# if op == "+":
#     print("Addition", s+t)
# elif op == "-":
#     print("Subtraction", s-t)
# elif op == "*":
#     print("Multiplication", s*t)
# elif op == "/":
#     print("Division", s/t)
# else:
#     print("Invalid input")

##--------------------------------------------------------------------------------

## 15. Determine income tax slab based on salary.
# salary = float(input("Enter your salary: "))
# if salary <= 250000:
#     print("No tax (0%)")
# elif salary <= 500000:
#     print("Tax slab: 5%")
# elif salary <= 1000000:
#     print("Tax slab: 20%")
# else:
#     print("Tax slab: 30%")
##--------------------------------------------------------------------------------

## 16. Check whether a triangle is equilateral, isosceles, or scalene.
# s1 = int(input("Enter side 1: "))
# s2 = int(input("Enter side 2: "))
# s3 = int(input("Enter side 3: "))
#
# if s1 == s2 == s3:
#     print("Equilateral triangle")
# elif s1 == s2 or s2 == s3 or s1 == s3:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

##--------------------------------------------------------------------------------

## 17. Check whether a number is 1-digit, 2-digit, or multi-digit.

# num1 = int(input("Enter first number: "))
#
# if -9 <= num1 <= 9:
#     print("1 - digit number")
# elif -99 <= num1 <= 99:
#     print("2 - digit number")
# else:
#     print("Multi- digit number")

##--------------------------------------------------------------------------------

## 18. Convert marks into percentage and class (First, Second, Pass).
# marks1 = int(input("Enter marks: "))
# percentage = marks1
#
# if percentage >= 60:
#     print("First class")
# elif percentage >= 50:
#     print("Second class")
# elif percentage >= 40:
#     print("Pass class")
# else:
#     print("Fail")

##--------------------------------------------------------------------------------

## 19. Check whether a character is an alphabet, digit, or special symbol.

# ch = input("Enter a character: ")
# if ch.isalpha():
#     print("Alphabet")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special Symbol")

##--------------------------------------------------------------------------------

## 20. Display season name based on month number.
# month = int(input("Enter month number: "))
#
# if month == 12 or month == 1 or month == 2:
#     print("winter")
# elif month == 3 or month == 4 or month == 5:
#     print("summer")
# elif month == 6 or month == 7 or month == 8:
#     print("Monsoon")
# elif month == 9 or month == 10 or month == 11:
#     print("Autumn")
# else:
#     print("Invalid month number")

##--------------------------------------------------------------------------------

## 21. Check whether a number is positive and even.

# num2 = int(input("Enter a number: "))
# if num2 is num2<0:
#     print("Negative number")
# elif num2 is num2 > 0:
#     print("Positive number")
# else:
#     print("Number is zero")
##--------------------------------------------------------------------------------

## 22. Validate username and password using nested if.
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == "Admin":
#     if password == "1234":
#         print("Login successful")
#     else:
#         print("Login unsuccessful")
# else:
#     print("Wrong username or password")
##--------------------------------------------------------------------------------

## 23. Find the largest of three numbers using nested if.
# x = int(input("\nX :"))
# y = int(input("Y :"))
# z = int(input("Z :"))
#
# if x > y:
#     if x > z:
#         print("Largest X =", x)
#     else:
#         print("Largest Z =", z)
# else:
#     if y > z:
#         print("Largest Y =", y)
#     else:
#         print("Largest Z =", z)
##--------------------------------------------------------------------------------

## 24. Check whether a student is eligible for scholarship (marks + income).
# marks2 = int(input("\nMarks :"))
# income = int(input("Income :"))
#
# if marks2 >= 70:
#     if income <= 200000:
#         print("Eligible for scholarship")
#     else:
#         print("Not Eligible(income is high)")
# else:
#     print("Not Eligible(marks is low)")

##--------------------------------------------------------------------------------

## 25. Check whether a year is leap year and century year.

# year = int(input("Year :"))
#
# if year % 100 == 0:
#     if year % 400 == 0:
#         print("Century Leap year")
#     else:
#         print("Century but Not Leap year")
# else:
#     if year % 4 == 0:
#         print("Leap year")
#     else:
#         print("Not Leap year")

##--------------------------------------------------------------------------------
## 26. Print numbers from 1 to N.
# n2 = int(input("Enter N:"))
#
# for i in range(1, n2 +1):
#     print(i)

##--------------------------------------------------------------------------------
## 27. Print even numbers between 1 and 100.
# for i in range(2, 101, 2):
#     print(i)

##--------------------------------------------------------------------------------
## 28. Find the sum of first N natural numbers.
# n3 = int(input("Enter N: "))
# sum = 0
#
# for i in range(1, n3 + 1):
#     sum = sum + i
# print("Sum of first", n3, "natural numbers is", sum)

##--------------------------------------------------------------------------------

# # 29. Print the multiplication table of a given number.
# table = int(input("\nEnter a number which number table you want: "))
# for i in range(1,11):
#     print(table * i)

##--------------------------------------------------------------------------------

#  # 30. Find the factorial of a number.
# number = int(input("\nEnter a number: "))
# fact = 1
#
# for i in range(1, number+1):
#     fact = fact * i
#
# print("Factorial:", fact)

##--------------------------------------------------------------------------------
## 31. Count the number of digits in a number.
# num4 = int(input("\nEnter a number: "))
# count = 0
#
# while num4 !=0:
#     count += 1
#     num4 //=10
# print("Digits: ",count)

##--------------------------------------------------------------------------------
## 32. Print all factors of a number.
# num5 = int(input("\nEnter a number: "))
#
# for i in range(1, num5 + 1):
#     if num5 % i == 0:
#         print(i)

##--------------------------------------------------------------------------------
## 33. Check whether a number is prime.
# num33 = int(input("\nEnter a number: "))
# flag = True
#
# for i in range(2, num6):
#     if num6 % i == 0:
#         flag = False
#         break
#
# if flag and num6 > 1:
#     print("Prime")
# else:
#     print("Not Prime")
##--------------------------------------------------------------------------------
## 34. Print the Fibonacci series up to N terms.
# num7 = int(input("Enter terms: "))
# a, b = 0, 1
#
# for i in range(num7):
#     print(a)
#     a, b = b, a+b

##--------------------------------------------------------------------------------
## 35. Reverse a number using a for loop.
# num8 = input("Enter a number: ")
# rev = ""
#
# for i in num8:
#     rev = i + rev
#
# print("Reverse: ",rev)

##--------------------------------------------------------------------------------
## 36. Reverse a number using a while loop.
# num9 = int(input("Enter a number: "))
# rev = 0
#
# while num9 > 0:
#     rev = rev * 10 + num9 % 10
#     num9 = num9 // 10
# print("Reverse: ",rev)

##--------------------------------------------------------------------------------
## 37. Find the sum of digits of a number.
# num01 = int(input("Enter a number: "))
# sum = 0
#
# while num01 >0:
#     sum += num01 % 10
#     num01 //= 10
# print("Sum of digits:", sum)

##--------------------------------------------------------------------------------
## 38. Check whether a number is palindrome.
# num11 = int(input("Enter a number: "))
# temp = num11
# rev = 0
#
# while num11 > 0:
#     rev = rev * 10 + num11 % 10
#     num11 //= 10
#
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

##--------------------------------------------------------------------------------
## 39. Keep accepting numbers until the user enters 0 and then display the sum.
# sum = 0
# while True:
#      n3 = int(input("Enter a number: "))
#      if n3 == 0:
#          break
#      sum = sum + n3
# print("Sum of above all numbers is:", sum)

##--------------------------------------------------------------------------------
## 40. Print numbers from N to 1.
# n4 = int(input("\nEnter a number: "))
#
# for i in range(n4, 0, -1):
#     print(i)

##--------------------------------------------------------------------------------
## 41. Print numbers from 1 to 10 but stop when number is 6.
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)

##--------------------------------------------------------------------------------
## 42. Print numbers from 1 to 10 but skip multiples of 3.
# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i)

##--------------------------------------------------------------------------------
## 43. Search a number in a list and break when found.
# list = [40, 50, 60, 70, 80]
# key = int(input("Enter num to search: " ))
# for i in list:
#     if i == key:
#         print(key, "is present in the list")
#         break
# else:
#     print(key, "is not present in the list")

##--------------------------------------------------------------------------------
## 44. Print only odd numbers from a list using continue.
# lst = [1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     if i % 2 == 0:
#         continue
#     print(i)


##--------------------------------------------------------------------------------
## 45. Create a loop where pass is used as a placeholder condition.
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)
