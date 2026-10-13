import pandas as pd 
a=pd.read_excel("Date_Time_Practice_set.xlsx")
a['Joining_Date'] = pd.to_datetime(a['Joining_Date'])
b=a["Joining_Date"].dt.year
c=a["Joining_Date"].dt.month
d=a["Joining_Date"].dt.day
e=a["Joining_Date"].dt.day_name()
f=a["Joining_Date"].dt.month_name()
print(b)
print(c)
print(d)    
print(e)
print(f)
