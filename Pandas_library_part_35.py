
# 📅 Phase 5: Date-Time Manipulation (21–25)

# 21. Convert to DateTime: Convert the Date column into a proper pandas datetime format.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Date'] = pd.to_datetime(a['Date'])
print(b)
                 
# 22. Extract Month: Create a new column named Month containing just the month name or number extracted from Date.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Month'] = a['Date'].dt.month
print(b)


# 23. Weekday Analysis: Create a boolean column Is_Weekend that flags whether an order was placed on a Saturday or Sunday.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Is_Weekend'] = a['Date'].dt.day_name().isin(['Saturday', 'Sunday'])
print(b)
print(a)

# 24. Date Filtering: Extract all transactions that occurred between 2026-02-01 and 2026-02-15.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a[(a['Date'] >= '2026-02-01') & (a['Date'] <= '2026-02-15').index]
print(b)

# 25. Chronological Sort: Sort the entire DataFrame chronologically by Date from oldest to newest.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.sort_values(by='Date', ascending=True, inplace=True, ignore_index=True)
print(b)