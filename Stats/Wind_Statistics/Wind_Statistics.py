# import the necessary libraries
import pandas as pd
import datetime

# load the dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
data = pd.read_csv(url, sep='\s+', parse_dates=[[0, 1, 2]])
print("the last entries in this dataset:")
print(data.tail())
print()

# Year 2061? do we really have data from this year?
# Creating a function to fix it and apply it
def fix_year(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_year)

# setting the right dates as the index.
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data.set_index('Yr_Mo_Dy', inplace=True)
print("the dataset after setting a new index:")
print(data.head(5))

# compute how many values are missing for each location over the entire record
print("the number of missing values in each column:")
print(data.isnull().sum())
print()

# clac the mean windspeeds of the windspeeds over all the locations and all the times
mean_windspeed = data.mean().mean()
print("Mean windspeed:", mean_windspeed)
print()

# create loc_stats dataframe and calc min, max, mean and std of windspeeds at each location
loc_stats = pd.DataFrame()
loc_stats['min'] = data.min()
loc_stats['max'] = data.max()
loc_stats['mean'] = data.mean()
loc_stats['std'] = data.std()
print("the min, max, mean and std of windspeeds for each location:")
print(loc_stats)
print()

# create day_stats dataframe and calc min, max, mean and std of windspeeds across all locations for each day
day_stats = pd.DataFrame()
day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis=1)
day_stats['mean'] = data.mean(axis=1)
day_stats['std'] = data.std(axis=1)
print("the min, max, mean and std of windspeeds across all locations for each day:")
print(day_stats)
print()

# find the average windspeed in January for each location
average_January = data[data.index.month == 1].mean()
print("average windspeed in January for each loaction:")
print(average_January)
print()

# downsample the record to a yearly frequency for each location
yearly_data = data.resample('Y').mean()
print("Yearly Data:")
print(yearly_data.head())
print()

# downsample the record to a monthly frequency for each location
monthly_data = data.resample("M").mean()
print("Monthly Data:")
print(monthly_data.head())
print()

# downsample the record to a weekly frequency for each location
weekly_data = data.resample('W').mean()
print("Weekly Data:")
print(weekly_data.head())
print()

# calc min, max, mean and std of windspeeds across all locations for each week
weekly_stats = data['1961-01-02':'1961-12-31'].resample('W').agg(['min', 'max', 'mean', 'std'])
print("Weekly stats for the first 52 weeks:")
print(weekly_stats)


