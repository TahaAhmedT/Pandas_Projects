# import the necessary libraries
import pandas as pd

# create dataframe
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
            'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

regiment = pd.DataFrame(raw_data)

# what is the mean preTestScore from the regiment Nighthawks?
mean_preTestScore_for_Nighthawks = regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()
print("the mean preTestScore from the regiment Nighthawks:", mean_preTestScore_for_Nighthawks)
print()

# present general statistics by company
companies = regiment.groupby('company')
print("the general statistics by company:")
print(companies.describe())
print()

# what is the mean of each company's preTestScore?
print("the mean of each company's preTestScore:")
print(companies['preTestScore'].mean())
print()

# present the mean preTestScores grouped by regiment and company
regiment_company = regiment.groupby(['regiment', 'company'])
print("the mean preTestScore grouped by regiment and company:")
print(regiment_company['preTestScore'].mean())
print()

# present the mean preTestScores grouped by regiment and company without the heirarchical indexing
mean_scores_grouped = regiment.groupby(['regiment', 'company'], as_index=False)['preTestScore'].mean()
print("mean preTestScores grouped by regiment and company without heirarchical indexing:")
print(mean_scores_grouped)
print()

# what is the number of observations in each regiment and company
print("the number of observations in each group:")
for rc, data in regiment_company:
    print(rc)
    print("the number of observations:", len(data))
print()

# iterate over groups and print the name and the whole data from the regiment
for rc, data in regiment_company:
    print("name:", rc)
    print(data)
