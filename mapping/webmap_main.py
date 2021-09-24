import folium
import pandas

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

    

def coordinates(locats):
    for lt,ln,el,name in locats:
         
        fg.add_child(folium.Marker(location=[lt,ln], radius = 6,  popup=name+"\n"+str(el)+" m", icon=folium.Icon(color=color_producer(el))))

# map = folium.Map(location=[31.36, 120.59], zoom_start=6,tiles = "Stamen Terrain")
map = folium.Map(location=[48.77, -120.59], zoom_start=6)


fg = folium.FeatureGroup(name="My Map")

df1 = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
lat = list(df1["LAT"])
lon = list(df1["LON"])
elev = list(df1["ELEV"])
name = list(df1["NAME"])

 

locations = list(zip(lat,lon,elev,name))

coordinates(locations)
fg.add_child(folium.GeoJson(data=(open('Webmap_datasources/world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(fg)
map.save("Map1.html")