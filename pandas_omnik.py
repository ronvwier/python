'''
Read OMNIK inverter excel sheets

Read the OMNIK values and calculate max per hour
'''

import pandas as pd

# Read the input excel files skip 8 header lines
df = pd.read_excel('pandas_omnik.xlsx', skiprows=8 , skipfooter=3).rename(columns={"Time(GMT +1)": "Time"})

# Calculate the hour and correct for summertime (GMT+2)
df['Hour'] = pd.to_numeric(df['Time'].str[7:9]) +1

# Obtain the max values (Pac1 = power)
dfresult = df.set_index('Hour').filter(items=['Hour', 'Pac1']).max(level='Hour').reset_index()

hour_list = dfresult['Hour'].tolist()
print(hour_list)
power_list = dfresult['Pac1'].tolist()
print(power_list)