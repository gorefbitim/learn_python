import pandas as pd
baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()
baby_names.head(10)
# deletes Unnamed: 0
del baby_names['Unnamed: 0']

# deletes Unnamed: 0
del baby_names['Id']

baby_names.head()
baby_names['Gender'].value_counts('F')
# you don't want to sum the Year column, so you delete it
# del baby_names["Year"]

# group the data
names = baby_names.groupby("Name").sum()

# print the first 5 observations
names.head()

# print the size of the dataset
print names.shape

# sort it from the biggest value to the smallest one
names.sort_values("Count", ascending = 0).head()
# as we have already grouped by the name, all the names are unique already. 
# get the length of names
len(names)
names.Count.idxmax()

# OR

# names[names.Count == names.Count.max()]
len(names[names.Count == names.Count.min()])
names[names.Count == names.Count.median()]
names.Count.std()
names.describe()
