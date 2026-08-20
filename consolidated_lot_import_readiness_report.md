# Bilan consolidé des lots reçus — AutobahnHub

**Statut : audit terminé, import non autorisé et aucune annonce créée.** Le catalogue actuel reste à **176 annonces authentiques**. Les chiffres ci-dessous distinguent les fichiers reçus, les collisions exactes de contenu et les candidats techniquement disponibles. Une empreinte SHA-256 différente ne prouve pas à elle seule que deux photos représentent deux véhicules individuels distincts ; cette validation finale devra être faite avant la création des brouillons.

## Synthèse par catégorie

| Catégorie demandée | Fichiers reçus et vérifiés | Doublons internes exacts | Déjà présents dans le catalogue | Candidats sans collision SHA-256 | Conclusion d’intégration immédiate |
|---|---:|---:|---:|---:|---|
| Voitures / SUV | 60 | 0 | 3 | **57** | 57 candidats photo-uniques ; identité individuelle encore à confirmer |
| Bus / minibus | 12 | 0 | 0 | **12** | 12 candidats photo-uniques ; modèle exact non inventé |
| Tracteurs agricoles | 0 photo clairement identifiable comme tracteur agricole | — | — | **0** | Ne pas intégrer sous « Tracteur » : le lot reçu correspond à du matériel de chantier |
| Poids lourd | 30 | 1 paire (`68552.jpg` / `68555.jpg`) | 0 | **29** | 29 candidats photo-uniques ; identité individuelle encore à confirmer |
| **Total des catégories demandées** | **102** | **1 paire + 3 collisions catalogue** | **3** | **98** | **98 candidats techniques, non encore certifiés comme 98 véhicules distincts** |

## Lot de matériel envoyé comme « tracteurs »

Le lot contient **16 références transmises correspondant à 15 fichiers distincts**. La référence `68530.jpg` apparaît deux fois dans le message, mais le fichier local n’existe qu’une fois et son contenu n’a été haché qu’une seule fois. Les 15 empreintes sont distinctes entre elles et aucune collision n’a été trouvée avec les 176 annonces, les lots Voiture/SUV, les lots Bus ou le lot Poids lourd.

L’examen prudent des images montre principalement des **engins de chantier** : chargeuses, pelles hydrauliques, bulldozer, grue mobile, compacteur, télescopique et autres machines lourdes. `68524.jpg` correspond à une bétonnière et `68537.jpg` est une scène composite montrant plusieurs machines ; ces deux fichiers ne doivent pas devenir automatiquement des annonces individuelles de véhicule. Il reste donc **13 candidats potentiels de matériel de chantier** si cette catégorie est ajoutée séparément, mais **zéro tracteur agricole clairement vérifié** dans ce lot.

## Doublons et collisions à exclure

Les trois fichiers Voiture/SUV déjà utilisés dans le catalogue sont `68432.jpg`, `68433.jpg` et `68461.jpg`. Ils correspondent respectivement aux images déjà associées aux annonces `vehicleId 270130`, `270082` et `270139` via les actifs canoniques `65563.jpg`, `65485.jpg` et `65572.jpg`. Ils ne doivent pas être réutilisés comme nouvelles annonces.

Dans le lot Poids lourd, `68552.jpg` et `68555.jpg` ont exactement la même empreinte SHA-256 `9d8f19aad221f521ee8587fbc16861dbbffeea1670ce1fb68cf976308a401c40`. Une seule référence peut être conservée pour un futur brouillon.

## Verdict avant import

Le nombre **technique maximal** de candidats sans collision de contenu, pour les quatre catégories demandées, est de **98** : 57 voitures/SUV, 12 bus et 29 poids lourds. Ce nombre ne doit pas encore être présenté comme « 98 véhicules réellement distincts », car certaines photos peuvent représenter le même véhicule sous plusieurs angles ou une même série de modèle.

Pour un import professionnel sans doublons d’identité, le feu vert devra autoriser la création de **brouillons non publiés uniquement après validation individuelle**. Les valeurs de marque, modèle, année, kilométrage, équipements et prix ne devront être ajoutées que lorsqu’elles sont fournies ou vérifiables ; sinon, l’annonce doit rester générique au niveau de catégorie. La publication restera manuelle via l’administration.

**Aucun import, remplacement, suppression, réattribution ou publication n’a été effectué pendant cet audit.**
