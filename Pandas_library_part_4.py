# METHOD  OF PANDAS 
# Mean : returns the average 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a.mean())


# Median : Returns the median value 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a.median())

# Mode : returns the most repeated value 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a.mode())


# Head : it returns the top elements of the series .
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a.head(3))  # 3 defines how many elements wants to returns 

# Tail : it returns last values 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a.tail(4))       # 4 defines how many elements wants to returns 
