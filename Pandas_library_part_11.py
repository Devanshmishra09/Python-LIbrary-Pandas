# Perorming Operations on DataFrames .
# Adding New  columns :

# ex 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"]
})
print(a)
a["salary"]=[20000,19000,18000,17000]
print(a)


# substracting Columns :
# Drop we use drop for removing columns from DataFrame .
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"]
})
print(a)
print(a.drop(columns="Age"))



# Performing mathmatical operations in it .
# ex 
# add 2 years in age columns 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"]
})
print(a)
a["Age"]=a["Age"]+2
print(a)


# multiply : 
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"]
})
print(a)
a["salary"]=[20000,19000,18000,17000]
print(a)
a["salary"]=a["salary"]+a["salary"]*0.05
print(a) 


# Substracting :
import pandas as pd 
a=pd.DataFrame({
    "Name":["Devansh","shivam","shubhu","suraj"],
    "Age":[20,21,22,21],
    "Course":["Data Analytics","BCA","B.tech","M.tech"]
})
print(a)
a["salary"]=[20000,19000,18000,17000]
print(a)
a["salary"]=a["salary"]-2000
print(a)

