#  Indexing : when Index is customized it gives the customized index else it gives the default index .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.index)

# Size : It returns how many elements presents in DataFrames.
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.size)


# values : It returns all values of Tables in list form .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.values)


# info : It returns column ,index ,Not-null,Datatypes,memory of the DataFrame .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.info())


# Head : it returns top rows of Dataframes according to use of user needs .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.head(2))   # 2 defines inndex 

