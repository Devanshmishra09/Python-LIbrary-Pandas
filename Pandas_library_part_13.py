# iloc : Integer-location based indexing for selection by position
# df.iloc[row_indexer, column_indexer]
# Ex 
import pandas as pd 
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
print(a)
print(a.iloc[1,2])


# Adddig some values in in it 
import pandas as pd 
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
print(a)
c=a.loc[1,"Salary"]+600
print(a)


# Adding new columns to a DataFrame
import pandas as pd
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
a["City"]=["Lucknow","Mumbai","Banglore","Delhi"]
print(a)


# Removing columns from a DataFrame
import pandas as pd
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
a=a.drop("City", axis=1)
print(a)

