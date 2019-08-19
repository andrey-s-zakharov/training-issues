from folium import CircleMarker, Map
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv('Volcanoes_USA.txt')
lat = data.get('LAT')
lon = data.get('LON')
elevation = data.get('ELEV')

def color_change(elevation):
    if (elevation < 1000):
        return('green')
    elif (1000 <= elevation < 3000):
        return('orange')
    else:
        return('red')


map = Map(location=[37.296933, -121.9574983], zoom_start=5)

marker_cluster = MarkerCluster().add_to(map)

for lat, lon, elevation in zip(lat, lon, elevation):
    CircleMarker(
        location=[lat, lon],
        radius=9,
        popup='{} m'.format(str(elevation)),
        fill_color=color_change(elevation),
        color='gray',
        fill_opacity=0.9,
    ).add_to(marker_cluster)

map.save('map1.html')
