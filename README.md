## Note d'intention

> Travail sur la visualisation des données des manuscrits et copies de manuscrits de l'oeuvre monumentale de Llull. 

BLABLABLABLABLABLA 

En effet, il y a de nombreuses références de manuscrits, éparpillés dans le monde. Frances Yates évoque la difficulté de s'y retrouver dans son livre sur Lulle et Giordano Bruno. La visualisation peut aider le chercheur à organiser, éventuellement voir l'écologie archivistique de l'oeuvre lullienne, par exemple en découvrant les différents lieux de conservation et différentes dates d'édition d'un même manuscrit.

J'ai pris cette thématique car j'ai de l'affection pour l'oeuvre lullienne, sa diversité; mais aussi parce que, en clin d'oeil à la thématique du cours, Lulle fait figure de pionnier dans le travail de visualisation d'élément à valeur épistémiques (Johanna Drucker, mais informatique); mais aussi parce que le site manque de clarté. Un travail cartographique semble adapté.

> Biblio

C'est donc un travail sur les fonds d'archives et de bibliothèques qui m'intéresse; et sur l'**éparpillement des manuscrits**, au contenu différents ou non dont c'est l'objet.

L'intérêt de ma proposition est je pense dans la **démarche** d'apprendre python les dataframe. Je suis dans une optique d'apprendre, de le faire en expérimentant, non pas d'utiliser des applications dont l'utilisation me rapprocherait peut être davantage du design graphique qu'une démarche d'analyse des données. Ce travail pourrait être plus abouti, mais il est le signe d'un intérêt pour l'approche numérique de questions patrimoniales.

Un site internet avec toutes les données; mais difficile de lire l'information, de naviguer entre différents onglets (faut cliquer et recliquer). Un travail de visualisation s'impose donc.

> [Par pays : Base de Dades Ramon Llull](https://www.ub.edu/llulldb/manuscrits/pais#ca)
> 
> [Par oeuvre Base de Dades Ramon Llull](https://www.ub.edu/llulldb/obres)
> 
> [Par lieu de composition : Base de Dades Ramon Llull](https://www.ub.edu/llulldb/obres/lloc)
> 
> [Catalogue : Base de Dades Ramon Llull](https://www.ub.edu/llulldb/obres/cioarl)

- Nodes = **a) lieux de conservation** + b) manuscrits. 
  
  - a) weight = nombre de manuscrits conservés
  
  - b) weight = nombre de villes ou sont conservés ce manuscrit

- Edges
  
  - différents lieux de conservation peuvent êtres liés ensembles car ils conservent le même contenu.
  
  - source : identifiant du manuscrit; target = différents lieux de conservation; type null; label : nom manuscrit; poids = à voir

## Etablir le jeu de données à partir des tables html du site Lulle bdd et des liens

Pas de jeux de données en point csv prêt à l'emploi. Mais à partir des tableaux présents sur le site (catalogue et à partir des listes par pays) on peut établir un jeu de données.

[Extraire les données d&#8217;un tableau HTML &#8211; Tekipaki](https://tekipaki.hypotheses.org/14)

### Récupérer les données du HTML avec python (Soup)

1. enregistrer la page HTML de la listes de pays qui ont des manuscrits

2. récupérer tableaux des HTML avec pandas

3. clean tableau

4. export csv

5. utilisation geocodeur pour latitudes/longitudes à partir du csv

6. Problème : Nomimachin pas suffisament précis pour rechercher certaines instittions : deux solutions possibles : google maps api, api chat gpt; ou encore scraper données URL google maps; ou encore compléter avec données cherchées à la main; ou encore demander via un prompt. Je pourrais le faire, mais je me contente des données obtenues + éventuellement croisement avec les data ouvertes de Catalogne

### Créer un jeu de données géopgraphique avec geopy

Il y a plus de 100 lieux de conservation. Etablir les données GPS à la main prendrait bcp du temps. Avec un csv basique et un probgramme en python, on peut ajouter automatiquement ces données.

Aller plus loin :

Critique data display/data visualisaiton johanna Drucker

Limite des données non-ouvertes, sans format csv : compliquer d'extraire; besoin d'avoir plus de données : exemple origination des manuscrits pour faire une étude de la diffusion des manuscrits lullien selon leurs date, ce qui pourrait être intéressant pour étudier l'influence du lullisme en europe; puis les procédures de captation des documents par des institutios.

; date de versement des mansucrits

### échelle et expressivité des rapports

Les échelles de type affine nuisent, dans mon cas, à la lisibilité de la carte étant donné la majorité de villes avec peu de manuscrits (moins de 10) et quelques unes avec plus de 100. Entre 1 et 100 manuscrit, l'echelle des rayons est d'un rapport 1/100. Grands écarts qui se répercutent dans la visualisation.

 ça peut être 1 pixel vs 100; ou même $ax + b$ peu importe, c'est affine.

![](C:\Users\joelf\Downloads\Screenshot%202024-05-29%20at%2023-15-40%20Screenshot.png)

Je veux donc donc "écraser" l'expressivité des grands nombres pour gagner en lisibilité... sans pour autant rejeter cette expressivité entre des "petits ensembles" (moins d'une dizaine), des "ensembles moyens" (une ou deux dizaines) et "grands ensembles" (poignée de dizaines jusqu'à dépasser la centaine). 

![Screenshot 2024-05-29 at 22-54-53 Traceur de courbes.png](C:\Users\joelf\Downloads\Screenshot%202024-05-29%20at%2022-54-53%20Traceur%20de%20courbes.png)

Par exemple 60 et 80 manuscrits c'est le même *ordre de grandeur*. Mais je veux marquer la différence entre 2/3 et 6/7 manuscrits, mais amortir entre 60 et 80 manuscrits.Il faut donc une fonction qui croît vite au début; et qui s'écrase en tendant vers les grands nombres pour que les rayons de mes cercles ne soient pas trop gros. L'idée est d'exprimer un *ordre de grandeur*.

Pour rendre cette expressivité, j'ai tout de suite pensé à la fonction logarithme, avec un facteur et un + 1 pour qu'elle soit définie dans N strictement positif.

$f(x) = 1\ +\ln\left(x\right)\cdot n$

Pour n = 10

$g(x) = \sqrt{\left(x\right)} \cdot n$

N = variable "esthétique"

On veut des variables définies sur R[1;+infini]

La fonction f logarithmique garde une grande expressivité sous la quarantaine de manuscrits par rapport à la fonction identité dans les petites quantité (regarder du côté de paris); elle atténue avec force les "grands" nombres. Le contraste est donc fort entre très peu de manuscrit et beaucoup; mais modéré entre une quantité moyenne de manuscrit et beaucoup de manuscrit

> Calculer Moyenne et médiane.

![](C:\Users\joelf\Downloads\Screenshot%202024-05-29%20at%2023-16-14%20Screenshot.png)

> Fonction ln

Avec la fonction racine carré pour atténuer la taille des grands ensembles : Sensible à la variation pour des petits entiers; et variation atténuée, modeste, pour de très grands ensembles. Peu importe si pour 100 ou 120 manuscrits, le rapport d'agrandissement est moins sensible, "plus écrasé" que pour 1 et 5. 

Belle expressivité car un écrasement modéré et donc un contraste qui persiste sans pour autant "exagérer". (Il faut comparer avec la fonction identité). Le contrastre est bien marqué; mais modère le "tempérament" de la fonction identité qui, dans ce cas très précis, croit bcp trop vite par rapport à mon jeu de données. évidemment, en dehors de cette exercice que la fonction identité croit lentement par rapport à la fonction carrée ou à celle exponentielle.

![](C:\Users\joelf\Downloads\Screenshot%202024-05-29%20at%2023-16-39%20Screenshot.png)

> fonction racine carrée. Regarder à Paris pour comparer. 

Je choisis la fonction racine carré, car elle garde de l'expressivité. Ici, bien sûr, ce choix est esthétique. 

> Vérifier ce choix par rapport à moyenne/médiane.

Le but de la visualisation, c'est de *donner à voir* une information. Qu'entre 100 et 120 manuscrits on ne voit pas vraiment de différence, cela importe peu; l'information c'est "beaucoup". En revanche, entre 1, 5, et 10 manuscrits, il y a une différence qui mérite d'être vue et explicitée. La différence doit rendre avant tout sensible qu' "un unique exemplaire", une "petite quantité", "une dizaine", une centaire et un millier soi.

Si le rapport de grandeur entre 100 et 1200 manuscrits (imaginons) est plus écrasée que pour 1 et 5, cela n'est pas grave, et pour des besoins de lisibilité de la carte, il m'a semble que l'échelle racine carrée, avec un rapport homothétique de 4,

|                      | 1 manuscrit | 50 manuscrits | 100 manuscrits | rapport des bornes |
| -------------------- | ----------- | ------------- | -------------- | ------------------ |
| f(x) = x             | 1 px        | 25 px         | 100 px         | 1/100              |
| f(x) = $\sqrt(x)* 4$ | 4 px        | ~28 px        | 40 px          | 1/10               |

![](C:\Users\joelf\Downloads\Screenshot%202024-05-28%20at%2018-38-45%20Traceur%20de%20courbes.png)

### Limites

Données relationnelles peu intéressantes; je pensais avoir plus de liens, de copies. Mais ce n'est pas le cas. Cela m'a appris en tout cas que les références des mansucrits sont assez uniques. Je ne pouvais pas le savoir en amont. Et j'anticipe : ce n'est pas une erreur : en effectuant des recherches sur le tableur : effectivement peu de copies. J'aurais pu le vérifier avant : mais au moins j'ai mon programme qui pourra me resservir pour un travail ultérieur.

On voit aussi l'importance des données ouvertes : l'extraction est un moyen de contourner les problèmes; mais cela peut rajouter des marges d'erreur dans l'extraction.
