# Removing Dublicate value .

# we use duplicated()

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a.duplicated("Name")]
print(b)

#
import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.duplicated("Name")
print(b)

# with Department

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a.duplicated("Department")]
print(b)


# with City

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a.duplicated("City")]
print(b)



# with Age 

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a.duplicated("Age")]
print(b)


# Marks 

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a.duplicated("Marks")]
print(b)


# Attendance

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a.duplicated("Attendance")]
print(b)

