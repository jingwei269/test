import folium
import pandas
     
data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
     
html = """<h4>Volcano information:</h4>
Height: %s m
"""
     
map = folium.Map(location=[48.77, -120.59], zoom_start=6)
fg = folium.FeatureGroup(name = "My Map")
     
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
     
map.add_child(fg)
map.save("Map_html_popup_advanced.html")