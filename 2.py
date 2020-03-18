import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')
# clean the item_price column and transform it in a float
prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices 

# make the comparison
chipo10 = chipo[chipo['item_price'] > 10.00]
chipo10.head()

len(chipo10)
# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])

# select only the ones with quantity equals to 1
price_per_item = chipo_filtered[chipo_filtered.quantity == 1]

#
price_per_item = chipo_end[['item_name', 'item_price']]

# sort the values from the most to less expensive
price_per_item.sort_values(by = "item_price", ascending = False)
chipo.item_name.sort_values()

# OR

chipo.sort_values(by = "item_name")
chipo.sort_values(by = "item_price", ascending = False).head(1)
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]

len(chipo_salad)
chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)



