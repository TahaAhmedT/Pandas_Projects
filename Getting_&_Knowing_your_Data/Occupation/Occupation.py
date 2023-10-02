# import the necessary libraries
import pandas as pd

# load data from the website and store it in a dataframe
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, delimiter='|')

# set 'user_id' column as index
users = users.set_index('user_id')

# print the first 25 entries
print("the first 25 entries:")
print(users.head(25))
print()

# print the last 10 entries
print("the last 10 entries:")
print(users.tail(10))
print()

# what is the number of observations in the dataset
print("the number of observations in the dataset:", len(users))
print()

# what is the number of columns in the dataset
print("the number of columns in the dataset:", users.shape[1])
print()

# name of all the columns
print("the name of all the columns:")
print(users.columns.to_list())
print()

# how is the dataset indexed?
print("the manner that dataset indexed:")
print(users.index)
print()

# what is the data type of each column?
print("her is the data type of each column:")
print(users.dtypes)
print()

# print only the occupation column
print("occupation column:")
print(users['occupation'])
print()

# how many different occupations are in this dataset?
print("the number of different occupations in this dataset: ", users['occupation'].nunique())
print()

# what is the most frequent occupation?
print("the most frequent occupation is:", users['occupation'].value_counts().index[0])
print()

# summarize the dataframe
print("summarizing the dataframe:")
print(users.info())
print()

# summarize all the columns
print("summarizing all columns:")
print(users.describe(include='all'))
print()

# summarize only the occupation column
print("summarizing occupation column:")
print(users['occupation'].info())
print()

# what is the mean age of users?
print("the average age of users is:", users['age'].mean())
print()

# what is the age with the least occurrence?
print("the age with the least occurrence is:", users['age'].value_counts().index[users['age'].nunique() - 1])
