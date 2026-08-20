# Diagnostic intermédiaire — catégories, recherche et images

Date de l'audit : 2026-08-19.

## État non destructif observé

Le catalogue public actuel affiche 191 annonces publiées. La base contient les slugs `buses` (25), `trucks` (21), `agricultural` (12), `agricultural-machinery` (19), ainsi que cars (27), suvs (25), coupes (15), minibuses (15), classics (11), electric (11) et vans (10).

La route tRPC `vehicles.list` fonctionne quand elle reçoit la requête batch correctement : `buses` retourne 25, `trucks` retourne 21, `agricultural` retourne 12 et `agricultural-machinery` retourne 19. Le test public du champ de recherche avec le terme français `tracteur` affiche 0 résultat. Le backend recherche seulement dans `brand`, `model`, `version` et `description`, pas dans `categorySlug` ni dans des synonymes/libellés traduits. Une recherche textuelle `bus` ne correspond qu'à 5 annonces sur 25, car les autres n'ont pas le mot `bus` dans les quatre champs textuels.

Le frontend `Vehicles.tsx` propose le slug `agricultural-machinery`, tandis que le footer public utilise le slug `agricultural`. Ces deux slugs existent effectivement en base et représentent ensemble 31 annonces agricoles, mais ils sont exposés comme deux valeurs différentes. Les liens et libellés ne sont donc pas normalisés.

## Images actives

Les 191 annonces actuelles utilisent des URL `images.unsplash.com`; aucune `mainImage` active n'utilise `/manus-storage/`. Chaque annonce a une seule image JSON et une seule ligne `vehicle_images` dans l'état actuel. Les URL sont rendues techniquement distinctes par un suffixe `&sig=<id>`, mais après retrait de ce suffixe artificiel, seulement 10 images Unsplash canoniques sont partagées par 191 annonces. Les photos fournies précédemment ne sont donc pas utilisées par le catalogue actuel.

Le rapport historique non destructif `provided_photo_usage_report.json` documente 236 photos de véhicules distinctes localement, 148 lignes `photo_assets` enregistrées, 0 photo fournie référencée dans les 362 annonces de l'ancien état et 362 URL Unsplash à cette date. La répartition locale actuelle comprend 246 fichiers image dans `/home/ubuntu/upload`, dont 218 JPEG et 28 PNG ; l'écart avec les 236 photos distinctes documentées provient des copies/artefacts et doit être interprété avec le rapport de hachage, pas avec un simple comptage de fichiers.

Aucune écriture de données, suppression, réattribution ou modification d'image n'a été effectuée pendant cet audit.

## Vérification publique supplémentaire

Le filtre public `?category=buses` affiche bien 25 véhicules. Le filtre public `?category=agricultural` affiche 12 véhicules. Les cartes visibles dans ces deux pages montrent toutefois des photos de voitures particulières pour des annonces de bus et de tracteurs : par exemple les annonces Bus utilisent des images de BMW/berlines, et les annonces agricoles utilisent une image de coupé/berline Mercedes. Cela confirme un problème de correspondance d'image et non un problème d'absence de lignes en base.

Le slug Bus fonctionne donc comme filtre de catégorie. Le zéro observé avec `tracteur` vient de la recherche textuelle, tandis que l'incohérence agricole est visuelle : les catégories contiennent des lignes mais leurs URL d'image Unsplash sont génériques et réutilisées entre catégories.

Aucune écriture de données, suppression, réattribution ou modification d'image n'a été effectuée pendant cette vérification.
