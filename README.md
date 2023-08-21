# Segmentation des clients d'un site de vente en ligne.

Pour ce projet, on nous a soumis un historique de vente de plusieurs annees d'une application de vente en ligne. L'application en question permet a ses revendeurs de poster des articles sur plusieurs market place distinctes.

L'objectif est de proposer une premiere segmentation des acheteurs et acheteuses, puis de chiffrer une prestation de maintenance realiste, en fonction du drift des donnees.

Nous allons fonc separer notre travail en trois etapes accessibles dans trois Jupyter Notebook differents :
1. Une analyse exploratoire des donnees
2. Une categorisation non supervisee des acheteurs avec differents algorithmes
3. Una analyse de l'effet du drift des donnees sur notre clusterisation pour estimer une frequence de maintenance.


## 1. Analyse exploratoire des donnees.
Fichier : 0_Analyse_Des_Donnees.ipynb

Une analyse exploratoire des donnees assez classique qui permet de recomposer les liens entre les differentes tables du dataset.

- On va estimer des indicateurs courants type "panier moyen" ou "temps moyen pour qu'un primo-acheteur devienne un client regulier".
- On realise une premiere segmentation RFM qui permet de se faire une premiere idee, assez generique, des profils des acheteurs et acheteuses.

## 2. Segmentations des acheteurs et acheteuses.
Fichier : 1_Segmentation_DataScience.ipynb

- On va explorer plusieurs algorithmes de clusterisation non supervisee : K-means, DBSCAN, CAH.
- On va travailler sur des dataset disposant de differentes features et mesurer les silhouettes scores de nos differentes segmentation pour determiner celle qui offre les meilleurs resultats.
- On va etudier les clusters identifies et faire des radar charts pour mieux comprendre le profil de nos acheteurs et acheteuses.
- On va reduire le nombre de dimensions avec t-SNE pour visualiser nos clusters.

## 3. Estimation d'une frequence de maintenance.
Fichier : 2_Evolution_Temporelle_des_Clusters.ipynb

- On va etudier le drift de nos donnees sur la base du data set fourni
- On va calculer l'evolution de l'ARI de nos modeles pour estimer une frequence ad hoc de maintenance