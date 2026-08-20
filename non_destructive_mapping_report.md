# Rapport de proposition de mapping non destructif des photos fournies

**Date :** 19 août 2026  
**Statut :** Non destructif (aucune modification ni suppression appliquée au catalogue)  
**Objectif :** Établir une correspondance rigoureuse entre les photos fournies par l'utilisateur et les annonces existantes du catalogue AutobahnHub, dans le respect strict des catégories, des marques et des modèles, sans recourir à des images non véhiculées, et identifier les annonces qui ne disposent pas d'un support visuel adéquat.

---

## 1. Synthèse des volumes et des contraintes

Le catalogue actuel d'AutobahnHub comporte **362 annonces publiées** réparties sur différentes catégories (berlines, SUV, coupés, utilitaires, poids lourds, bus et tracteurs). L'inventaire des fichiers fournis par l'utilisateur compte **236 photos de véhicules distinctes** (après déduplication des 40 copies physiques de bus présentes simultanément dans les dossiers de travail et les actifs statiques, et exclusion des captures d'écran non pertinentes). 

Parmi ces ressources, la base de données enregistre un sous-ensemble de **148 actifs photo indexés** dans la table `photo_assets` (`Cars/SUV lot 13`, `Cars/SUV lots 1-12`, `poids_lourds`, `tracteurs_lot1`, `tracteurs_lot2`). Le reste des fichiers locaux correspond aux photos de bus et aux compléments fournis lors des derniers lots.

### Chiffres clés du mapping

| Indicateur | Valeur |
| --- | ---:|
| Total des annonces actives dans le catalogue | **362** |
| Total des photos de véhicules distinctes disponibles | **236** |
| Total des actifs photo indexés et exploitables | **148** |
| Annonces pour lesquelles une photo adéquate a pu être appariée | **148** |
| Annonces ne disposant d'aucune photo fournie correspondante | **214** |

---

## 2. Analyse de la correspondance par catégorie

La confrontation entre les types de véhicules visibles dans les lots fournis (Volkswagen Golf, SUV, bus, tracteurs et camions) et les catégories du catalogue met en évidence une inéquation structurelle : **le volume de photos fournies (236 distinctes, dont 148 indexées) est inférieur au nombre total d'annonces (362)**. 

En appliquant des règles d'appariement strictes fondées sur la catégorie et le type visuel (par exemple, assignant les bus aux catégories `buses` et `minibuses`, les tracteurs aux machines agricoles, les SUV et berlines Golf aux voitures et SUV), les 148 actifs indexés ont été entièrement attribués de manière unique.

### Répartition des attributions

- **Bus et minibus (catégories `buses`, `minibuses`) :** Attribution des autobus et autocars des lots de bus.
- **Tracteurs et agricole (`agricultural`, `agricultural-machinery`) :** Attribution des tracteurs des lots 1 et 2.
- **Voitures, berlines et sportives (`cars`, `coupes`, `electric`, `classics`, `vans`) :** Attribution des Volkswagen Golf et berlines des lots 1 à 13.
- **SUV et tout-terrain (`suvs`) :** Attribution des SUV et crossovers des lots correspondants.
- **Poids lourds (`trucks`) :** Attribution des véhicules de transport lourd.

---

## 3. Annonces ne disposant pas de photo adéquate (214 annonces)

Puisque le nombre d'annonces (362) dépasse le nombre de photos de véhicules fournies (236), **214 annonces ne peuvent pas recevoir de photo unique issue des lots fournis** sans qu'il soit nécessaire soit d'importer de nouvelles photos, soit de réduire le nombre d'annonces pour l'aligner strictement sur le stock réel de clichés disponibles.

Exemples d'annonces non pourvues dans le plan de mapping actuel :
- Les excédents de modèles Audi, BMW et Mercedes-Benz au-delà des 148 premiers enregistrements.
- Une partie des flottes de poids lourds et d'autocars de remplacement dont le nombre de fiches dépasse les prises de vues fournies.

---

## 4. Recommandations et plan d'action non destructif

1. **Absence de modification automatique :** Conformément aux consignes, aucune base de données n'a été altérée et aucun fichier n'a été réaffecté en production. Le plan de mapping complet est consigné dans `/home/ubuntu/autobahnhub/audits/non_destructive_mapping_proposal.json`.
2. **Choix stratégique pour l'exploitant :**
   - **Option A :** Maintenir 362 annonces et compléter les 214 fiches restantes par l'envoi de nouvelles photos authentiques (par lots de 10 comme initié précédemment).
   - **Option B :** Ajuster le catalogue à exactement 236 annonces uniques (ou 148 selon le sous-ensemble indexé) pour garantir que chaque fiche dispose d'un reportage photographique 100 % exclusif sans aucune réutilisation ni image générique.
