import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')
chipo.head(10)
# chipo['choice_description'][4]
chipo.info()#

# OR

chipo.shape[0]
# 4622 observations
chipo.shape[1]
chipo.columns
chipo.index
chipo.item_name.value_counts().head(1)
mostOrd = chipo.item_name.value_counts().max() #or mostOrd = chipo["item_name"].max()
mostOrd
chipo.choice_description.value_counts().head()
total_items_orders = chipo.quantity.sum()
total_items_orders

dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

chipo.item_price.sum()
chipo.order_id.value_counts().count()

order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()['item_price']

# Or 

#chipo.groupby(by=['order_id']).sum().mean()['item_price']
chipo.item_name.value_counts().count()
