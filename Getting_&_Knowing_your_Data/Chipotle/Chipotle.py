# import the necessary libraries
import pandas as pd

# load data from the website and store it in a dataframe
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')

# print the first 10 entries
print("the first 10 entries:")
print(chipo.head(10))
print()

# print the number of observations in the dataset, first method
print("the number of observation in the dataset:", len(chipo))
print()

# print the number of observations in the dataset, second method
print("the number of observation in the dataset:", chipo.shape[0])
print()

# print the number of columns in the dataset
print("the number of columns in the dataset:", chipo.shape[1])
print()

# print the name of all columns
columns_name = chipo.columns.to_list()
print("the name of all columns:")
print(columns_name)
print()

# how is the dataset indexed?
print("the manner that dataset indexed:")
print(chipo.index)
print()

# which was the most-ordered item?, and how many items were ordered for this item?
print("the most-ordered item is:", chipo['item_name'].value_counts().nlargest(1).index[0])
print("The number of times this item has been ordered is:", chipo['item_name'].value_counts().nlargest(1).values)
print()

# what was the most ordered item in the choice_description column?
print("the most-ordered item in the choice-description column is:")
print(chipo['choice_description'].value_counts().nlargest(1).index[0])
print()

# how many items were ordered in total?
print("the number of items were ordered in total:", chipo['item_name'].nunique())
print()

# turn the item price into a float
# first, display the current data type
print("the data type of item_price column before converting is:", chipo.dtypes['item_price'])
print()
# second, replace $ sign with '' to can convert the data type into float
chipo = chipo.replace({'item_price': '[$]'}, '', regex=True)

# third, covert the data type using lambda function
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x))

# finally, display the new data type
print("the data type of item_price column after converting is:", chipo.dtypes['item_price'])
print()

# how much was the revenue for the period in the dataset?
chipo['revenue'] = chipo['item_price'] * chipo['quantity']
print("the total revenue is:", chipo['revenue'].sum())

# how many orders were made in the period?
print("the number of orders were made:", chipo['order_id'].nunique())
print()

# what is the average revenue amount per order?
order_revenue = chipo.groupby('order_id')['revenue'].sum()
print("the average revenue amount per order:", order_revenue.mean())
print()

# how many different items are sold?
print("the number of different items that has been sold:", chipo['item_name'].nunique())
