# Vérification non destructive des possibilités de restauration

Date : 2026-08-19.

## Checkpoints historiques identifiés

Le dépôt Git contient les checkpoints suivants :

| Révision | État décrit dans le message de checkpoint |
|---|---|
| `256bb79` | 324 véhicules, dont 63 bus, après intégration des quatre lots de bus |
| `37026d9` | 444 véhicules après intégration des lots Cars/SUV 1 à 13 et bus |
| `f7faf79` | Ajout de 28 véhicules : 9 poids lourds et 19 tracteurs/machines agricoles |
| `3b168ea9` | 362 véhicules après une première purge dite rigoureuse |
| `b57f3da8` | 361 véhicules après nettoyage conservateur |
| `b6dee939` | 191 véhicules après nettoyage final actuel |

## Ce que le dépôt contient réellement

Les checkpoints restaurent le code, les scripts et les rapports, mais aucune sauvegarde SQL complète des lignes de la base distante n'a été trouvée dans le projet ou dans les fichiers de sauvegarde usuels du workspace. Les fichiers de migration Drizzle décrivent le schéma, pas les anciennes annonces.

Des scripts historiques d'import existent encore : `server/insertBusListings.mjs`, `server/insertLots1To12Listings.mts`, `server/insertLot13Listings.mts` et `seed_trucks_tractors.mjs`. Ils conservent des listes de photos et des modèles d'import, mais ils ne constituent pas une sauvegarde des anciennes lignes. Ils génèrent notamment des prix, kilométrages et métadonnées au moment de l'insertion ; les réexécuter ne restaurerait donc pas fidèlement les anciennes annonces et pourrait créer des doublons. Ils ne doivent pas être exécutés pendant cette vérification.

Le script bus conserve 38 fichiers de bus non exclus après deux doublons SHA-256. Le script poids lourds/tracteurs conserve 28 fichiers uniques, soit 9 poids lourds et 19 tracteurs/machines agricoles. Le script Cars/SUV 1-12 référence un fichier temporaire `/tmp/canonical_lots_1_12.json` encore présent : il indique 120 fichiers traités et 110 fichiers canoniques uniques. Ces éléments sont des sources de reconstitution contrôlée, pas une sauvegarde de la base.

## Verdict provisoire

Une restauration exacte du catalogue de plus de 350 annonces n'est pas possible par un simple rollback Git, car la base distante et les lignes supprimées ne sont pas stockées dans Git. Une reconstitution partielle à partir des scripts et des photos locales est techniquement possible, mais elle devrait être préparée dans un nouvel espace de prévisualisation ou un export séparé, jamais par réexécution directe des scripts sur la base actuelle.

Aucune modification de la base, du catalogue public ou des photos n'a été effectuée pendant cette vérification.
