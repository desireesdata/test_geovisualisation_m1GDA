import pandas as pd
from math import *
import folium

data = pd.read_csv("master_nodes_edges.csv")
rows = len(data.axes[0])
x = data.loc[0, "lat"]
y = data.loc[0, "lng"]
print(x, y)
m = folium.Map(location=(48, 11), zoom_start=5.5)

### NODES ###
group_1 = folium.FeatureGroup("Institutions Patrimoniales").add_to(m)
test = 0
while test < rows:
    #print(test, data.loc[test, "Biblioteca"])
    folium.CircleMarker(
        fill=True,
        radius=sqrt(int(data.loc[test, "weight"]))*4,
        #radius=log(int(data.loc[test, "nombre_manuscrits"]))*10,
        #radius=int(data.loc[test, "nombre_manuscrits"]),
        location=[data.loc[test, "lat"], data.loc[test, "lng"]],
        tooltip=data.loc[test, "Biblioteca"] + ", " + data.loc[test, "Ciutat"],
        popup="Manuscrit(s) disponible(s) : " + data.loc[test, "Manuscrits"],
        #icon=folium.Icon(icon="book"),
    ).add_to(group_1)
    test+=1

### EDGES ###
group_2 = folium.FeatureGroup("Villes partageant la même référence de manuscrit").add_to(m)
for i in range(len(data)-1):
    print(len(data["Edges"].iloc[i].split(",")))
    if len(data["Edges"].iloc[i].split(","))>= 2:
        identifiants = data["Edges"].iloc[i].split(",")
        print(identifiants)
        locations = [
            [data["lat"].iloc[int(identifiants[0])],
             data["lng"].iloc[int(identifiants[0])]],
            [data["lat"].iloc[int(identifiants[1])],
             data["lng"].iloc[int(identifiants[1])]]
        ]
        #locations = [[data['lat'].iloc[i], data['lng'].iloc[i]], [data['lat'].iloc[i+1], data['lng'].iloc[i+1]]]
        print(data["Biblioteca"].iloc[int(identifiants[1])])
        folium.PolyLine(locations=locations, color="red", stroke=0.2).add_to(group_2)
        folium.CircleMarker(
            fill=True,
            radius=int(data["weight"].iloc[int(identifiants[0])])*2,
            location=[data["lat"].iloc[int(identifiants[0])], data["lng"].iloc[int(identifiants[0])]],
            popup=data["Biblioteca"].iloc[int(identifiants[0])]
        ).add_to(group_2)
        folium.CircleMarker(
            fill=True,
            radius=int(data["weight"].iloc[int(identifiants[1])])*2,
            location=[data["lat"].iloc[int(identifiants[1])], data["lng"].iloc[int(identifiants[1])]],
            popup=str(data["Biblioteca"].iloc[int(identifiants[1])])
        ).add_to(group_2)
    #locations = [[data['lat'].iloc[i], data['lng'].iloc[i]], [data['lat'].iloc[i+1], data['lng'].iloc[i+1]]]
    #folium.PolyLine(locations=locations, color="red", stroke=0.2).add_to(m)

##################################
folium.LayerControl().add_to(m)
m.save("index.html")
