# Pandas – Rows & Columns Practice

# 6. Change the Marks of the student at index 5 to 80 using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[5,"Marks"]=80
print(b)
print(a)

# for Range 
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.loc[5:20,"Marks"]=80
print(b)
print(a)


# 7. Change the City of the student at index 10 to "London" using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[10,"City"]="London"
print(b)
print(a)


# 8. Change the City and Age of the student at index 8 to "Lucknow" and 23 using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[8,["City","Age"]]=["Lucknow",23]
print(b)
print(a)
# 9. Access the complete row at position 5 using iloc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.iloc[5]
print(b)



# 10. Access the Name and City of the student at row position 5 using iloc.
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.iloc[5,[1,3]]
print(b)
