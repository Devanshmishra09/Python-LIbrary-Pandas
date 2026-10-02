# Decribe Transpose : It returns describe value rows in columns and columns and columns in rows .
# Ex 

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shubh","Shivam","Suraj"],
    "Age":[20,22,21,25],
    "Subject":["Python","SQL","Excel","powerBi"],
    "Salary":[25000,24000,23000,22000]
})
print(a)
print(a.describe())
print(a.describe().transpose())


#  To extract out single column or multiple Column 
# use (head) to find single or multiple columns .
# for single columns 

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shubh","Shivam","Suraj"],
    "Age":[20,22,21,25],
    "Subject":["Python","SQL","Excel","powerBi"],
    "Salary":[25000,24000,23000,22000]
})

print(a["Salary"])
print(a["Name"])
print(a["Age"])
print(a["Subject"])



# for Multiple Columns 

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shubh","Shivam","Suraj"],
    "Age":[20,22,21,25],
    "Subject":["Python","SQL","Excel","powerBi"],
    "Salary":[25000,24000,23000,22000]
})
print(a)
print(a[["Age","Salary"]])


# Set Index : Use to Set column index 
# Ex 

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shubh","Shivam","Suraj"],
    "Age":[20,22,21,25],
    "Subject":["Python","SQL","Excel","powerBi"],
    "Salary":[25000,24000,23000,22000]
})
print(a)
a = a.set_index("Name")
print(a.head())


# Reset_Index : use to remove column index 
# ex 

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shubh","Shivam","Suraj"],
    "Age":[20,22,21,25],
    "Subject":["Python","SQL","Excel","powerBi"],
    "Salary":[25000,24000,23000,22000]
})

print(a.set_index("Name").head())

a.reset_index()
print(a)

