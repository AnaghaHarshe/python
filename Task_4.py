##1. Write a Python program to create a NumPy array of size n from user input and print it.
import numpy as np
n = int(input("Enter size of array:"))
arr = []
for i in range(n):
    num = int(input(f"Enter elements {i+1}: "))
    arr.append(num)

np_arr = np.array(arr)

print("Numpy array: ",np_arr)


# 2. Take input of a 2D matrix (m×n) from the user and convert it into a NumPy array.

import numpy as np
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

matrix = []

for i in range(m):
    row = list(map(int(input(f"Enter {n} elements for row {i+1} separated by space: ")).split()))
    matrix.append(row)

np_array = np.array(matrix)

print("NumPy 2D Array: \n",np_array)



# 3. Create a NumPy array of numbers from 1 to 20 and reshape it into a 4×5 matrix.
import numpy as np

arr = np.arange(1, 21)
matrix = arr.reshape(4, 5)
print("4 x 5 matrix", matrix)




# 4. Generate a 3×3 identity matrix using NumPy.
i_matrix = np.eye(5)
print(i_matrix)



# 5. Create a 5×5 matrix of random integers (1–100) and print it.
print(np.random.randint(1, 101, (5,5)))



# 6. Given a 1D NumPy array, print the first, last, and middle element.
import numpy as np
arr = np.array(list(map(int, input("Enter elements separated by space: ").split())))

first = arr[0]
middle = arr[len(arr)//2]
last = arr[-1]

print("First element of the array: ", first)
print("Middle element of the array: ", middle)
print("Last element of the array: ", last)



# 7. From a given 2D array, extract the 2nd row as a 1D array.
import numpy as np

p = int(input("Enter number of rows (p):"))
q = int(input("Enter number of columns (q):"))

matrix = []

for i in range(m):
    rows =list(map(int, input(f"Enter {p} elements for row {i+1} separated by space: ").split()))
    matrix.append(rows)

arr = np.array(matrix)

print("\nComplete 2D Matrix\n", arr)

second_row = arr[1]
print("Second row from matrix ",second_row)



# 8. From a 2D array, extract the last column.
import numpy as np
p = int(input("Enter number of rows (p):"))
q = int(input("Enter number of columns (q):"))

matrix = []

for i in range(m):
    rows =list(map(int, input(f"Enter {p} elements for row {i+1} separated by space: ").split()))
    matrix.append(rows)

arr = np.array(matrix)

print("\nComplete 2D Matrix:")
print(arr)

last_column = arr[:, -1]
print("Last column from matrix ",last_column)



# 9. Create a 4×4 matrix and replace the diagonal elements with 0.
import numpy as np
matrix = np.arange(1, 17).reshape(4, 4)

print("Original Matrix:")
print(matrix)

np.fill_diagonal(matrix, 0)

print("\nMatrix after replacing diagonal with 0:")
print(matrix)



# 10. Given a 2D array, access the element at (row=2, col=3).
rows = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of columns: "))

matrix=[]
print("Enter the elements row wise")

for i in range(rows):
    row =list(map(int, input().split()))
    matrix.append(row)

print("\nmatrix")
for r in matrix:
    print(r)

if rows > 2 and cols > 3:
     print("\nElement at (row=2, col=3):", matrix[2][3])
else:
    print("\nMatrix is too small to access (row=2, col=3)")



# 11. From a 1D NumPy array, print all even-indexed elements.

import numpy as np

arr = np.array(list(map(int, input("Enter elements separated by space: ").split())))

print(arr)

print("Even- indexed elements- ",arr[::2])



# 12. From a 1D array, print elements between index 3 to 7.

import numpy as np
arr = np.array(list(map(int,(input("Enter elements separated by space: ").split()))))
print(arr)

print("Elements between index 3 to 7", arr[2:7])



# # 13. From a 5×5 matrix, slice out the top-left 3×3 submatrix.
import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)

print("Original 5x5 Matrix:\n", matrix)

submatrix = matrix[:3, :3]

print("\nTop-left 3x3 Submatrix:\n", submatrix)

## Method 2
#
# import numpy as np
#
# print("Enter 25 elements for 5x5 matrix:")
# elements = list(map(int, input().split()))
#
# matrix = np.array(elements).reshape(5, 5)
#
# submatrix = matrix[:3, :3]
#
# print("Top-left 3x3 Submatrix:")
# print(submatrix)

  ## access any sub matrix
   #  submatrix = matrix[row_start : row_end, col_start : col_end]



# 14. From a 6×6 matrix, extract every alternate row and column.
import numpy as np
matrix = np.arange(1, 37).reshape(6,6)
print("Original 6x6 Matrix:\n", matrix)

result = matrix[::2, ::2]
print("extract every alternate row and column.\n", result)




# 15. Reverse a given NumPy array using slicing.
arr = np.array(list(map(int, input("Enter elements separated by space: ").split())))

print("Orignal array:-",arr)
print("Reverse array:-",arr[::-1])



# 16. Take an array of integers from the user and separate odd and even numbers using slicing/indexing.

import numpy as np

arr =np.array(list(map(int,input("Enter elements separated by space: ").split())))

print("Original array:-",arr)
even = arr[arr % 2 ==0]
odd = arr[arr % 2 !=0]

print("Odd elements", odd)
print("Even elements", even)



# 17. Replace all negative values in an array with 0.

arr = np.array(list(map(int, input("Enter elements separated by space: ").split())))
print("Original array:-",arr)

arr [ arr < 0 ]= 0
print("After replacing -ve elements:- ", arr)



# 18. Create a 5×5 matrix and set the border elements to 1 and inside elements to 0.

import numpy as np
matrix = np.zeros((5, 5),dtype=int)
matrix[0, :] = 1
matrix[4, :] = 1
matrix[:, 0] = 1
matrix[:, 4] = 1

print("5×5 matrix and set the border elements to 1 and inside elements to 0.\n", matrix)



# 19. Take two 2D arrays from the user and perform matrix addition and multiplication.
import numpy as np

row = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of columns: :"))

print("Enter first matrix elements row-wise:")
data1 = [list(map(int, input().split())) for _ in range(row)]
matrix1 = np.array(data1)
print("Matrix 1 \n",matrix1)

print("Enter second matrix elements row wise:")
data2 = [list(map(int,input().split()))for _ in range(row)]
matrix2 = np.array(data2)
print("Matrix 2 \n",matrix2)

addition = matrix1 + matrix2
print("Addition of Matrix\n", addition)

multiplication = np.dot(matrix1, matrix2)
print("Multiplication of Matrix\n", multiplication)




# 20. Flatten a given 2D matrix into a 1D array using NumPy.
import numpy as np

rows = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of columns: "))

#Enter matrix elements row-wise#
data = [list(map(int, input().split())) for _ in range(rows)]

matrix = np.array(data)
flat_array = matrix.flatten()
print("Flattened 1D Array:", flat_array)
