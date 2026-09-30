# when we indexing custom index then al index will be printed .

# default index 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a[1:4])

# with customize index 
import pandas as pd
a=pd.Series([10,20,30,40,50,60],index=["shubh","shivam","suraj","Ram","raghav","Devansh"])
print(a["suraj":"Devansh"])



# performing mathmaticial operatyions 
# addition 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a+25)

# substraction 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a-25)

# multiplication 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a*25)

# Division 
import pandas as pd 
a=pd.Series([10,20,30,40,50])
print(a/25)
