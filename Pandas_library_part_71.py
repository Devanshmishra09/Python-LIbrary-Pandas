# join method : It is used to join two or more dataframes based on a common column or index. 
# The join method can be performed using the `merge()` function in pandas.

# Example of join method in pandas:
import pandas as pd
a=pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                'value': [1, 2, 3, 4]}) 
b=pd.DataFrame({'key': ['B', 'D', 'E' ],
                'value': [5, 6, 7]}) 
c=a.join(b.set_index('key'), on='key', lsuffix='_left', rsuffix='_right')
print(c)


# merge method : It is used to combine two or more dataframes based on a common column or index.
# The merge method can be performed using the `merge()` function in pandas.

# Example of merge method in pandas:
import pandas as pd
a=pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                'value': [1, 2, 3, 4]})
b=pd.DataFrame({'key': ['B', 'D', 'E' ],
                'value': [5, 6, 7]})
c=pd.merge(a, b, on='key', how='inner', suffixes=('_left', '_right'))
print(c)    

