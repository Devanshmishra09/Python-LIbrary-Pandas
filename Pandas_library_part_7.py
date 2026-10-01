# isna : it checks values  if nan   then gives Gives True otherwise False 
# ex 

import pandas as pd 
a=pd.Series([58,14,25,24,34,68,5,35,65,45])
print(a.isna())

# notna : it checks values  if not nan   then gives Gives True otherwise False
# ex 
import pandas as pd 
a=pd.Series([10,20,float("nan"),50,60,70,float("nan"),float("nan")])
print(a.notna())


# dropna : it removes the nan values from the series 
# ex 
import  pandas as pd 
a=pd.Series([10,20,30,float("nan"),float("nan"),50])
print(a.dropna())


# fillna : Fill the nan values acouding the users need 
# ex 
import pandas as pd 
a=pd.Series([10,20,30,float("nan"),45,float("nan"),12])
print(a.fillna(5))