# Tail : it returns rows lists from downwards according to the user needs .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.tail(2))  # it returns rows from downwards 


# Describe : It returns statics calculation like 
# [Count , Mean , Standard Derivations , Minimum value # PErcentage [25% 50% 75%] , MAximum value ]
# it works on integer columns 
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
print(a.describe())


# for Strings Columns it returns  .
#  [Count , Unique , Top , Frequency]
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],e
})
print(a)
print(a.describe())

# Rename : Use to renaming of Columns Name .
# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"],
    "Salary":[20000,19000,18000,17000]
})
print(a)
a.rename(columns={"Name":"Students"},inplace=True)
print(a)