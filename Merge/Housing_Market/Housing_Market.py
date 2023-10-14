# import the necessary libraries
import pandas as pd
import numpy as np

# create three different series
series1 = pd.Series(np.random.randint(1, 5, size=100))
series2 = pd.Series(np.random.randint(1, 4, size=100))
series3 = pd.Series(np.random.randint(10000, 30001, size=100))

# create a dataframe by joining the series by column
df = pd.concat([series1, series2, series3], axis=1)
print("the new dataframe:")
print(df.head())
print()

# change the name of the columns
df.columns = ['beds', 'bathes', 'price_per_meter']
print("the new dataframe after renaming its columns:")
print(df.head())
print()

# create a one-column dataframe with the values of the three series
bigcolumn = pd.concat([series1, series2, series3])
print("a new one column dataframe:")
print(bigcolumn.head())
print()

# check if it goes only until index 99
print("checking if it goes only until index 99:", bigcolumn.index.max() == 99)  # True
print()

# reindex the dataframe from 0 to 299
print("the bigcolumn dataframe after the reindexing:")
bigcolumn = bigcolumn.reset_index(drop=True).reindex(range(300))
print(bigcolumn)
