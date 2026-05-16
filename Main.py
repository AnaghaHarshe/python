#Advanced Data Analysis Using Pandas

# 1. Joining the DataFrames

import pandas as pd

df1 = pd.DataFrame({
    'ID':[1,2,3],
    'Name':['Anagha', 'sakshi', 'sanika',]
    })

df2 = pd.DataFrame({
    'ID':[1,2,3],
    'Marks':[95,85,90]
    })

result = pd.merge(df1,df2, on = "ID")
print(result)


r2 = pd.merge(df1, df2, on ='ID', how = 'left')
print("\nLeft join\n",r2)

r3 = pd.merge(df1, df2, on = 'ID', how = 'right')
print("\nRight Join\n",r3)

#---------------------------------------------------------------------------

#2. How to Join When There is No Common Column
# use left_index and right_index

import pandas as pd 

df1 = pd.DataFrame({
    'Name':['Anagha','Ankita','Neha']
    })

df2 = pd.DataFrame({
    'Marks':[95,90,88]
    })

result = pd.merge(df1, df2, left_index = True, right_index = True)

print(result)


#---------------------------------------------------------------------------

#3 Concentration of Tables
import pandas as pd
df1 = pd.DataFrame({1:['A', 'B']})
df2 = pd.DataFrame({1:['C','D']})

result = pd.concat([df1, df2])

print(result)

#Horizontal concatenation
df1 = pd.DataFrame({'Name':['Anagha','Ankita']})
df2 = pd.DataFrame({'Marks':[90,85]})
result = pd.concat([df1, df2], axis = 1)

print(result)


#---------------------------------------------------------------------------

# 4 where() Method
import pandas as pd 
df = pd.DataFrame({
    'Marks':[85,40,75,30]
    })
result = df.where(df['Marks']>40, "Fail")

print(result)


#---------------------------------------------------------------------------

# 5 groupby() Method
import pandas as pd
data = {
        'Department':['IT','HR', 'IT', 'HR'],
        'Salary':[50000, 60000, 45000, 55000]
        }

df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].sum()
print(result)


#---------------------------------------------------------------------------

# 6 Agregate functions
import pandas as pd
df = pd.DataFrame({
    'Marks':[85,90,78,88]
    })

print(df['Marks'].sum())
print(df['Marks'].mean())
print(df['Marks'].max())
print(df['Marks'].min())

#---------------------------------------------------------------------------

# 8 Regular expressions
import pandas as pd 
df = pd.DataFrame({
    'Email':[
        'abc@gmail.com', 'test@yahoo.com', 'hello@gmail.com'
        ]
    })

result = df[df['Email'].str.contains('gmail')]
print(result)


