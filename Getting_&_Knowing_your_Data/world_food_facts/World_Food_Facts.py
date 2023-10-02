# import the necessary libraries
import pandas as pd

# read data file
food = pd.read_csv("en.openfoodfacts.org.products.tsv", sep='\t', low_memory=False)  # this file is over 100mb so I did not push it to the repo

# print the first 5 entries
print("the first 5 entries:")
print(food.head(5))
print()

# what is the number of observation in the dataset?
print("the number of observations in the dataset:", len(food))
print()

# what is the number of columns in the dataset?
print("the number of columns in the dataset:", food.shape[1])
print()

# print the name of all columns
print("the name of all columns:")
columns_name = food.columns.to_list()
print(columns_name)
print()

# what is the name of 105th column?
print("the name of the 105th column is:", columns_name[104])
print()
# what is the type of the observations of the 105th column?
print("the data type of 105th column is:", food.dtypes[columns_name[104]])
print()

# how is the dataset indexed?
print("the manner that dataset indexed:")
print(food.index)
print()

# what is the product name of the 19th observation?
print("the product name of the 19th observation is:", food.loc[food.index[18], 'product_name'])
print()
