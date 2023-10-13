# import the necessary libraries
import pandas as pd
import numpy as np

# load the dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url)

# slice the dataframe from 'school' until the 'guardian' column
print("slicing the dataframe from 'school' until the 'guardian' column:")
print(df.iloc[:, :12])
print()

# create a lambda function that will capitalize strings, capitalize both Mjob and Fjob columns
print("the Mjob and Fjob columns before capitalizing:")
print(df[['Mjob', 'Fjob']])
print()
df['Mjob'] = df['Mjob'].apply(lambda x: x.capitalize())
df['Fjob'] = df['Fjob'].apply(lambda x: x.capitalize())
print("the Mjob and Fjob columns after capitalizing:")
print(df[['Mjob', 'Fjob']])
print()

# print the last elements of the dataset
print("the last 10 elements in this dataset:")
print(df.tail(10))
print()

# create a function to determine if a student is a legal drinker
def majority(age):
    return age > 17

df['legal_drinker'] = df['age'].apply(majority)
print("the first 10 element in the dataset after applying the majority function:")
print(df.head(10))
print()

# multiplying every number in the dataset by 10 (it does not make a sense but it just a try)
df = df.applymap(lambda x: x * 10 if isinstance(x, (int, float, np.number)) else x)
print("the first 10 element from the dataset after applying the multiplication function:")
print(df.head(10))
