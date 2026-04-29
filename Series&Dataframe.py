#1. Series and Dataframe

import pandas as pd
print("\nSeries and Dataframe")
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)

data1 = {
    'Name':['Anagha','Ankita'],
    'Marks':[90, 85]
    }
df = pd.DataFrame(data1)
print(df)

# ----------------------------------------------------------------------------
#2. Creating Data Frame from an Excel Spreadsheet

print("\nCreating Data Frame from an Excel Spreadsheet")
df = pd.read_excel("data.xlsx")   #read data
print(df)


# update in dataframe
print("\nupdate in dataframe ")
df.loc[0, 'Marks'] = 95
print(df)


#Selecting Specific Columns
print("\nSelecting Specific Columns")
df = pd.read_excel("data.xlsx", usecols=['Name','Marks'])
print(df)

#Skipping rows
print("\nSkipping rows")
df = pd.read_excel("data.xlsx", skiprows=2)
print(df)

# ----------------------------------------------------------------------------
#3. Creating Data Frame from .csv Files

print("Creating Data Frame from .csv Files")

data = {
        'Name': ['Anagha', 'Ankita', 'Arohi'],
        'Marks':[90,85, 80]
        }

df = pd.DataFrame(data)

df.to_csv("data.csv", index= False)  #index=False removes row numbers

df = pd.read_csv("data.csv")
print(df)


# ----------------------------------------------------------------------------
# 4. Creating Data Frame from a Python Dictionary

print("\nCreating Data Frame from a Python Dictionary")

data = {
        'Name':["Anagha", "Ankita"],
        'PRN': ['22UAI033', '22UDS030'],
        'Dept': ['AIML', 'AIDS']
      }

df = pd.DataFrame(data)
print(df)

print("\nTranspose") #Converts rows ↔ columns for better format
df = pd.DataFrame(data).T
print(df)


# ----------------------------------------------------------------------------
#5. Creating Data Frame from Python List of Tuples

import pandas as pd
data = {
        (101,'Riya', 25000),
        (102,'Anagha', 35000),
        (103, 'Aditya', 40000)
        }

df = pd.DataFrame(data, columns=['EmpID',  'EmpName', 'Salary'])
print("Creating Data Frame from Python List of Tuples\n",df)


# ----------------------------------------------------------------------------
#6. Viewing Data frame Using loc() and iloc()

data = {
        'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
        'Marks': [90, 85, 70, 75],
        'City': ['Ichalkarnji','Kolhapur', 'Pune', 'Sangli']
}

df = pd.DataFrame(data)
print(df)

#loc() → Label-Based Selection

print("\n",df.loc[0])

print("\nIndex:1 and Marks:-",df.loc[1, 'Marks'])

print("\nMulltiple rows:\n",df.loc[0:2])

print("\nSpecific column\n",df.loc[:,['Name', 'Marks']])

print("\nCondition-based selection\n",df.loc[df['Marks'] > 80])

# iloc() - Index based selection

print("iloc() - Index based selection")
print("\nSelect single row\n",df.iloc[1])

print("\nSelection specific value\n",df.iloc[1,1])

print("\nSelect multiple rows\n",df.iloc[0:3])

print("\nSelect subset (rows + columns) \n",df.iloc[1:3][0:2])


# ----------------------------------------------------------------------------
# 7.Operations on Data Frames

import pandas as pd
data = {
        'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
        'Marks': [89, 85, 70, 75],
        'City': ['Ichalkarnji','Kolhapur', 'Pune', 'Sangli']
}

df = pd.DataFrame(data)
print(df)

df['Bonus_Marks'] = df ['Marks'] + 5
print("\n1. Adding a New Column\n",df)

df.loc[0, 'Marks'] = 95
print("\n2. Updating Data\n",df)

df.drop('Bonus_Marks', axis = 1, inplace=True)
print("\n 3. Deleting a Column\n",df)

df.drop(2, inplace = True)
print("\n4. Delete row\n",df)

df['Marks'] = df['Marks'] + 2
print("\n5. Arithmetic Operations\n",df)

df1 = df[df['Marks']>80]
print(("\n6. Filtering Data\n"),df1)

df2 = df.sort_values('Marks')
print("\n7. Sorting Data\n", df2)

df.rename(columns={'Marks': 'Score'}, inplace = True)
print("\n8.Renaming Columns\n",df)


#----------------------------------------------------------------------------
#8. Knowing Number of Rows and Columns
import pandas as pd

data = {
        'Name':['Anagha','Ankita','Amita','Arohi'],
        'Dept':['Manager','HR','IT', 'Salse'],
        'Salary':[80000, 55000, 40000, 30000]
        }
df = pd.DataFrame(data)
print(df)

print("\n1.Using shape\n",df.shape)

print("\n2. Get Number of Rows Only\n",df.shape[0])

print("\n3. Get Number of Columns Only\n", df.shape[1])

print("\n4. Using len() (Rows)\n",len(df))


# ----------------------------------------------------------------------------
# 9. Retrieving Rows from Data Frame
# “Rows in a DataFrame can be retrieved using methods like loc(), iloc(), head(), tail(), and conditional filtering.”

#----------------------------------------------------------------------------
# 10. Retrieving a Range of Rows
import pandas as pd

data = {
        'Name':['Anagha', ' Ankita', 'Amita', 'Arohi', 'Manisha'],
        'Age':[22,21,20,15,23],
        'City':['Tilwani','Kerli','Kolhapur','Ichalkaranji','Jaypur']
        }
df= pd.DataFrame(data)
print(df)

#1. Using loc() (Label-Based Range)
print("\n",df.loc[1:3]) 

#2. Using iloc() (Index-Based Range)
print("\n",df.iloc[1:3])

#3. Range with Specific Columns
print("\n",df.loc[0:4,['Name','City']])

#4. Range Using Step (Skipping Rows)
print("\n",df.loc[0:5:2])


# ----------------------------------------------------------------------------
# 11. Retrieving Data from Multiple Columns
import pandas as pd

data = {
    'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
    'Marks': [90, 85, 70, 75],
    'City': ['Pune', 'Kolhapur', 'Pune', 'Sangli']
}

df = pd.DataFrame(data)
print(df)

#1. Selecting Multiple Columns (Most Common)
print("\n",df[['Name', 'City']])

#2. Using loc() for Multiple Columns
print("\n",df.loc[:, ['Name', 'City']])   # : means all rows

#3. Using iloc() (Index-Based)
print("\n",df.iloc[:, [0, 2]])

#4. Selecting Columns with Condition
print("\n",df.loc[df['Marks'] > 80, ['Name', 'Marks']])

#5. Selecting First Few Columns
print(df.iloc[:, 0:2])


#----------------------------------------------------------------------------
# 12. Finding Maximum and Minimum Values
max = df['Marks'].max()
min = df['Marks'].min()

print("\nMaximun marks form column",max)
print("Minimun marks form column",min)


#----------------------------------------------------------------------------
# 13. Displaying Statistical Information
d1=df.describe()
print(d1)


#----------------------------------------------------------------------------
# 14. Performing Queries on Data
d2 = df[df['Marks'] > 80]
print("\n",d2)

d3 = df.query('Marks > 71')
print("\n",d3)


#----------------------------------------------------------------------------
# 15. Setting a Column as Index
df.set_index('Name', inplace=True)
print("\n",df)


#----------------------------------------------------------------------------
# 16. Resetting the Index
df.reset_index(inplace=True)
print(df)


#----------------------------------------------------------------------------
#17. Sorting the Data)
d4= df.sort_values('Marks')  #asending order
print("\n",d4)

df.sort_values('Marks', ascending=False, inplace=True)  #desending order
print(df)


#----------------------------------------------------------------------------
#18. Handling Missing Data

import pandas as pd
import numpy as np

data = {
    'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
    'Marks': [90, np.nan, 70, np.nan],
    'City': ['Pune', 'Kolhapur', None, 'Sangli']
}

df = pd.DataFrame(data)
print(df)

print("\nDetect\n",df.isnull())    #Detect

df.fillna({'Marks':0, 'City':'Unknown'}, inplace=True)   #replace

print("\n After Replace\n",df)

df.dropna(inplace=True)   #remove

print("\nAfter Remove\n",df)



#----------------------------------------------------------------------------
# 19. Creating Series from a DataFrame
import pandas as pd

data = {
    'Name': ['Anagha', 'Ankita', 'Amita', 'Arohi'],
    'Marks': [90, 85, 70, 75],
    'City': ['Pune', 'Kolhapur', 'Pune', 'Sangli']
}

df = pd.DataFrame(data)
print(df)

print("\nCerating Marks series\n",df['Marks'])
print("\nCerating Names series\n",df['Name'])

#s = df.loc[:, 'Marks'] , s = df.iloc[:, 1]   # column index 1 = Marks


#----------------------------------------------------------------------------
#20. Creating Series from Numpy Array

import pandas as pd
import numpy as np

arr = np.array([10,20,30,40])

s = pd.Series(arr)
print(s)


#----------------------------------------------------------------------------
# 21. Converting Series into Numpy Array

import pandas as pd
import numpy as np

s = pd.Series([10,20,30,40,50])

arr = s.to_numpy()
print("\nConverting Series into Numpy Array\n",arr)



#----------------------------------------------------------------------------
# 22. Creating Series from a Dictionary

import pandas as pd

data = {
        'A':11, 'B':22, 'C':23
        }

s = pd.Series(data)
print(s)



#----------------------------------------------------------------------------
# 23. Accessing Elements of a Series

import pandas as pd

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
