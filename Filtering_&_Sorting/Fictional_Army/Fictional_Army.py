# import the necessary libraries
import pandas as pd

# create a dataset
raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
    'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
    'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
    'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
    'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
    'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
    'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']
}

army = pd.DataFrame(raw_data)

# Set the 'origin' column as the index of the dataframe
army.set_index('origin', inplace=True)

# Print only the 'veterans' column
print("Veterans column:")
print(army['veterans'])
print()

# the 'veterans' and 'deaths' columns
print("Veterans and deaths columns:")
print(army[['veterans', 'deaths']])
print()

# Print the name of all the columns
print("Column names:")
print(army.columns.tolist())
print()

# Select the 'deaths', 'size', and 'deserters' columns from 'Maine' and 'Alaska'
print("Selected columns from 'Maine' and 'Alaska':")
print(army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']])
print()

# Select rows 3 to 7 and columns 3 to 6
print("Selected rows and columns:")
print(army.iloc[2:7, 2:6])
print()

# Select every row after the fourth row and all columns
print("Rows after the fourth row:")
print(army.iloc[4:])
print()

# Select every row up to the fourth row and all columns
print("Rows up to the fourth row:")
print(army.iloc[:4])
print()

# Select the 3rd column up to the 7th column
print("Selected columns:")
print(army.iloc[:, 2:7])
print()

# Select rows where 'deaths' is greater than 50
print("Rows where 'deaths' is greater than 50:")
print(army[army['deaths'] > 50])
print()

# Select rows where 'deaths' is greater than 500 or less than 50
print("Rows where 'deaths' is greater than 500 or less than 50:")
print(army[(army['deaths'] > 500) | (army['deaths'] < 50)])
print()

# Select all the regiments not named 'Dragoons'
print("Regiments not named 'Dragoons':")
print(army[army['regiment'] != 'Dragoons'])
print()

# Select the rows called 'Texas' and 'Arizona'
print("Rows 'Texas' and 'Arizona':")
print(army.loc[['Texas', 'Arizona']])
print()

# Select the third cell in the row named 'Arizona'
print("Third cell in the row 'Arizona':")
print(army.loc['Arizona'].iloc[2])
print()

# Select the third cell down in the column named 'deaths'
print("Third cell down in the column 'deaths':")
print(army['deaths'].iloc[2])
print()
