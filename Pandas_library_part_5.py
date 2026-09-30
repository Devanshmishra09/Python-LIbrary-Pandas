# Min: returns minimum value of series 
# ex 
import pandas as pd 
a=pd.Series([10,24,63,84,21,59,67,35,24,35])
print(a.min())


# Max : Returns the maximum value of series 
# ex 
import pandas as pd 
a=pd.Series([10,24,63,84,21,59,67,35,24,35])
print(a.max())


# Count: it returns how many elements are present in series 
# ex 
import pandas as pd 
a=pd.Series([10,24,63,84,21,59,67,35,24,35])
print(a.count())


# var : ir returns the varience of Sries 
# ex 
import pandas as pd 
a=pd.Series([10,24,63,84,21,59,67,35,24,35])
print(a.var())

 
#  Unique : it removes the dublicate values .
# ex 
import pandas as pd 
a=pd.Series([10,20,30,40,50,10,20,60,40])
print(a.unique())