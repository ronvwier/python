import requests, pandas as pd
r = requests.get('https://www.ecdc.europa.eu/en/cases-2019-ncov-eueea')
dfs = pd.read_html(r.text)
print(dfs[0])