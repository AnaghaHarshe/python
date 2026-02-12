#NUMPY ARRAY:-

# NumPy (Numerical Python) is a library used for working with array and mathematical operations in python.
# It is faster than normal Python lists because it is implemented in C and optimized for numerical works.

# Advantages of Arrays
# 1. Faster computation than list
# 2. Less memory usage
# 3. Supports mathematical operations directly
# 4. Can handel Multi-Dimensional data
# 5. Useful for Data Science, Ml, Scientific Computing

#=====================================================================================================================
# Types of array

import numpy as np

# 1- D array(vector)
a1 = np.array([1,2,3,4,5])
print(a1)

# 2-D Array(Matrix)
b1 = np.array([[1,2,3],[4,5,6]])
print(b1)

# 3-D Array / multi-dimensional array
c1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c1)

#------------------------------------------------------------------------------------------

# Working with Arrays using numpy
# 1. creating arrays
# 2. Accessing & modifying elements
# 3. Performing mathematical operations
# 4. Reshaping arrays
# 5. Using built-in functions
# 6. Handling multi-dimensional data

#------------------------------------------------------------------------------------------

#Array Creation Using:- array function, linspace, logspace, arange, zeros & ones,

# array()
a = np.array([1,2,3])
print(a)


# Linspace() - Generated evenly spaced numbers.
b= np.linspace(0, 10, 5) #Start,  stop,  num:- from starting to end how many number of parts you want to print
print(b)


# Logspace() - generates numbers evenly spaced on log scale.
c =np.logspace(0, 1, 5)
print(c)


# Arange() - similar to range
d = np.arange(1,10,3)
print(d)

# Zeros()  - print all zeros in matrix way
e = np.zeros((2,3))  # single num= 1-d  : 2 numbers = 2-D : 3 nums= 1st n - times, 2nd n - rows, 3rd n - column
print(e)

# ones() - print all ones in matrix way
f = np.ones((2,3))
print(f)

#------------------------------------------------------------------------------------------
# Mathematical Operations on Arrays

g = np.array([1,2,3])
h = np.array([4,5,6])
print("Addition: ", g+h)
print("Substraction: ", h - g)
print("Multipication: ",g * h)
print("Division: ", h / g)

#------------------------------------------------------------------------------------------
#Indexing and Slicing in numpy Arrays
i = np.array([1,2,3,4,5,6,7,8,9])
print(i[0])
print(i[5])
print(i[0 : 6])

#------------------------------------------------------------------------------------------
# Dimensions of Arrays
# In NumPy, the dimension of an array tells us how many axes (directions) it has.
# It is also called the rank of the array.

#( array.ndim ) = tells size of array

#1-D Array

j = np.array([10,20,30,40])
print(j.ndim)
print(j.shape)

# 2-D Array
k = np.array([[10,20,30],[40,50,60]])
print(k.ndim)
print(k.shape)

# 3-D Array
l = np.array([[[1,2,3],[4,5,6]],
             [[7,8,9],[10,11,12]]])
print(l.ndim)
print(l.shape)  # 2-blocks, 2-rows, 3-columns

# Changing Dimensions using reshape()
m = np.arange(6)
n = np.reshape(m,(2,3))  # reshape array m into 2 rows and 3 columns
print(n)

#------------------------------------------------------------------------------------------
# Attributes of an Array
o = np.array([[1,2,3],[4,5,6]])
print("\nNumber of dimensions",o.ndim)  # number of dimension
print("Size of array: ",o.shape)      # size (rows, columns)
print("Total Elements: ",o.size)     #total elements
print("Data type: ", o.dtype)         # Data Type
print("Memory size: ", o.itemsize)  # Memory Size


#------------------------------------------------------------------------------------------
# Working with Multi-dimensional Arrays
# 2-D array
k1 = np.array([[10,20,30],
               [40,50,60]])
print(k1)
print(k1.ndim)
print(k1.shape)
print(k1.size)
print(k1[0,1])  # 20
print(k1[1,2])  # 60


# 3-D array
                # 0       1
k2 = np.array([ [[1,2], [3,4]],   # 0   block
                [[5,6], [7,8]] ]) # 1   block
print(k2.ndim)
print(k2.shape)
print(k2[0, 0, 0])# block, row, column
print(k2[0, 0, 1])
print(k2[0, 1, 0])
print(k2[0, 1, 1])

print(k2[1, 0, 0])
print(k2[1, 0, 1])
print(k2[1, 1, 0])
print(k2[1, 1, 1])


# Slicing Multi-Dimension Arrays

print("\nEntire row of k1:",k1[0, :])
print("Entire column of k1:",k1[:,0])
print("partial selection: ",k1[:1:3])
