# IOC : Use to select values from DataFrames on the Basis of index .
# it returns the value of on the basis of index of rows and keys of columns .

# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salay":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
print(a)
  # Selecting name Shivansh 
  # we will give index of row and Key of columns 
print(a.loc[1,"Name"])
  # Changing or updating values of Dataframes 
c=a.loc[3,"course"]="Excel"
print(c)
print(a)


# Increment in Salary 

import pandas as pd 
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
print(a)
a["Salary"]=a["Salary"]+500
print(a)

# adding Salary to single index 
import pandas as pd 
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
a.loc[0,"Salary"]=a.loc[0,"Salary"]+500
print(a)

# adding New columns to a DataFrame 
import pandas as pd 
a=pd.DataFrame({
    "Name": ["Devansh","Shivansh","Suryansh","Vedansh"],
    "course": ["Python","Cse","Mern","SQL"],
    "Salary":[25000,20000,22000,23000],
    "Age":[20,19,15,11]
})
print(a)
a["City"]=["Lucknow","Mumbai","Banglore","Delhi"]
print(a)