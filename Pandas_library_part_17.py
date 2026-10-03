# writing a Dataframe to a csv file 
# we can use the to_csv() function to write a DataFrame to a CSV file.


# writing a Dataframe to a csv file
import pandas as pd
a=pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "City": ["New York", "London", "Paris"]
})

a.to_csv("data.csv", index=True)
print(a)



# writing a dataframe to an Excel file 

import pandas as pd 
a=pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "City": ["New York", "London", "Paris"]
})

a.to_excel("data.xlsx",index=True)
print(a)


# writing  dataframe to a json file 

import pandas as pd 
a=pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "City": ["New York", "London", "Paris"]
})

a.to_json("data.json",index=True)
print(a)