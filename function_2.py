#function example
def  average(a, b):
    print("The average is ",(a+b)/2)
average(4, 6)

#default argument
def average(a=9, b=1):
    print("The average is ",(a+b)/2)
average()  

#keywod arguments
def average(a, b):
    print("The average is ",(a+b)/2)
average(b=2, a=5)

#variable length argument
def average(*numbers):
    sum = 0
    for i in numbers:
        sum= sum+i 
    print(sum/len(numbers))
average(5, 6, 7, 8, 10, 20, )  

#return statment
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
c = average(5,6,7,1)
print(c)