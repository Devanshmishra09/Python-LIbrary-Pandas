# Value_counts : It returns how many times value can be repeated 
# ex 
import pandas as pd 
a=pd.Series([10,20,30,40,50,10,30,40,50,60])
print(a.value_counts())


#  Sort_values : It returns values in ascending order : 
# ex 
import pandas as pd 
a=pd.Series([58,14,25,24,34,68,5,35,65,45])
print(a.sort_values())

# ex 
import pandas as pd 
a=pd.Series([58,14,25,24,34,68,5,35,65,45])
print(a.sort_values(ascending=False))


#  Sort_index: return value accoundding with imdex 
# ex 
import pandas as pd 
a=pd.Series([58,14,25,24,34,68,5,35,65,45])
print(a.sort_index())


# isna : it checks values  if nan   then gives Gives True otherwise False 
# ex 

import pandas as pd 
a=pd.Series([58,14,25,24,34,68,5,35,65,45])
print(a.isna())


