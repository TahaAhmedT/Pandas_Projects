# importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# loading the dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv'
titanic = pd.read_csv(url)

# setting PassengerId as the index
titanic.set_index('PassengerId', inplace=True)

# Creating a pie chart presenting the male/female proportion
male_female = titanic['Sex'].value_counts().tolist()
Sex_labels = ['male', 'female']

plt.figure(figsize=(8, 6))
plt.pie(male_female, labels=Sex_labels, autopct='%1.2f%%')
plt.title("Males and Females Proportion")
plt.show()

# Creating a scatter plot with the fare payed and the age, differ the plot color by gender
gender_color = {'female': 'red', 'male': 'blue'}

plt.figure(figsize=(8, 6))
plt.scatter(titanic['Fare'], titanic['Age'], c=titanic['Sex'].map(gender_color))
plt.xlabel("Fare")
plt.ylabel("Age")
plt.title("Relationship between Fare and Age")
plt.show()

# how many people survived?
survived_notsurvived = titanic['Survived'].value_counts().tolist()
survived_label = ['Not Survived', 'Survived']

plt.figure(figsize=(8, 6))
plt.pie(survived_notsurvived, labels=survived_label, autopct='%1.2f%%')
plt.title("Survived and not Survived people")
plt.show()

# Creating a histogram with the Fare payed
plt.figure(figsize=(8, 6))
plt.hist(titanic['Fare'], rwidth=0.9, bins=5)
plt.xlabel("Fare Payed")
plt.ylabel("Frequency")
plt.title("Fare Payed and its Frequencies")
plt.show()
