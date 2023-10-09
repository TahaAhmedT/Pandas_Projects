# import the necessary libraries
import pandas as pd

# load the dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, delimiter='|')

# discover what is the mean age per occupation
mean_age_per_occupation = users.groupby('occupation')['age'].mean()
print("the mean age per occupation:")
print(mean_age_per_occupation)
print()

# discover the male ratio per occupation and sort it from most to least
male_count_per_occupation = users[users['gender'] == 'M'].groupby('occupation')['gender'].count()
total_count_per_occupation = users.groupby('occupation')['gender'].count()
male_ratio_per_occupation = (male_count_per_occupation / total_count_per_occupation).fillna(0)
male_ratio_per_occupation = male_ratio_per_occupation.sort_values(ascending=False)
print("the male ratio per occupation sorting from the most to the least:")
print(male_ratio_per_occupation)
print()

# calculate the min and max age for each occupation
min_age_per_occupation = users.groupby('occupation')['age'].min()
max_age_per_occupation = users.groupby('occupation')['age'].max()
print("the minimum age per each occupation:")
print(min_age_per_occupation)
print()

print("the maximum age per each occupation:")
print(max_age_per_occupation)
print()

# calculate the mean age for each combination of occupation and gender
mean_age_per_occupation_gender = users.groupby(['occupation', 'gender'])['age'].mean()
print("the mean age for each combination of occupation and gender:")
print(mean_age_per_occupation_gender)
print()

# calculate the percentage of women and men for each occupation
total_count_per_occupation_gender = users.groupby(['occupation', 'gender'])['gender'].count()
percentage_per_occupation_gender = (total_count_per_occupation_gender / total_count_per_occupation).fillna(0) * 100
percentage_per_occupation_gender = percentage_per_occupation_gender.unstack()
print("the percentage of women and men for each occupation:")
print(percentage_per_occupation_gender)
