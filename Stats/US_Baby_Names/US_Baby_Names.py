# import the necessary libraries
import pandas as pd

# load dataset
baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

# deleting the columns 'Unnamed: 0' and 'Id'
baby_names = baby_names.drop(columns=['Unnamed: 0', 'Id'])

# Seeing the first 10 entries
print("the first 10 entries from this dataset:")
print(baby_names.head(10))
print()

# checking if there are more male or female names in the dataset
gender_counts = baby_names['Gender'].value_counts()
more_common_gender = gender_counts.idxmax()
print("the gender with more names:", more_common_gender)
print()

# grouping the dataset by name and assign to names
names = baby_names.groupby('Name')

# counting the number of different names in the dataset
num_different_names = len(names)
print("the number of different names in this dataset:", num_different_names)
print()

# finding the name with the most occurrences
name_with_most_occurrences = names['Count'].sum().idxmax()
print("the name with the most occurrences:", name_with_most_occurrences)
print()

# counting the number of different names with the least occurrences
names_with_least_occurrences = names['Count'].sum().value_counts().min()
print("the names with the least occurrences:", names_with_least_occurrences)
print()

# finding the median name occurrences
# first, calculate the total occurrences for each name
name_occurrences = names['Count'].sum()
# second, find the median occurrences
median_occurrences = name_occurrences.median()
# third, get the name(s) with median occurrences
median_names = name_occurrences[name_occurrences == median_occurrences].index.tolist()
print("name(s) with median occurrences:", median_names)
print()

# calculating the standard deviation of names
std_names = names['Count'].sum().std()
print("the standard deviation of names:", std_names)
print()

# getting a summary with the mean, min, max, std, and quartiles
summary = names['Count'].sum().describe()
print("summary with the mean, min, max, std, and quartiles:")
print(summary)
