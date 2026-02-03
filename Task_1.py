#1. Write a program to perform addition, subtraction, multiplication, and division on two integers.

a = (int(input("Enter a number: ")))
b = (int(input("Enter b number: ")))
print("a + b =", a+b)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", a/b)


#2. Accept a float value from the user and convert it into an integer.
c = (float(input("c=")))
print(int(c))

#3. Perform addition of two complex numbers.
        M1
p = 5 + 3j
q = 4 + 2j
print(p + q)
         M2
p1 = complex(input("Enter 1st complex number: "))
p2= complex(input("Enter 2nd complex number: "))
print(p1 + p2)


#4. Write a program to convert a decimal number into binary.
d = int(input("Enter a number: "))
bin(d)
print(bin(d))


#5. Convert a decimal number into octal and hexadecimal.
e = int(input("Enter a number: "))
oct(e)
print(oct(e))

hex(e)
print(hex(e))


#6. Convert a binary number into decimal.
binary = input("Enter a binary number: ")
deci = int(binary, 2)
print("Decimal number:", deci)

#7. Convert a hexadecimal number into decimal.
f = input("Enter a hexadecimal number:")   #A, 1F, 2A, 7B, FF, 3C9, 9AF, 10A
hexdec = int(f, 16)
print("Decimal number: ", hexdec)


#8. Write a program to display a number in binary, octal, and hexadecimal formats.
num = int(input("Enter a decimal number:"))
bin(num)
print(bin(num))

oct(num)
print(oct(num))

hex(num)
print(hex(num))


#9. Demonstrate string slicing with examples.
str = "AnaghaHarshe"
print(str)
print(str[0:6:]) # start : End : Stop
print(str[::6])
print(str[::-1])
print(str[-6:12])


#10. Create a list of integers and find the sum of all elements.
list = [10, 20, 30, 40, 50]
print(list)
total = sum(list)
print(total)


#11. Write a program to find the largest and smallest element in a list.
list1 = [50, 20,79, 30, 66, 87, 12]

largest = max(list1)
smallest = min(list1)

print("largest value from the list is: ", largest)
print("smallest value from the list is: ", smallest)

#12. Demonstrate list methods: append(), insert(), remove(), and pop().
list2 = [1, 2, 3, 4]
print(list2)

list2.append(5)
print(list2)

list2.insert(1,7)
print(list2)

list2.remove(2)  #using value
print(list2)

list2.pop(1)  # using index number
print(list2)


#13. Write a program to remove duplicate elements from a list.
list3 = [1, 2, 3, 3, 5, 7, 9,7]
print(list3)

new_lst = list(set(list3))
print("This is new list ", new_lst)


#14. Sort a list in ascending and descending order.
lst = [50, 20,79, 30, 66, 87, 12]
print(lst)
lst.sort()
print("Ascending order", lst)
lst.sort(reverse=True)
print("Descending order", lst)


# 15. Create a tuple and access its elements using indexing.
t = (1, 2, 3, 4, 5)
print(t)
print(t[0])
print(t[1])
print(t[3])
print(t[-1])


#16. Write a program to convert a tuple into a list.
t2 = (1, 2, 3, 4, 5, 6)
print(t2)
newList = list(set(t2))
print(newList)


# 17. Demonstrate immutability of tuples with an example.
t3 = (1, 2, 4, 5, 6)
print(t3)
t3.append(7)     #AttributeError: 'tuple' object has no attribute 'append'
print(t3)
t3.remove(4)       #AttributeError: 'tuple' object has no attribute 'remove'
print(t3)


# 18. Count the number of occurrences of an element in a tuple.
t4 = (1, 2, 3, 4, 3, 5, 3, 6)
count = t4.count(3)
print(count)


# 19. Create two sets and perform union, intersection, and difference operations.
a ={1,2,3}
b ={3,4,5}
print(a | b) #union
print(a & b) #intersection
print(a - b) #diffrence


# 20. Write a program to remove duplicate elements from a list using a set.
lst = [10, 20, 60, 20, 30, 40, 40, 50]

new_list1 = list(set(lst))
print("Original List:", lst)
print("After removing duplicates:", new_list1)


# 21. Add and remove elements from a set.
b = {1,7,2,3,5}
print(b)

b.add(4)
print(b)

b.remove(7)
print(b)

#22. Create a dictionary of student details and display keys and values.
d ={
    "Name" : "Anagha",
    "College" : "DKTE",
    "Course" : "CSEAI",
    "PRN" : 22033
}
print(d)
print(d.keys())
print(d.values())

#23. Write a program to update and delete elements from a dictionary.
d2 ={
    "Name" : "Anagha",
    "Course" : "CSEAI",
    "PRN" : 22033
}
print(d2)
d2.update({"Age": "21", "marks": 85})
print("After update():", d2)

d2.pop("Age")
print("After pop():", d2)


# 24. Write a program to demonstrate boolean values True and False.
x = 10
y = 15
print(x > y)
print(x < y)
print(x == y)
print(x != y)


# 25. Check whether a given number is even or odd using boolean expressions.
n = int(input("Enter number: "))
if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")


# 26. Create a byte object and display its elements.
b = bytes([10, 20, 30, 40, 50])
print(b)
for i in b:
    print(i)


# 27. Create a bytearray and modify its elements.
ba = bytearray([10, 20, 30, 40, 50])
print("Original bytearray:", ba)
ba[1] = 99
print("After modification:", ba)



# 28. Demonstrate the use of constants in Python and explain why they are not strictly enforced.
PI = 3.14
r = int(input("Enter the radius: "))

area = PI * r * r    #3.14 * r * r
print("Area =", area)
