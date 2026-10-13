# 5 Practice  Questions on Pandas Library

# 1 
import pandas as pd
a=pd.read_excel("student.xlsx")
print(a)
b=a.loc[a["Marks"]>80]
print(b)


# 2

import pandas as pd
a=pd.read_excel("student.xlsx")
print(a)
b=a.loc[a["Attendance"]<80]
print(b)


# 3

import pandas as pd
a=pd.read_excel("student.xlsx") 
print(a)
b=a.loc[a["Department"]=="CSE"]
print(b)


# 4

import pandas as pd
a=pd.read_excel("student.xlsx")
print(a)
b=a.loc[a["Exam_Status"]=="Fail"]
print(b)


# 5 

import pandas as pd
a=pd.read_excel("student.xlsx")
print(a)
b=a.loc[a["Marks"]>80 & a["Attendance"]<80]


