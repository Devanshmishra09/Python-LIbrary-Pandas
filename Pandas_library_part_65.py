# Date & Time in pandas 
# It is often necessary to work with date and time data in pandas.
# The library provides powerful tools for handling datetime objects,
# performing time series analysis, and manipulating date and time data efficiently.
# we will explore some common operations and functionalities related to date and time in pandas.

# Accessor Methods : in pandas, datetime data can be accessed and manipulated using accessor methods.

# dt accessor : The dt accessor is used to access datetime properties and methods of a pandas Series containing datetime data.

import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
print(a)

   # changing the datatype of the column to datetime
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
print(a.dtypes)

# finding Year, Month, Day, Hour, Minute, Second from the datetime column
import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
b=a["Joining_Date"].dt.year
print(b)


# Month
import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
b=a["Joining_Date"].dt.month
print(b)

# Day
import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
b=a["Joining_Date"].dt.day
print(b)


# Day Name
import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
b=a["Joining_Date"].dt.day_name()
print(b)


# Month Name
import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
b=a["Joining_Date"].dt.month_name()
print(b)
