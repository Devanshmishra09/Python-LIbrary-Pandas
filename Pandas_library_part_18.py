# using min max function in pandas library
# max : it will return the maximum value from the column

# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a["Age"].max())
print(a["Salary"].max())


# idxmax : it will return the id of max value 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a["Salary"].idxmin())
print(a.loc[a["Salary"].idxmin()])

# min : using to find minimum value  

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a["Age"].min())
print(a["Salary"].min())

# idxmin : it will return the id of min value .

import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","Shivansh","Suryansh","Vedansh"],
    "Age":[20,19,15,11],
    "Course":["Python","Excel","Sql",None],
    "Salary":[20000,19000,25000,56000]
})
print(a)
print(a["Age"].idxmin())
print(a.loc[a["Age"].idxmin()])
print(a["Salary"].idxmin())
print(a.loc[a["Salary"].idxmin()])