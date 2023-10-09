# import the necessary libraries
import pandas as pd

# load dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url)
print(drinks[['country', 'continent', 'wine_servings']].head(10))
print()

# which continent drinks more beer on average?
continent_drinks = drinks.groupby('continent')
print("the continents that drink more beer on average are:")
print(continent_drinks.sum()['beer_servings'].sort_values()[2:])
print()

# for each continent print the statistics for wine consumption
print("the statistics for wine consumption per continent:")
print(continent_drinks.describe()['wine_servings'])
print()

# print the median alcohol consumption per continent for every column
numeric_columns = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
median_alcohol_consumption = continent_drinks[numeric_columns].median()
print("median alcohol consumption per continent:")
print(median_alcohol_consumption)
print()

# print the mean, min, and max values for spirit consumption
spirit_consumption_stats = drinks['spirit_servings'].agg(['mean', 'min', 'max'])
print("spirit consumption statistics:")
print(spirit_consumption_stats)
