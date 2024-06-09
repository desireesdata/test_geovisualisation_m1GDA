import pandas as pd
import numpy as np
'''
villes = pd.read_csv("01_data.csv")
for i in range(len(villes)):
    if i+1 < len(villes) and villes.loc[i, "Biblioteca"] == villes.loc[i+1, "Biblioteca"]:
        print("identique !", villes.loc[i, "Ciutat"])
        villes.loc[i, "Manuscrits"] =  villes.loc[i, "Manuscrits"] + " - " + villes.loc[i+1, "Manuscrits"]
        villes.loc[i+1, "Fusion"] = "fusionné"
  
villes.to_csv("villes_fusion.csv")
'''
### SERT à nettoyer les données
villes = pd.read_csv("01_data.csv")
df_merged = villes

## df_merged = villes.groupby('Biblioteca').apply(concat_manuscrits, include_groupes=False)
### villes.to_csv("villes_fusion.csv")
df_merged['label_complet'] = df_merged['Ciutat'] + " - " + df_merged['Biblioteca']
df_merged = villes.groupby(["Biblioteca", "Ciutat"])['Manuscrits'].apply(lambda x: "%s" % ', '.join(x))
df_merged.to_csv("02_fusion.csv")