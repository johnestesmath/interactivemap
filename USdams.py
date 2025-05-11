import pandas as pd
import time
import folium
import geocoder

old_df = pd.read_csv('nation.csv', usecols=["Dam Name","Latitude","Longitude"])

df = old_df.dropna()



# create a map centered on average at and long
m = folium.Map(
    location=[df["Latitude"].mean(), df["Longitude"].mean()],
    zoom_start = 6,
    tiles = 'Esri.WorldTopoMap'
)

for _, row in df.iterrows():
    folium.Marker(
        location = [row['Latitude'], row['Longitude']],
        popup = row['Dam Name']
    ).add_to(m)

m



# for dam in us_dams_list:
#     time.sleep(1)
#     location = geocoder.osm(dam)

#     if location:
#         us_dams_dict['Dam'].append(dam)
#         us_dams_dict["Lattitude"].append(location.latlng[0])
#         us_dams_dict["Longitude"].append(location.latlng[1])
#     else:
#         not_found.append(dam)

# print(f"{len(us_dams_dict['Dam'])} found and {len(not_found)} not found.")
