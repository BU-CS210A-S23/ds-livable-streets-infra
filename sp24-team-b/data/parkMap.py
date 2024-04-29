import folium
import json

# Load the GeoJSON data
with open('Boston_Neighborhoods.geojson') as f:
    data = json.load(f)

# Create a map centered around Boston
map = folium.Map(location=[42.3601, -71.0589], zoom_start=11)

folium.GeoJson(
    data,
    style_function=lambda feature: {
        'fillColor': '#000000',  # or any color you want for the fill
        'color': 'None',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.2,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('esplanade.geojson') as f:
    esplanade_data = json.load(f)
    
folium.GeoJson(
    esplanade_data,
    style_function=lambda feature: {
        'fillColor': '#FF0000',  # or any color you want for the fill
        'color': '#FF0000',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('jamaicaPond.geojson') as f:
    jamaicaPond_data = json.load(f)
    
folium.GeoJson(
    jamaicaPond_data,
    style_function=lambda feature: {
        'fillColor': '#66FF00',  # or any color you want for the fill
        'color': '#66FF00',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('olmstedPark.geojson') as f:
    olmsted_data = json.load(f)
    
folium.GeoJson(
    olmsted_data,
    style_function=lambda feature: {
        'fillColor': '#BC13FE',  # or any color you want for the fill
        'color': '#BC13FE',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('roseKennedy.geojson') as f:
    roseKennedy_data = json.load(f)
    
folium.GeoJson(
    roseKennedy_data,
    style_function=lambda feature: {
        'fillColor': '#FFFF00',  # or any color you want for the fill
        'color': '#FFFF00',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('southwest.geojson') as f:
    southwest_data = json.load(f)
    
folium.GeoJson(
    southwest_data,
    style_function=lambda feature: {
        'fillColor': '#FF5722',  # or any color you want for the fill
        'color': '#FF5722',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('franklin.geojson') as f:
    franklin_data = json.load(f)
    
folium.GeoJson(
    franklin_data,
    style_function=lambda feature: {
        'fillColor': '#FF007F',  # or any color you want for the fill
        'color': '#FF007F',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('backbay.geojson') as f:
    backbay_data = json.load(f)
    
folium.GeoJson(
    backbay_data,
    style_function=lambda feature: {
        'fillColor': '#0000FF',  # or any color you want for the fill
        'color': '#0000FF',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)

with open('muddyRiver.geojson') as f:
    muddy_data = json.load(f)
    
folium.GeoJson(
    muddy_data,
    style_function=lambda feature: {
        'fillColor': '#B46400',  # or any color you want for the fill
        'color': '#B46400',  # set a valid color for the boundary
        'weight': 2,  # set a positive number for the weight
        'fillOpacity': 0.85,  # you can adjust the fill opacity here
    }
).add_to(map)
# Save the map as an HTML file
map.save('output_map.html')