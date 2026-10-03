# Drop : Dropping row from DataFrames 

# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a.drop(2,axis=0)) # we use 2 as a index of row 
print(a)


# Drop : Dropping columns From DataFrames  

# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a.drop("Age",axis=1)) # we use "Course" as a column


# drop : Dropping rows and columns from DataFrames
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a.drop(index=2,columns="Age",axis=0))

# drop : Dropping columns from dataframes using list of columns
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
df = a.drop(a.columns[[1, 2]], axis=1)
print(df)