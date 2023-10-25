# importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# loading the dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv'
tips = pd.read_csv(url)

# deleting the Unnamed 0 column
tips = tips.drop(['Unnamed: 0'], axis=1)

# Plotting the total_bill column histogram
plt.hist(tips['total_bill'], rwidth=0.9, bins=5)
plt.xlabel("Total Bills")
plt.ylabel("Number of Occurrences")
plt.title("Total Bills Histogram")
plt.show()

# creating a scatter plot presenting the relationship between total_bill and tip
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel("Total Bills")
plt.ylabel("Tips")
plt.title("Relationship between the Total Bills and the Tips")
plt.show()

# Creating one image with the relationship of total_bill, tip and size
plt.scatter(tips['total_bill'], tips['tip'], label='tip')
plt.scatter(tips['total_bill'], tips['size'], label='size')
plt.title("Relationship between Total Bills, Tip and Size")
plt.legend()
plt.show()

# presenting the relationship between days and total_bill value
plt.figure(figsize=(8, 6))
plt.bar(tips['day'], tips['total_bill'])
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.title("Relationship between Days and Total Bill")
plt.show()

# creating a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex
plt.figure(figsize=(8, 6))
colors = {'Male': 'blue', 'Female': 'red'}
plt.scatter(tips['tip'], tips['day'], c=tips['sex'].map(colors))
plt.xlabel('Tip')
plt.ylabel("Day")
plt.title("Tip vs Day (Differentiated by sex)")
plt.legend(colors)
plt.show()

# Drawing a Box plot of total_bill per day, differentiated by time
plt.figure(figsize=(8, 6))
tips['time_day'] = tips['time'] + '_' + tips['day']
ax = tips.boxplot(column='total_bill', by='time_day')
plt.xlabel('Time and Day')
plt.ylabel('Total Bill')
plt.title('Total Bill per Day (Differentiated by Time)')
plt.suptitle('')
plt.show()

# presenting a histograms of tip value for Dinner and Lunch (side by side)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(tips[tips['time'] == 'Dinner']['tip'], bins=10, color='blue', alpha=0.5)
plt.xlabel('Tip')
plt.ylabel('Frequency')
plt.title('Histogram of Tip for Dinner')

plt.subplot(1, 2, 2)
plt.hist(tips[tips['time'] == 'Lunch']['tip'], bins=10, color='red', alpha=0.5)
plt.xlabel('Tip')
plt.ylabel('Frequency')
plt.title('Histogram of Tip for Lunch')

plt.tight_layout()
plt.show()

# Scatter plot of total_bill vs tip, differentiated by gender and smoker status (side by side)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(tips[tips['sex'] == 'Male']['total_bill'], tips[tips['sex'] == 'Male']['tip'], c=tips[tips['sex'] == 'Male']['smoker'].map({'Yes': 'blue', 'No': 'red'}), label='Male')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs Tip for Male')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(tips[tips['sex'] == 'Female']['total_bill'], tips[tips['sex'] == 'Female']['tip'], c=tips[tips['sex'] == 'Female']['smoker'].map({'Yes': 'blue', 'No': 'red'}), label='Female')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs Tip for Female')
plt.legend()

plt.tight_layout()
plt.show()
