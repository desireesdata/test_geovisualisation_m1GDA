from bs4 import BeautifulSoup as soup
import pandas as pd

#### TRANSFORME PDF en CSV Brut de données non géocodées. Problème : doublons (exemple Berlin)

with open("manuscrit_pais.html", "rb") as f:
        html_doc = f.read()
data = soup(html_doc, "html.parser")  

tables = pd.read_html(html_doc, encoding='utf-8')
print(tables[3])

list_concat = []
for i in tables:
        list_concat.append(i)
lines = pd.concat(list_concat)
# lines = lines.drop_duplicates()
lines.to_csv("01_data.csv")
villes = lines.iloc[:, :-3]
# villes = villes.drop_duplicates()
#### Crée données, mais peu propres : doublons à cause de la ligne fonds
villes.to_csv("01_villes_master.csv")
