import pandas as pd
import folium
import requests

file_path = 'incomeR2022.csv'
# Load data from CSV
data = pd.read_csv(file_path)

# Filter relevant columns
rent_data = data[['Zip Code', 'RentUnits', 'Income-Restricted Rental']]

# Group data by zip code and sum the number of rent units and income-restricted rental units
grouped_data = rent_data.groupby('Zip Code').sum().reset_index()


# Create a map centered around Boston
latitude = 42.3601
longitude = -71.0589
map_boston = folium.Map(location=[latitude, longitude], zoom_start=11)

# Add markers for each zip code
for index, row in grouped_data.iterrows():
    zip_code = str(int(row['Zip Code'])).zfill(5)  # Pad with leading zeros if necessary
    print(f"Processing zip code: {zip_code}")  # Print the zip code for verification
    url = f"https://nominatim.openstreetmap.org/search?postalcode={zip_code}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        if results:
            location = results[0]
            rent_units = int(row['RentUnits'])
            income_restricted_units = int(row['Income-Restricted Rental'])
            popup_text = f"Zip Code: {zip_code}\nRent Units: {rent_units}\nIncome-Restricted Rental Units: {income_restricted_units}"
            folium.Marker(
                location=[float(location['lat']), float(location['lon'])],
                popup=popup_text,
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(map_boston)
        else:
            print(f"No results for zip code: {zip_code}")
    else:
        print(f"Failed to retrieve data for zip code: {zip_code}")

# Save the map as an HTML file
map_boston.save('boston_rent_map.html')

