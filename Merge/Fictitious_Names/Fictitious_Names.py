# import the necessary libraries
import pandas as pd

# raw data
raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}

raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}

raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}

# load datasets
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

# join the two dataframes along rows
all_data = pd.concat([data1, data2])

# join the two dataframes along columns
all_data_col = pd.concat([data1, data2], axis=1)

# print data3
print("Data3:")
print(data3)

# merge all_data and data3 along subject_id
merged_data = pd.merge(all_data, data3, on='subject_id')

# merge data1 and data2 with matching subject_id
merged_inner = pd.merge(data1, data2, on='subject_id')

# merge all values in data1 and data2
merged_outer = pd.merge(data1, data2, on='subject_id', how='outer')

# Print the results
print("\nMerged Data:")
print(merged_data)
print("\nInner Merge:")
print(merged_inner)
print("\nOuter Merge:")
print(merged_outer)
