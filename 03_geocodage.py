import geopy
from geopy.geocoders import Nominatim
from geopy.geocoders import Bing
import pandas as pd

villes = pd.read_csv("02_fusion.csv")
geolocalisation = pd.DataFrame()

geolocator = Nominatim(user_agent="my_geocoder")
#location = geolocator.geocode("Biblioteca Nacional Russa, Russian Federation")
#print("Adresse:", location.address,"Latitude:", location.latitude, "Longitude:", location.longitude)

#################
ciutats = []
institutions = []
longitudes = []
latitudes = []

for i in range(len(villes)):
    ciutats.append(villes.loc[i, "Ciutat"])
    institutions.append(villes.loc[i, "Biblioteca"])

#len(ciutats))*
for i in range(0, len(villes)):
    #print(ciutats[i] + ", " + institutions[i])
    location = geolocator.geocode(institutions[i] + ", "+ ciutats[i], timeout=10)
    if location is None:
        print(institutions[i] + ", "+ ciutats[i])
        latitudes.append("non reconnu")
        longitudes.append("non reconnu")
    else:
        latitude = location.latitude
        longitude = location.longitude
        latitudes.append(latitude)
        longitudes.append(longitude)

geolocalisation["lat"] = latitudes
geolocalisation["lng"] = longitudes
print(geolocalisation.head())
geolocalisation.to_csv("03_villes_geocodees.csv")

##  Puis supprimer lignes, remplacer " - " par ", "
## c) ajouter id

