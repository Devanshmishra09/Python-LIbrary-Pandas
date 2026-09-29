# Pandas is a python library built for working with  structured data such as tables , 
# spreadsheets , csv files , database results and time series data . 
# Its two most important objects are series (1 dimension data ) and data Frame (2 Dimensional data).

# Pandas Importance 
# load data 
# Cleaning dublicate ,missing ,wrong data types and inconsisent text.
# Filtring ,Summarize 
# Creates Business matrix such as sales , average , growth etc.
# It works with Numpy ,matplotlib , Bi workflows etc .


# Series :
# 1 dim 
# in rows form 
# single Variable 
# no column axis 

# Dataframes 
# 2 dimensional 
# In table forms 
# one or more columns 

# series :
# ex 

import pandas as pd
a=pd.Series([10,20,30])
print(a)

# for customize index 

import pandas as pd
a=pd.Series([10,20,30],index=["shivam","shubh","devansh"])
print(a)

# with dictonary 

import pandas as pd
a=pd.Series({"shivam":50,"shubh":40,"Devansh":60})
print(a)


# Finding values with  keywords 

import pandas as pd 
a=pd.Series({"shivam":50,"shubh":82,"Devansh":98})
print(a["shubh"])