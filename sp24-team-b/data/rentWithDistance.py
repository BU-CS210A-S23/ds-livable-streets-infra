import numpy as np
import matplotlib.pyplot as plt
from haversine import haversine

# Read data from text file
data = np.loadtxt('rentData.txt')

rent = data[:, 0]
longitude = data[:, 3]
latitude = data[:, 4]
bedrooms = data[:, 1]

esplanadeCenter = (42.354642609034514, -71.08090805089577)
jamaicaPondCenter = (42.317425074525474, -71.12082788871538)
backBayFensCenter = (42.34154391237527, -71.09570266263808)

centers = [["Esplanade", esplanadeCenter], ["Jamaica Pond", jamaicaPondCenter], ["Back Bay Fens", backBayFensCenter]]

radius = 1.5 # Radius in kilometers

# Initialize dictionary to store rents for each number of bedrooms
bedroom_prices = {}

# Iterate over unique number of bedrooms and filter data for each group
for center in centers:
    for num_bedrooms in range(6):
        # Filter data for the current number of bedrooms
        filtered_rent = []
        filtered_distances = []
        for rent_price, lon, lat, num_bed in zip(rent, longitude, latitude, bedrooms):
            if num_bed == num_bedrooms:
                distance = haversine(center[1], (lat, lon))
                if distance > radius:
                    continue
                filtered_rent.append(rent_price)
                filtered_distances.append(distance)
        bedroom_prices[num_bedrooms] = (filtered_distances, filtered_rent)

    # Plot lines for each number of bedrooms
    for num_bedrooms, (distances, rents) in bedroom_prices.items():
        sorted_indices = np.argsort(distances)
        sorted_distances = np.array(distances)[sorted_indices]
        sorted_rents = np.array(rents)[sorted_indices]
        plt.plot(sorted_distances, sorted_rents, label=f'{num_bedrooms} Bedroom(s)')

    plt.title('Rent Prices in a 1.5 km Radius from the Center of ' + center[0])
    plt.xlabel('Distance from Center (km)')
    plt.ylabel('Rent Price')
    plt.legend()
    plt.show()
