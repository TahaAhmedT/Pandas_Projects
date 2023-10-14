# import the necessary libraries
import pandas as pd
import numpy as np
# load dataset
cars1 = pd.read_csv('cars1.csv')
cars2 = pd.read_csv('cars2.csv')

# it seems our first dataset has some unnamed blank columns
cars1 = cars1.iloc[:, :9]

# what is the number of observation in each dataset?
print("the number of observation in first dataset:", cars1.shape[0])
print("the number of observation in second dataset:", cars2.shape[0])
print()

# join cars1 and cars2 into a single dataframe called cars
cars = pd.merge(cars1, cars2, on='mpg', how='inner')
print("the new merged dataframe:")
print(cars)
print()

# creating a new column called owners by create a random number Series from 15,000 to 73,000
owner_column = np.random.randint(low=15000, high=73000, size=(344, 1))

# adding it to the new dataframe
cars['owners'] = owner_column
print("the new dataframe after adding the owners column:")
print(cars.head(20))
