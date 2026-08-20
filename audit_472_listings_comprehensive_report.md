# Rapport d'Audit Complet de l'État à 472 Annonces

- **Date de l'audit** : Février 2026
- **Périmètre** : 472 annonces recensées dans la base de données avant nettoyage et réintégration des photos authentiques.

## 1. Constats chiffrés et divergence d'affichage
- **Nombre total d'enregistrements en base** : 472 lignes.
- **Divergence affichée ("472 vehicles found")** : Le compteur public lisait directement le nombre total de lignes en base de données, tandis que la pagination limitait le rendu par blocs de 50 éléments. Cependant, de nombreux enregistrements partageaient les mêmes signatures d'Unsplash ou des variations artificielles de prix/kilométrage (identifiés comme doublons d'identité).
- **Doublons d'identité et de photos** : Environ 296 annonces présentaient des collisions strictes d'images principales ou de galeries partagées, avec des variations cosmétiques de prix.

## 2. Résolution
Ces constats ont servi de base à la purge conservatrice puis à la réintégration rigoureuse et définitive des **176 véhicules authentiques** liés aux photos physiques fournies.
