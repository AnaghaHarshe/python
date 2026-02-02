# None type
x = None
print(type(x))

#=================================================

#Numeric type datatype

#int
a = 10
print(type(a))
print(a)

#float
b = 2.56
print(type(b))
print(b)

#complex
c = 2 + 5j
print(c.real, c.imag)

#binary representation
d = 0b0101
print(d)

#conversion of binary
bin(21)
print(bin(21))


#octal rep.
e = 0o257   #(2*8^2 + 5*8^1 + 7) = [2*64 + 5*8 + 7] = (128 + 40 + 7) = 175
print(e)
#conversion of octal
oct(175)
print("octal of 175 - ", oct(175))


# Hexadecimal rep.
f = 0x2f     #(2 × 16¹) + (F × 16⁰) = (2 × 16) + (15 × 1) = 32 + 15 = 47 (decimal)
print(f)

#conversion of hexa
hex(47)
print(hex(47))

#=========================================================================================

#Sequences

#String
p = 'anagha'
print(p,(type(p)))

#List
list1 = [1, 2, 3]
print(list1,(type(list1)))

list1.append(4)
print("This is appended list", list1)

list1.insert(1, 5)
print("This is inserted list", list1)

list1.sort()
print("This is sorted list", list1)

list1.remove(5)
print("This is no. 5 removed list", list1)

list1.pop(2)
print("This is 2nd index popped list", list1)

#ISR operation in list (Indexing, Slicing, repetition)
print("     ")
print("Indexing")
lst=[1,2,3,4,5,6,7,8,9]
print(lst[0])
print(lst[1])

print(lst[-1])
print(lst[-2])

print("     ")
print("Slicing")
print(lst[1:9:3])  #[Start : End : stop/jump]
print(lst[:4])   #end at 4 no.
print(lst[::3])  # considering start to end value and apply where to stop
print(lst[:5:2])
print(lst[1::])
print(lst[::-1]) #reverse string

print("     ")
print("Repetition")
print(lst * 2)



#tuple
tuple1 = (1,2,3,4,5,6,7,8,9)
print(tuple1,(type(tuple1)))

s ='anagha',1,5
print(s[0])
print(s[1])
print(s[2])


s1 = {1,2,3,3}
print(s1)

s1.add(4)
print(s1)

print("    ")
a = {1,2,3}
b = {3,4,5}

print(a | b) #union
print(a & b) #intersection common value
print(a - b) # difference

#==================================================

#Dictionary (key : value pair) dictionary is a mapping-

d = {"name" : 'Anagha',
     "Course" : 'CSE(AI)',
     "Clg" : "DKTE"
     }
print(d)
print(type(d))
print(d.keys())
print(d.values())
print(d.items())
print("     ")
#===================================================

# Boolean datatype
print("boolean comparison operator-")
print(10>5)
print(10<5)
print(10>=5)
print(5==5)
print(5!=5)

print("Boolean with Logical Operators")
print("AND")
print(True and True)
print(True and False)

print(" ")
print("OR")
print(True or False)
print(False or False)

print(" ")
print("Xor")
print(True ^ True)
print(True ^ False)

print(" ")
print("Byte Datatype")
b = bytes([10,20])
print(type(b))
print(b)

