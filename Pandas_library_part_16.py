# Reading and Writing Data with pandas 
# Real-world data is often stored in files, and pandas provides functions to read and write data from various file formats.
# The most common formats are CSV, Excel, and JSON.

# Reading with CSV files 
import os 
import pandas as pd 
a=pd.read_csv("student.csv")
print(a)

# Reading with Excel files 

import pandas as pd 
a=pd.read_excel("student.xlsx")
print(a)

# Reading with json files 

import pandas as pd 
a=pd.read_json("student.json")
print(a)

