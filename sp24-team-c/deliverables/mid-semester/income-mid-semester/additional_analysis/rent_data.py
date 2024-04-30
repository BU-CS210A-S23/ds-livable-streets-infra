import pandas as pd
import matplotlib.pyplot as plt

file_path = 'gross_rent.csv'
rent_data = pd.read_csv(file_path)

# print(rent_data.columns)
# print(rent_data.head())

brookline_rent_data = rent_data[rent_data['municipal'] == 'Brookline']

brookline_rent_data['med_c_r'] = pd.to_numeric(brookline_rent_data['med_c_r'], errors='coerce')
brookline_rent_data.dropna(subset=['med_c_r'], inplace=True)

# Creating a pivot table for Brookline
pivot_brookline_rent_data = brookline_rent_data.pivot(index='municipal', columns='acs_year', values='med_c_r')

plt.figure(figsize=(10, 6))
# Plotting the median gross rent changes for Brookline
plt.plot(pivot_brookline_rent_data.columns, pivot_brookline_rent_data.loc['Brookline'], marker='o', label='Brookline')

plt.title('Median Gross Rent Changes in Brookline')
plt.xlabel('ACS Year Range')
plt.ylabel('Median Gross Rent ($)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# rent_data['med_c_r'] = pd.to_numeric(rent_data['med_c_r'], errors='coerce') 

# rent_data.dropna(subset=['med_c_r'], inplace=True) 

# pivot_rent_data = rent_data.pivot(index='municipal', columns='acs_year', values='med_c_r')

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10, 6))
# for municipality in pivot_rent_data.index:
#     plt.plot(pivot_rent_data.columns, pivot_rent_data.loc[municipality], marker='o', label=municipality)

# plt.title('Median Gross Rent Changes by Municipality')
# plt.xlabel('ACS Year Range')
# plt.ylabel('Median Gross Rent ($)')
# plt.legend(loc='best', fontsize='xx-small')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

