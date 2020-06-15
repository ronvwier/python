'''
Read OMNIK inverter excel sheets with pandas

Read the OMNIK values and calculate max per hour
'''

import pandas as pd

# Read the input excel files skip 8 header lines
df = pd.read_excel('pandas_omnik.xlsx', skiprows=8 , skipfooter=3)

df2 = df.rename(columns={"Time(GMT +1)": "Time"})

# Calculate the hour and correct for summertime (GMT+2)
df2['Hour'] = df2['Time'].str[7:9].astype(int) +1

# Obtain the max values (Pac1 = power)
df4 = df2.set_index(['Hour','Time'])
print(df4.max(level='Hour'))
