# import necessary libraries
import pandas as pd

# load dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url)

# selecting only the Goal column
print("Goal column:")
print(euro12['Goals'])
print()

# how many team participated in the Euro2012?
print("the number of teams participated in the Euro2012:", len(euro12.Team))
print()

# what is the number of columns in teh dataset?
columns_name = euro12.columns.to_list()
print("the number of columns in this dataset:", len(columns_name))
print()

# View only the columns Team, Yellow Cards and Red Cards
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("Team, Yellow Cards and Red Cards columns:")
print(discipline)
print()

# sort the teams by Yellow Cards
print("sorting teams by Yellow Cards:")
print(discipline.sort_values('Yellow Cards'))
print()

# sort the teams by Red Cards
print("sorting teams by Red Cards:")
print(discipline.sort_values('Red Cards'))
print()

# Calc the mean Yellow cards given per team
print("the mean Yellow Cards given per Team:", discipline['Yellow Cards'].mean())
print()

# filter teams that scored more than 6 goals
great_team = euro12['Team'][euro12['Goals'] > 6]
print("the teams that scored more than 6 goals:")
print(great_team)
print()

# select the teams that start with G
print("the teams that start with 'G':")
print(euro12[euro12['Team'].str.startswith('G')])
print()

# select the first 7 columns
print("the first 7 columns from this dataset:")
print(euro12.iloc[:, :7])
print()

# select all columns except the last 3
print("the last 3 columns from this dataset:")
print(euro12.iloc[:, -3:])
print()

# present only the shooting accuracy from England, Italy and Russia
# first, filter the dataset for England, Italy and Russia teams
teams = ['England', 'Italy', 'Russia']
filtered_df = euro12[euro12['Team'].isin(teams)]
# second, select only the 'Shooting Accuracy' column
shooting_accuracy = filtered_df[['Team', 'Shooting Accuracy']]
print("shooting accuracy for England, Italy and Russia:")
print(shooting_accuracy)
