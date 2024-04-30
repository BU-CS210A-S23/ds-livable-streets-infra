import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# List of file names for the additional files
file_names = ['incomeR2022.csv']

# Read each CSV file and store the DataFrames in a list
data_frames = []
for file_name in file_names:
    df = pd.read_csv(file_name)
    data_frames.append(df)


grouped_dfs = []
for df in data_frames:
    grouped_df = df.groupby('Zip Code').sum().reset_index()
    grouped_dfs.append(grouped_df)

# Concatenate the grouped DataFrames into a single DataFrame
combined_df = pd.concat(grouped_dfs)

# Group the combined DataFrame by zip code and sum the total units for rent and income-restricted units
final_df = combined_df.groupby('Zip Code').sum().reset_index()

# Pivot the DataFrame to reshape it for the heatmap
pivot_df = final_df.pivot('Zip Code', 'Income-Restricted Rental', 'RentUnits')

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, cmap='viridis', annot=True, fmt='g', linewidths=0.5, linecolor='grey')
plt.title('Heatmap of Total Units for Rent and Income-Restricted Units by Zip Code')
plt.xlabel('Total Income-Restricted Rental Units')
plt.ylabel('Zip Code')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the heatmap as a PNG image
plt.savefig('heatmap.png')

plt.show()