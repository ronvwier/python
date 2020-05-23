import pandas as pd

seen = pd.read_excel('pandas_in.xlsx', sheet_name='seen', index_col='license')
owners = pd.read_excel('pandas_in.xlsx', sheet_name='owners', index_col='license')

all = seen.join(owners)
print(all)

df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
print(df)

with pd.ExcelWriter('pandas_out.xlsx') as writer:  
    all.to_excel(writer, sheet_name='All')
    seen.to_excel(writer, sheet_name='Seen')
    owners.to_excel(writer, sheet_name='Owners')

#print(df.describe())