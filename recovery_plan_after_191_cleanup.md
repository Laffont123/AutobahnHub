# Plan de récupération d'AutobahnHub

## Réponse courte

Pour retrouver exactement l'ancien AutobahnHub, il faut restaurer la **base de données**, pas seulement le code du site. Le dernier état actuel contient 191 annonces. Les anciens checkpoints peuvent restaurer le code et l'interface, mais ils ne restaurent pas automatiquement les lignes supprimées de la base distante.

## Ce qui s'est réellement passé

Le catalogue a auparavant atteint plus de 350 lignes, mais une grande partie des annonces a été créée à partir de variantes artificielles et d'images génériques. Les opérations de nettoyage ont ensuite réduit le catalogue à 191 annonces. Les audits conservés indiquent que les photos authentiques fournies n'étaient pas réellement utilisées dans le catalogue publié : les 191 annonces actuelles utilisent des URL Unsplash.

L'audit non destructif documente 236 photos de véhicules distinctes disponibles localement. Il existe aussi 148 métadonnées `photo_assets` enregistrées, mais ces références ne sont pas les URL actuellement utilisées par les annonces publiques. Un simple comptage de fichiers donne 246 fichiers image dans `/home/ubuntu/upload`, car il comprend des copies ou variantes ; ce nombre n'est donc pas le nombre de photos distinctes vérifiées.

## Limite importante sur l'unicité

Avec 236 photos de véhicules distinctes, il est impossible de publier plus de 236 annonces qui possèdent chacune une photo principale différente, si l'on interdit réellement la réutilisation d'une même photo. Pour publier 350 annonces réellement distinctes avec une photo principale unique par annonce, il faudrait au moins 350 photos de véhicules distinctes supplémentaires, correctement identifiées et classées.

Il ne faut donc pas recréer artificiellement 350 annonces à partir de 236 photos. Cela reproduirait exactement le problème que l'utilisateur souhaite supprimer.

## Deux chemins possibles

### Chemin A — Restaurer d'abord l'ancien catalogue de plus de 350 lignes

Restaurer une sauvegarde de base de données datant d'avant le nettoyage, si une sauvegarde existe. Il faudra ensuite auditer les lignes restaurées et conserver seulement les annonces correspondant à de vrais véhicules ou à de vraies photos fournies. Cette méthode est la seule qui puisse retrouver les anciennes lignes, leurs identifiants et leurs caractéristiques sans les réinventer.

Un rollback de code seul n'est pas suffisant : il remettrait éventuellement l'ancienne interface ou les anciennes procédures, mais pas les enregistrements distants supprimés.

### Chemin B — Reconstituer un catalogue propre à partir des photos authentiques

Conserver les 191 lignes actuelles en lecture seule, réimporter et vérifier les 236 photos distinctes, classer chaque photo par catégorie, puis associer une photo principale différente à chaque annonce réellement confirmée. Les annonces sans photo authentique compatible ne doivent pas recevoir une image de voiture générique, de bus incorrecte ou de tracteur inventé.

Cette méthode peut produire au maximum 236 annonces avec photo principale unique, et probablement moins si certaines photos sont trop incertaines, non-vehiculaires ou incompatibles avec les catégories demandées. Les marques et modèles non vérifiables doivent rester génériques, par exemple « Tractor », « Bus », « Truck », « SUV » ou « Car ».

## Recommandation professionnelle

Le chemin recommandé est :

1. Geler le catalogue actuel et ne rien supprimer ni importer immédiatement.
2. Chercher d'abord une sauvegarde de base de données antérieure au nettoyage pour savoir si l'ancien catalogue de plus de 350 lignes peut être récupéré réellement.
3. Si aucune sauvegarde exploitable n'existe, ne pas tenter de recréer 350 annonces. Constituer un catalogue plus réduit mais authentique, basé sur les 236 photos distinctes vérifiées.
4. Corriger le moteur de recherche pour que `bus`, `tracteur`, `agriculture`, `truck`, `poids lourd` et leurs équivalents localisés recherchent aussi la catégorie, sans toucher aux données pendant cette étape.
5. Normaliser les deux slugs agricoles (`agricultural` et `agricultural-machinery`) sous une seule catégorie publique, après validation.
6. Importer les photos dans le stockage permanent `/manus-storage/`, puis appliquer une correspondance contrôlée catégorie par catégorie : Cars/SUVs, Buses, Trucks et Tractors.
7. Vérifier l'unicité par empreinte de contenu avant publication : aucune même photo principale, aucune galerie identique et aucune photo de voiture dans une annonce de bus ou de tracteur.
8. Publier seulement après validation du catalogue et des pages de détail.

## Décision à prendre

La prochaine action doit être l'une des deux suivantes :

- **Restaurer une sauvegarde de l'ancien catalogue**, si l'objectif prioritaire est de retrouver les anciennes annonces de plus de 350 lignes ; ou
- **Construire un catalogue authentique limité par les 236 photos distinctes**, si l'objectif prioritaire est l'unicité et la cohérence professionnelle.

Aucune de ces deux options ne doit être engagée sans confirmer d'abord la présence ou l'absence d'une sauvegarde exploitable et sans conserver l'état actuel comme référence.
