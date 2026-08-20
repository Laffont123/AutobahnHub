# Vérification de publication — 2026-08-20

## Résultats en base

La table `vehicles` contient 286 véhicules avec `isPublished = 1` et aucun brouillon avec `isPublished = 0`. Le total correspond à 176 annonces authentiques initiales + 110 brouillons publiés par l’administrateur.

## Répartition publique par catégorie

| Catégorie | Véhicules publiés |
|---|---:|
| agricultural | 31 |
| buses | 50 |
| cars | 33 |
| suvs | 134 |
| trucks | 38 |
| **Total** | **286** |

## Vérification publique

La page publique `/vehicles` est accessible. Elle affiche `286 vehicles found`, 50 véhicules par page et 6 pages de pagination. Les nouvelles annonces Poids lourd sont visibles sur la première page, notamment les entrées 68554, 68553 et 68552, avec leurs photos correspondantes.

Aucune écriture n’a été effectuée pendant cette vérification.

## Réserve à traiter séparément

La base utilise encore `agricultural` pour les brouillons de matériel de chantier/TP ; cela ne change pas leur statut de publication, mais la classification métier devra être corrigée séparément si une catégorie dédiée TP est souhaitée.
