# import necessary libraries
import pandas as pd

# load dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')

# how many products cost more than 10.00$?
# first filter the item_price column to be float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# second, get the products with a price greater than $10
expensive_products = chipo[chipo['item_price'] > 10]
print("the number of products costing more than $10:", len(expensive_products))
print()

# what is the price of each item?
# first, divide the item price by the quantity to get the price of a single item
chipo['price_per_item'] = chipo['item_price'] / chipo['quantity']
# second, group the data by 'item_name' and calc the average price per item
average_prices = chipo.groupby('item_name')['price_per_item'].mean().reset_index()
print(average_prices)
print()

# sort by the name of the item
chipo = chipo.sort_values('item_name')
print(chipo.head(25))
print()
chipo = chipo.sort_index()

# what was the quantity of the most expensive item ordered?
# first, clac the total quantity of each item
item_quantity = chipo.groupby('item_name')['quantity'].sum().reset_index()
# second, find the item with the highest price
most_expensive_item = chipo[chipo['item_price'] == chipo['item_price'].max()]['item_name'].iloc[0]
# third, find the total quantity of the most expensive item
most_expensive_item_quantity = item_quantity[item_quantity['item_name'] == most_expensive_item]['quantity'].iloc[0]
print("total quantity of the most expensive item ordered:", most_expensive_item_quantity)
print()

# how many times was a Veggie Salad Bowl ordered?
Salad_quantity = item_quantity[item_quantity['item_name'] == 'Veggie Salad Bowl']['quantity'].iloc[0]
print("total quantity of Veggie Salad Bowl ordered:", Salad_quantity)
print()

# how many times did someone order more than one canned soda?
print("number of times someone ordered more than one Canned Soda:", len(chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)]))

