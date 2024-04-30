import pandas as pd
import matplotlib.pyplot as plt

# Load the income data CSV
income_data_path = 'Book2.csv'  # Adjust the path as necessary
income_data = pd.read_csv(income_data_path)


income_data['Median Income'] = pd.to_numeric(income_data['Median Income'].replace('[\$,]', '', regex=True), errors='coerce')
nan_rows = income_data[income_data['Median Income'].isna()]
# print(nan_rows)
low_income_threshold = 62843
high_income_threshold = 80000

def categorize_income(income):
    if income < low_income_threshold:
        return 'Low'
    elif income < high_income_threshold:
        return 'Medium'
    else:
        return 'High'
    
income_data['Income_Category'] = income_data['Median Income'].apply(categorize_income)


low = []
medium = []
high = []


for index, row in income_data.iterrows():
    if row['Unnamed: 0'] != 'United States' or row['Unnamed: 0'] != 'Massachusetts':
        if row['Income_Category'] == 'Low':
            low.append(row['Unnamed: 0'])
        elif row['Income_Category'] == 'Medium' and row['Unnamed: 0'] != "United States":
            medium.append(row['Unnamed: 0'])
        elif row['Income_Category'] == 'High' and row['Unnamed: 0'] != "Massachusetts":
            high.append(row['Unnamed: 0'])

print(low)
print(medium)
print(high)
# print(low)
# print(medium)
# print(high)
            
income_data.set_index('Unnamed: 0', inplace=True)


commute_datapath = 'means_of_commute.csv'  # Adjust the path as necessary
commute = pd.read_csv(commute_datapath)

# print(commute.columns)
# print(commute.index)

# merged_data = pd.merge(income_data, commute, on='')

merged_data = income_data.join(commute, lsuffix='_income', rsuffix='_commute')

# print(merged_data.columns)


#############

commute_perc = ['%_commute', '%.1_commute', '%.2_commute', '%.3_commute', '%.4_commute',
    '%.5_commute', '%.6_commute', '%.7_commute']
commute_methods = ['Car, truck, or van', 'Bus or trolley bus', 'Streetcar or trolley car', 'Subway or elevated', 'Railroad', 'Bicycle', 'Walked', 'Other']

# for method in commute_methods:
#     perc_column = method + '_perc'  # Adjust if the naming convention differs
#     merged_data[perc_column] = pd.to_numeric(merged_data[perc_column], errors='coerce')


# for method in commute_methods:
#     merged_data.groupby('Income_Category')[method + '_perc'].mean().plot(kind='bar', figsize=(10, 6), title=f'Percentage Using {method} by Income Category')
#     plt.ylabel('Percentage')
#     plt.show()

for column in commute_perc:
    # Remove the percentage sign at the end and divide by 100 to convert to a float percentage
    merged_data[column] = merged_data[column].str.rstrip('%').astype(float) / 100

merged_data['Income_Category'] = pd.Categorical(merged_data['Income_Category'], categories=['Low', 'Medium', 'High'], ordered=True)

for method_name, perc_column in zip(commute_methods, commute_perc):
    plt.figure(figsize=(10, 6))
    ax = merged_data.groupby('Income_Category')[perc_column].mean().plot(kind='bar')
    ax.set_title(f'Average Percentage Using {method_name} by Income Category')
    ax.set_ylabel('Average Percentage')
    plt.xticks(rotation=45)
    plt.show()


# print(merged_data)





