#  # Upper & Lower case 

# Upper 
# Name
import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["Name"].str.upper()
print(b)


# department


import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["Department"].str.upper()
print(b)


#  City

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["City"].str.upper()
print(b)

# lowwer 

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["Name"].str.lower()
print(b)


# department


import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["Department"].str.lower()
print(b)


#  City

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["City"].str.lower()
print(b)


# title used to give real formate 

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["Name"].str.title()
print(b)


# department


import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["Department"].str.title()
print(b)


#  City

import pandas as pd 
a=pd.read_excel("student_data.xlsx")
b=a["City"].str.title()
print(b)
