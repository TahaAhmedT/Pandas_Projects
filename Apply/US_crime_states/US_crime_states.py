# import the necessary libraries
import pandas as pd

# load dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
crime = pd.read_csv(url)

# what is the type of the columns
print("the data type of each column:")
print(crime.dtypes)
print()

# convert a data type of column Year to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
# set the year column as the index of the dataframe
crime = crime.set_index('Year')
print("the first 10 entries from this dataset after setting Year column as index:")
print(crime.head(10))
print()

# delete the Total column
crime = crime.drop(columns=['Total'])

# group the year by decades and sum the values
df_decades = crime.groupby(pd.Grouper(freq='10Y')).sum()

# find the most dangerous decade based on the highest sum of crimes
most_dangerous_decade = df_decades.sum(axis=1).idxmax()
print("most dangerous decade in US:", most_dangerous_decade)
