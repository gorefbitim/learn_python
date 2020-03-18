import numpy as np
import pandas as pd
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()
crime.info()
# pd.to_datetime(crime)
crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()
crime = crime.set_index('Year', drop = True)
crime.head()
del crime['Total']
crime.head()
# select the first two columns from the origional dataset
population = crime.iloc[:, 0:1]

# change the index for decades
population.index = (population.index.year//10)*10

# group the index by decades and selecting the max value from the Population column 
population1 = population.groupby(population.index).max()
population1

# group the dataframe by decades and sum all values, including population
crime = crime.groupby((crime.index.year//10)*10).sum()

# assing the right population value (max value) to the 
crime['Population'] = population1['Population']
crime
# apparently the 90s was a pretty dangerous time in the US
crime.idxmax(0)
f = lambda x: x.max() - x.min()

crime['Violent'].apply(f)
# crime.apply(f, axis=1)





