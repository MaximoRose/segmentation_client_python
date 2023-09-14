# Segmentation des clients d'un site de vente en ligne.

Pour ce projet, on nous a soumis un historique de ventes de plusieurs années d'une application de vente en ligne. L'application en question permet à ses revendeurs de poster des articles sur plusieurs market place distinctes.

L'objectif est de proposer une première segmentation des acheteurs et acheteuses, puis de chiffrer une prestation de maintenance réaliste, en fonction du _drift_ des données.

Nous allons fonc séparer notre travail en trois étapes accessibles dans trois Jupyter Notebook différents :
1. Une analyse exploratoire des données
2. Une catégorisation non supervisée des acheteurs avec différents algorithmes
3. Una analyse de l'effet du _drift_ des données sur notre clusterisation pour estimer une fréquence de maintenance.


## 1. Analyse exploratoire des données.
Fichier : __0_Analyse_Des_Donnees.ipynb__

Une analyse exploratoire des données assez classique qui permet de recomposer les liens entre les différentes tables du _dataset_.

![relations entre les tables](https://maximorose.eu/datascience_gh_ress/relations_dataset_projet_segmentation.png)

- On va estimer des indicateurs courants type "panier moyen" ou "temps moyen pour qu'un primo-acheteur devienne un client régulier".
- On réalise une première segmentation RFM qui permet de se faire une première idée, assez générique, des profils des acheteurs et acheteuses.

## 2. Segmentations des acheteurs et acheteuses.
Fichier : __1_Segmentation_DataScience.ipynb__

N.B : Le fichier s'ouvre difficilement dans GitHub, aussi une version HTML est disponible [ici](https://maximorose.eu/datascience_gh_ress/1_Segmentation_DataScience.html)

- On va explorer plusieurs algorithmes de clusterisation non supervisée : K-means, DBSCAN, CAH.
- On va travailler sur des dataset disposant de différentes _features_ et mesurer les silhouettes scores de nos différentes segmentations pour déterminer celles qui offrent les meilleurs résultats.
- On va etudier les _clusters_ identifiés et faire des _radar charts_ pour mieux comprendre le profil de nos acheteurs et acheteuses.
- On va réduire le nombre de dimensions avec t-SNE pour visualiser nos _clusters_.

## 3. Estimation d'une fréquence de maintenance.
Fichier : __2_Evolution_Temporelle_des_Clusters.ipynb__

- On va étudier le drift de nos données sur la base du _dataset_ fourni en étudiant l'évolution de l'ARI (_Adjusted Rand Index_) d'une clusterisation initiale avec le temps.
- On va calculer l'evolution de l'ARI de nos modeles pour estimer une frequence ad hoc de maintenance
