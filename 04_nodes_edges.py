import pandas as pd
from math import *

data = pd.read_csv("master.csv")
########### INIT FOLIUM#######################

########## AJOUT POIDS et ID ########################
rows = len(data.axes[0])
data["weight"] = 0
data["identifiant"] = 0
n = 0
for i in range(rows):
    temp = []
    temp = data.loc[i, "Manuscrits"].split(", ")
    data.loc[i, "weight"] = len(temp)
    data.loc[i, "identifiant"] = str(n)
    n+=1
########### AJOUT EDGES #######################
grouped = data.groupby('Manuscrits')['identifiant'].transform(lambda x: ','.join(set(x)))
data['Edges'] = grouped

####
data.to_csv("master_nodes_edges.csv")