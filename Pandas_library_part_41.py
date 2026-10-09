
# Pandas – Null Value Handling Practice

# Use the given Excel dataset and solve all questions using Pandas.

# 16. Fill null values in Marks with the median Marks.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["Marks"].fillna(a["Marks"].median())
print(b)


# 17. Fill null values in City with the most frequently occurring City using mode().


import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["City"].fillna(a["City"].mode())
print(b)


# 18. Use fillna() to fill Marks with 0 and City with "Unknown" in one statement.


import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.fillna({"Age":0,"City":"Unknown"})
print(b)

# 19. Find the row position of Deepak.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =  a.loc[a["Name"] == "Deepak"].index
print(b)

# 20. Access Deepak's row using iloc.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =  a.iloc[a["Name"] == "Deepak"].index
print(b)