# #1. Create a DataFrame from a Python dictionary containing employee details.
# import pandas as pd

# data = {
#         'EmpId': [101,202,303,404],
#         'EmpName':['Anagha','Aditya','Amita','Ishan'],
#         'Department':['Hr', 'IT', 'Finance', 'Marketing'],
#         'Salary':[80000, 60000, 40000, 30000]
#         }

# df = pd.DataFrame(data)

# print(df)


##------------------------------------------------------------------------------------------------
## 2. Create a DataFrame from a list of tuples representing student records.
 
# import pandas as pd

# data = [
#         (1, 'Anagha', 90, 'Pune'),
#         (2, 'Amita', 85, 'Kolhapur'),
#         (3, 'Sakshi', 80, 'Chandhgad'),
#         (4, 'sanchita', 75, 'Sangli')        
#         ]

# df =pd.DataFrame(data, columns=['RollNo', 'Name', 'Marks', 'City'])
# print("Student Dataframe:\n",df)


##------------------------------------------------------------------------------------------------
# # 3. Create a DataFrame from a CSV file containing product information.
# import pandas as pd

# df = pd.read_csv("products.csv")

# print("Product Dataframe\n",df) 


##------------------------------------------------------------------------------------------------
# # 4. Create a DataFrame from an Excel spreadsheet of sales data.
 
# import pandas as pd

# df =pd.read_excel("sales.Xlsx")

# print("Sales Dataframe\n",df)



##------------------------------------------------------------------------------------------------
# # 5. Display the first 5 rows of a DataFrame using head().
 
# import pandas as pd

# data = {
#         'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi', 'Arpita', 'Aradhna'],
#         'Marks':[95, 90, 88, 75, 80, 88]
#         }
# df = pd.DataFrame(data)

# print(df.head(5))


##------------------------------------------------------------------------------------------------
# # 6. Display the last 3 rows of a DataFrame using tail().
# import pandas as pd

# data = {
#         'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi', 'Arpita', 'Aradhna'],
#         'Marks':[95, 90, 88, 75, 80, 88]
#         }
# df = pd.DataFrame(data)

# print(df.tail(3))


##------------------------------------------------------------------------------------------------
# # 7. Display the shape of the DataFrame.

# import pandas as pd

# data = {
#         'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi', 'Arpita', 'Aradhna'],
#         'Marks':[95, 90, 88, 75, 80, 88]
#         }
# df = pd.DataFrame(data)

# print("\nShape of DataFrame:\n",df.shape)

 
##------------------------------------------------------------------------------------------------
# # 8. Display the column names of a DataFrame.

# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
#     'Marks': [90, 85, 70, 75],
#     'City': ['Pune', 'Kolhapur', 'Pune', 'Sangli']
# }

# df = pd.DataFrame(data)

# print("Column Names:", df.columns)


##------------------------------------------------------------------------------------------------
# # 9. Display the data types of all columns.
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
#     'Marks': [90, 85, 70, 75],
#     'Percentage': [90.5, 85.0, 70.2, 75.3],
#     'Passed': [True, True, False, True]
# }

# df = pd.DataFrame(data)

# print("Data Types:\n", df.dtypes)


##------------------------------------------------------------------------------------------------
# # 10. Generate a DataFrame with random numerical values using NumPy.

# #1. Using np.random.rand() (Random Floats)
# import pandas as pd
# import numpy as np

# data = np.random.rand(4,3) # data = np.random.rand(4,3)

# df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# print(df) 


# #2. Using np.random.randint() (Random Integers)
# data = np.random.randint(10, 100, size=(4, 3))

# df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# print(df)

##------------------------------------------------------------------------------------------------
# # 11. Retrieve a single row from a DataFrame using loc().
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita'],
#     'Age': [22, 25, 23]
# }

# df = pd.DataFrame(data)

# row = df.loc[1]

# print(row)


##------------------------------------------------------------------------------------------------
# # 12. Retrieve multiple rows using row labels with loc().
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita', 'Amit'],
#     'Age': [22, 25, 23, 24]
# }

# df = pd.DataFrame(data)

# rows = df.loc[[0, 2]]

# print(rows)


##------------------------------------------------------------------------------------------------
# # 13. Retrieve a specific row and column using iloc().
 
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita'],
#     'Age': [22, 25, 23]
# }

# df = pd.DataFrame(data)

# value = df.iloc[1, 0]

# print(value)


##------------------------------------------------------------------------------------------------
# # 14. Retrieve a range of rows using iloc().
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita', 'Amit', 'Neha'],
#     'Age': [22, 25, 23, 24, 21]
# }

# df = pd.DataFrame(data)

# rows = df.iloc[1:4]

# print(rows)

##------------------------------------------------------------------------------------------------
# # 15. Retrieve multiple columns using loc().
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita'],
#     'Age': [22, 25, 23],
#     'City': ['Mumbai', 'Pune', 'Delhi']
# }

# df = pd.DataFrame(data)

# columns = df.loc[:, ['Name', 'City']]

# print(columns)

##------------------------------------------------------------------------------------------------
# 16. Retrieve alternate rows from a DataFrame using iloc().

# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita', 'Amit', 'Neha'],
#     'Age': [22, 25, 23, 24, 21]
# }

# df = pd.DataFrame(data)

# alternate_rows = df.iloc[::2]

# print(alternate_rows)


##------------------------------------------------------------------------------------------------
# # 17. Modify a specific value in the DataFrame using loc().

# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita'],
#     'Age': [22, 25, 23]
# }

# df = pd.DataFrame(data)

# df.loc[1, 'Age'] = 26

# print(df)


##------------------------------------------------------------------------------------------------
# # 18. Retrieve rows based on a conditional filter using loc().
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita', 'Amit'],
#     'Age': [22, 25, 23, 24]
# }

# df = pd.DataFrame(data)

# filtered_rows = df.loc[df['Age'] > 23]

# print(filtered_rows)
 
##------------------------------------------------------------------------------------------------
# # 19. Find the number of rows and columns in a DataFrame.
# import pandas as pd

# data = {
#     'Name': ['Anagha', 'Rahul', 'Sita'],
#     'Age': [22, 25, 23]
# }

# df = pd.DataFrame(data)

# print(df.shape)

##------------------------------------------------------------------------------------------------
# # 20. Retrieve only the first 10 rows from a large DataFrame.
# import pandas as pd

# # Sample DataFrame
# data = {
#     'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
#     'Age': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
# }

# df = pd.DataFrame(data)

# # Get first 10 rows
# print(df.head(10))

##------------------------------------------------------------------------------------------------
# # 21. Retrieve rows where a column value is greater than a specific number.
# import pandas as pd

# data = {
#     "Name": ["Amit", "Neha", "Rahul", "Priya"],
#     "Marks": [75, 92, 65, 88]
# }

# df = pd.DataFrame(data)

# result = df[df["Marks"] > 80]

# print(result)
 
##------------------------------------------------------------------------------------------------
# # 22. Retrieve rows where values lie between two numbers.
# import pandas as pd

# data={
#      'Name':['Anagha','Ankita','Amita','Arohi'],
#      'Marks':[95,72,65,88]
#      }
# df = pd.DataFrame(data)

# result = df[(df["Marks"] >= 70) & (df["Marks"]<=90)]
# print(result)


##------------------------------------------------------------------------------------------------ 
# # 23. Find the maximum and minimum values of a numeric column.
# import pandas as pd
# data={
#       'Name':['Ankita', 'Amita','Aditya', 'Ishan', 'Arohi', 'Aayansh'],
#       'Age':[21, 19, 24, 17, 11, 5]
#       } 
# df = pd.DataFrame(data)
# print(df)

# max_value = df["Age"].max()
# print("Maximum age is :-",max_value)

# min_value = df["Age"].min()
# print("Minimum age is :-",min_value)



##------------------------------------------------------------------------------------------------
# # 24. Display statistical information of the DataFrame using describe().
# df = pd.DataFrame(data)
# print(df)

# print(df.describe())


##------------------------------------------------------------------------------------------------
# # 25. Perform a query to retrieve rows where salary > 50000.
# import pandas as pd

# data = {
#     "Name": ["Ankita", "Amita", "Aditya", "Ishan"],
#     "Salary": [45000, 60000, 75000, 50000]
# }

# df = pd.DataFrame(data)

# result = df.query("Salary > 50000")

# print(result)


##------------------------------------------------------------------------------------------------
# # 26. Add a new calculated column to the DataFrame.

# import pandas as pd

# data = {
#     "Name": ["Ankita", "Amita", "Aditya"],
#     "Marks1": [80, 75, 90],
#     "Marks2": [85, 70, 95]
# }

# df = pd.DataFrame(data)

# df["Total"] = df["Marks1"] + df["Marks2"]

# print(df)

##------------------------------------------------------------------------------------------------
# # 27. Rename one or more columns of a DataFrame.
 
# import pandas as pd

# data = {
#     "Name": ["Ankita", "Amita", "Aditya"],
#     "Marks": [80, 75, 90]
# }

# df = pd.DataFrame(data)

# df.rename(columns={
#     "Name": "Student_Name",
#     "Marks": "Score"
# }, inplace=True)

# print(df)

##------------------------------------------------------------------------------------------------
# # 28. Delete a specific column from a DataFrame.
# import pandas as pd

# data = {
#     "Name": ["Ankita", "Amita", "Aditya"],
#     "Age": [21, 19, 24],
#     "Marks": [80, 75, 90]
# }

# df = pd.DataFrame(data)
# print(df,"\n")

# df.drop("Age", axis=1, inplace=True)

# print(df) 

##------------------------------------------------------------------------------------------------
# # 29. Check for duplicate rows in the DataFrame.
# import pandas as pd

# data = {
#         "Name":['Ankita', 'Amita', 'Ankita', 'Ishan'],
#         "Age":[21,19,21,17]
#         }
# df = pd.DataFrame(data)
# print(df,"\n")

# duplicates = df.duplicated()

# print(duplicates)

##------------------------------------------------------------------------------------------------
# # 30. Remove duplicate rows and display the updated DataFrame.
# df = pd.DataFrame(data)

# df = df.drop_duplicates()

# print("\n",df)

##------------------------------------------------------------------------------------------------
# # 31. Set a specific column as the index of the DataFrame.
# import pandas as pd

# data = {
#     "Roll_No": [101, 102, 103],
#     "Name": ["Ankita", "Amita", "Aditya"],
#     "Marks": [80, 75, 90]
# }

# df = pd.DataFrame(data)
# print(df,"\n")

# df.set_index("Roll_No", inplace=True)

# print(df)


##------------------------------------------------------------------------------------------------
# # 32. Reset the DataFrame index back to default.
# import pandas as pd

# data = {
#     "Roll_No": [101, 102, 103],
#     "Name": ["Ankita", "Amita", "Aditya"],
#     "Marks": [80, 75, 90]
# }

# df = pd.DataFrame(data)

# df.set_index("Roll_No", inplace=True) # Set Roll_No as index

# print("DataFrame with custom index:")
# print(df)

# df.reset_index(inplace=True) # Reset index back to default

# print("\nDataFrame after resetting index:")
# print(df)

##------------------------------------------------------------------------------------------------
# # 33. Sort the DataFrame based on a single column.
# import pandas as pd 
# data={
#      "Name":['Ankita', 'Amita', 'Ankita', 'Ishan'],
#      "Marks":[90,75,80,70]

#      }
# df = pd.DataFrame(data)

# sorted = df.sort_values(by = "Marks")

# print(sorted)

##------------------------------------------------------------------------------------------------
# # 34. Sort the DataFrame based on multiple columns.
# import pandas as pd

# # Sample DataFrame
# data = {
#     "Name": ["Ankita", "Amita", "Aditya", "Ishan"],
#     "Marks": [80, 75, 77, 70],
#     "Age": [21, 19, 22, 17]
# }

# df = pd.DataFrame(data)

# sorted_df = df.sort_values(by=["Marks", "Age"])

# print(sorted_df) 

##------------------------------------------------------------------------------------------------
# # 35. Create a Pandas Series from a Python list of 10 integers and display it.
# import pandas as pd

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# series = pd.Series(numbers)

# print(series)


##------------------------------------------------------------------------------------------------
# # 36. Create a Series from a NumPy array containing float values and print its data type.
# import pandas as pd
# import numpy as np

# arr = np.array([1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, 9.1]) 

# series = pd.Series(arr)

# print(series)

# print("\nData type of Series:", series.dtype)

##------------------------------------------------------------------------------------------------
# # 37. Create a Series using a dictionary of student names and their marks.
# import pandas as pd

# data = {
#     "Ankita": 85,
#     "Amita": 78,
#     "Aditya": 92,
#     "Ishan": 74
# }

# series = pd.Series(data)

# print(series)
 
##------------------------------------------------------------------------------------------------
# # 38. Convert an existing Series into a NumPy array.
# import pandas as pd
# import numpy as np

# series = pd.Series([10, 20, 30, 40, 50])

# array = series.to_numpy()

# print(array)

# print(type(array)) 


##------------------------------------------------------------------------------------------------
# # 39. Access the first, last, and middle elements of a Series using index labels.
 
# import pandas as pd

# series = pd.Series(
#     [10, 20, 30, 40, 50],
#     index=["a", "b", "c", "d", "e"]
# )

# print("First element:", series["a"])

# print("Middle element:", series["c"])

# print("Last element:", series["e"])


##------------------------------------------------------------------------------------------------
# # 40. Retrieve elements of a Series using positive and negative indexing.
# import pandas as pd

# series = pd.Series([10,20,30,40,50])

# print("Element at index 1:", series[1])

# print("last element:",series.iloc[-1])

# print("Second last element:",series.iloc[-2])
 

##------------------------------------------------------------------------------------------------
# # 41. Perform arithmetic operations (+, −, ×, ÷) between two Series.

# import pandas as pd

# s1 = pd.Series([10, 20, 30, 40])
# s2 = pd.Series([2, 4, 6, 8])

# print("Addition:\n",s1 + s2)

# print("\nSubtraction:\n",s1 - s2)

# print("\nMultiplication:\n",s1 * s2)

# print("\nDivision:\n",s1 / s2) 


##------------------------------------------------------------------------------------------------
# # 42. Find the maximum, minimum, mean, and sum of a Series.
# import pandas as pd

# series = pd.Series([10, 20, 30, 40, 50])

# print("Maximum value:", series.max())

# print("Minimum value:", series.min())

# print("Mean:", series.mean())

# print("Sum:", series.sum())


##------------------------------------------------------------------------------------------------
# # 43. Update specific values of a Series using index labels.
# import pandas as pd

# series = pd.Series(
#     [10, 20, 30, 40],
#     index=["a", "b", "c", "d"]
# )

# print("Original Series:")
# print(series)

# series["b"] = 25
# series["d"] = 45

# print("\nUpdated Series:")
# print(series)

 
##------------------------------------------------------------------------------------------------
# # 44. Filter Series values greater than a given threshold.
# import pandas as pd

# series = pd.Series([10, 25, 30, 15, 50, 8])

# filtered_series = series[series > 20]

# print(filtered_series)


