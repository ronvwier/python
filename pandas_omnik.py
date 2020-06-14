'''
Read OMNIK inverter excel sheets with pandas

Just a test script
'''

import pandas as pd

def fill_hour(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df['Hour'] = df['Time'].str[7:9]
    #df['Hour'] = df['Hour'] +1
    return df


# Read the input excel files skip 8 header lines
df = pd.read_excel('pandas_omnik.xlsx', skiprows=8 , skipfooter=3)

df2 = df.rename(columns={"Time(GMT +1)": "Time"})
df3 = fill_hour(df2)
df4 = df3.set_index(['Hour','Time'])
print(df4.max(level='Hour'))
