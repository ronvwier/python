'''
Read, combine and write excel sheets with pandas

Just a test script
'''

import pandas as pd

# Read the input excel files
seen = pd.read_excel('pandas_in.xlsx', sheet_name='seen', index_col='license')
owners = pd.read_excel('pandas_in.xlsx', sheet_name='owners', index_col='license')

# Create a result from seen and owners
all = seen.join(owners)
print(all)

# Write everything to a multisheet excel file
with pd.ExcelWriter('pandas_out.xlsx') as writer:  
    all.to_excel(writer, sheet_name='All')
    seen.to_excel(writer, sheet_name='Seen')
    owners.to_excel(writer, sheet_name='Owners')