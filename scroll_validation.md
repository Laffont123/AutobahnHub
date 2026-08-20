# Validation du défilement des fiches véhicule

## Observation du catalogue publié

Le 18 août 2026, le catalogue publié à https://autobahnhub-mqfkjdyk.manus.space/vehicles a chargé 472 véhicules après attente du chargement asynchrone. Les premières annonces visibles incluaient des poids lourds et tracteurs, avec des liens de détail réels tels que `/vehicles/240028`, `/vehicles/240027` et `/vehicles/240019`.

## Correctif vérifié dans le code

`VehicleDetail` appelle `resetScrollPosition()` dans un `useEffect` dépendant de l’identifiant de l’annonce. La fonction appelle `window.scrollTo({ top: 0, left: 0, behavior: "auto" })` dans un navigateur et reste sans effet côté serveur. La couverture Vitest dédiée passe sur les cas navigateur et non navigateur.

## Parcours manuel restant

Le catalogue a été chargé avec succès sur l’URL publiée. Le parcours scrollé vers une annonce doit être reproduit avec un défilement explicite puis l’ouverture d’un lien de fiche ; la vérification desktop/mobile du rendu de la fiche a déjà confirmé que le haut de la fiche commence par la navigation puis l’image principale.

## Reproduction réelle du parcours desktop

Depuis le catalogue publié, j'ai attendu le chargement des 472 véhicules, fait défiler la page d'un viewport, puis ouvert l'annonce Renault T High Turbo Compound depuis une carte encore visible dans la zone défilée. Après navigation, le navigateur a indiqué `Pixels above viewport: 0`; après chargement de la fiche, il indiquait encore `Pixels above viewport: 0` et la capture commençait par la barre de navigation, le lien « Back to Inventory », puis l'image principale. Le correctif est donc confirmé sur le parcours réel desktop.

## Validation mobile

Les captures du projet en viewport 375×812 ont été prises simultanément sur `/vehicles` et `/vehicles/240025`. La fiche mobile commence à `Back to Inventory`, puis affiche immédiatement la carte de l'image principale Renault et le début des informations du véhicule ; aucun contenu inférieur ni position de scroll résiduelle n'est visible. Le catalogue mobile conserve sa structure et son en-tête sans régression.

La reproduction « avant » n'est plus disponible sur le déploiement courant, car le correctif est déjà appliqué ; l'état antérieur est celui signalé par l'utilisateur (`VehicleDetail` ne réinitialisait pas la position). La validation avant/après est donc documentée comme : absence de reset dans l'ancienne implémentation rapportée, puis `Pixels above viewport: 0` sur le parcours publié après correctif.
