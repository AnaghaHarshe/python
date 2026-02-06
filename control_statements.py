#CONTROL STATEMENTS:-

# if statement
age = 15
if age >=18:
    print("Eligible to vote")

# ------------------------------------------------------------

# if…. else statement
a = int(input("Enter age number: "))
if a >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#-------------------------------------------------------------------

# if…elif… else statement
age = int(input("Enter age number: "))

if age <= 12:
    print("you are child")
elif age >=13 and age <=19:
    print("you are teenager")
elif age >=20 and age <= 60:
    print("you are an Adult")
else:
    print("Senior citizen")

#------------------------------------------------------------------

# while loop
      # while condition:
              #statements
# Method 1
i = 1               # i = 1           |   i = 10         | i = 10
while i <= 5:       # while i <= 5:   |   while i>=5:    | while i >= 5:
    print(i)        #     i = i + 1   |       print(i)   |  i = i - 1
    i = i + 1       #     print(i)    |       i = i - 1  |  print(i)
                    #                 |                  |
# O/P = 1 2 3 4 5   #  2 3 4 5 6      | 10 9 8 7 6       | 9 8 7 6 5

#Method 2
i = 0
while i < 10:
    i += 1
    if i == 4:
        continue # when get continue then it will print all numbers excluding 4 and when get break then stop execution
    print(i)

#-------------------------------------------------------------------------------------------------------------------------


# for loop
# Method 1 numbers
for i in range(1, 10, 2):
    print(i)

# Method 2 strings
names=["Anagha", "Ankita", "Amita", "Arohi"]
for name in names:
    print(name)

# Method 3 character asssing
ch = "Python"
for ch in ch:
    print(ch)

# Reverse step value
for i in range(10, 0, -1):
    print(i)

#----------------------------------------------------------------------------------------

# break statement
# for break
for i in range(0, 10):
    i +=1
    if i == 6:
        break
    print(i)

#while break
i = 1
while i <=10:
    print(i)
    if(i == 5):
        break
    i=i+1

#--------------------------------------------------------------------

# continue statement
# for continue
for i in range(1,31):
    if i % 3 != 0:    # ( if i % 3 == 0 ) then print all values but not divisible by 3
        continue
    print(i)


# While continue
i = 5
while(i<15):
    i = i + 1
    if(i==10):
        continue
    print(i)

#----------------------------------------------------------------------------------------------------

# PASS STATEMENTS

# PASS in if
age = 12
if age >= 18:
    pass
else:
    print("You are minor")

# PASS in for
for i in range(1,5):
    pass       # when only pass will be pass then no any value will be print
    print(i)   # after pass print statement is there then values will be print


#PASS in while loop
i = 15            # i = 5
while i >= 5:     #while i<=15:
    print(i)      #    print(i)
    pass          #    pass
    i = i - 1     #    i = i+1


#-------------------------------------------------------------------------------------------------

# return statement

#Method 1
def add(a, b):
    return a+b
result = add(4, 2)
print(result)

def name():
    print("Anagha")
x = name()

# Method 2
n = int(input("enter  number: "))
def check(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
print(check(n))
