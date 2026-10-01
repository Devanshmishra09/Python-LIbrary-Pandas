# DataFrames : stores data in tabular form (rows and columns) and is the most commonly used data structure in pandas.
# It is similar to a spreadsheet or SQL table.
# It is a Two dimensional labeled data structure with columns of potentially different types.

# ex
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)

# shape : it gives the shape of the dataframe in the form of tuple (rows,columns)
# ex 

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.shape)


# Column Tolist  : it  returns columns of the dataFrame in the list form .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.columns.tolist())


# Columns : It returns column of datafraame .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.columns)