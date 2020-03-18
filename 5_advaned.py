import pandas as pd
url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)
df.head()
# weekly data
df = df.set_index('Date')
df.head()
df.index
# it is a 'object' type
df.index = pd.to_datetime(df.index)
type(df.index)
monthly = df.resample('M').sum()
monthly
monthly = monthly.dropna()
monthly
year = monthly.resample('AS-JAN').sum()
year
