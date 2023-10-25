# importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# load the dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')

# seeing the first 10 entries
print("the first 10 entries from this dataset:")
print(chipo.head(10))
print()

# creating a histogram of the top 5 items bought
# first, get the Series of the names
x = chipo.item_name
# second, use the counter class from collections to create a dictionary with keys(text) and frequency
letter_counts = Counter(x)
# third, convert the dictionary to a Dataframe
df = pd.DataFrame.from_dict(letter_counts, orient='index')
# fourth, sort the values from the top to the least value and slice the first 5 items
df = df[0].sort_values(ascending=True)[45:50]
# fifth, create the plot
df.plot(kind='bar')
# sixth, set title adn labels
plt.xlabel("Items")
plt.ylabel("Number of Times Ordered")
plt.title("Most ordered Chipotle\'s Items")
# finally, show the plot
plt.show()

# create a list of prices
# first, strip the dollar sign and trailing space
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price]
# second, groupby the orders and sum
orders = chipo.groupby('order_id').sum()
# third, create the scatterplot
plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')
# fourth, set the title and labels
plt.xlabel("Order Price")
plt.ylabel("Items ordered")
plt.title("Number of items ordered per order price")
plt.ylim(0)
plt.show()
