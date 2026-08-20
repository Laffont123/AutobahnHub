# Rapport d’inventaire et d’unicité des photographies d’AutobahnHub

## 1. État final du catalogue

Après intégration contrôlée des lots Cars/SUV, le catalogue comporte **444 véhicules publiés**. Le total se compose de l’inventaire existant, de **10 annonces du lot 13** et de **110 annonces canoniques issues des lots 1 à 12**. Les 57 fiches créées par erreur à partir d’anciens assets Volkswagen/Bus ont été retirées avant validation ; aucun véhicule antérieur à cette opération n’a été supprimé ou modifié.

La pagination et le total dynamique restent actifs. La validation tRPC confirme que le catalogue renvoie **444** comme total sans filtre et que deux pages successives de 50 résultats ne partagent aucun identifiant.

## 2. Lots Cars/SUV traités

Les lots Cars/SUV 1 à 12 représentaient **120 fichiers bruts**. Le contrôle SHA-256 a identifié **110 fichiers canoniques** et **10 doublons exacts** écartés. Ces 110 fichiers ont été transformés en 110 annonces distinctes, avec une image principale par annonce, une ligne dédiée dans `vehicle_images`, des prix compris entre **12 000 € et 80 000 €**, et des champs JSON `images`/`features` enregistrés nativement.

Le lot 13 comportait **10 fichiers**. Ils ont été intégrés en 10 annonces distinctes, avec revue visuelle des véhicules et correction des métadonnées des deux fiches T-Roc à toit fixe.

| Périmètre | Fichiers bruts | Fichiers canoniques | Annonces créées | Doublons exacts écartés |
|---|---:|---:|---:|---:|
| Cars/SUV lots 1–12 | 120 | 110 | 110 | 10 |
| Cars/SUV lot 13 | 10 | 10 | 10 | 0 |
| **Total Cars/SUV ajouté** | **130** | **120** | **120** | **10** |

## 3. Contrôles d’unicité

Le garde-fou d’image exécuté sur les 120 nouvelles annonces a renvoyé **passed: true**, avec **0 groupe de doublons d’image principale** et **0 groupe de doublons de galerie**. Les 120 assets correspondants sont enregistrés dans `photo_assets` avec le statut `assigned`.

L’audit global du catalogue distingue les historiques à traiter séparément des nouvelles annonces : **403 clés d’identité uniques**, **41 groupes d’identités similaires**, **25 groupes d’images principales partagées** et **32 groupes d’images de galerie partagées**. Ces groupes historiques n’ont pas été supprimés automatiquement, conformément à la règle de préservation des annonces légitimes ; le nouveau workflow bloque désormais toute nouvelle affectation qui créerait un partage.

## 4. Tests et vérifications

La suite Vitest complète passe avec **5 fichiers de test et 11 tests réussis**. TypeScript compile sans erreur. Les tests dédiés aux lots 1 à 12 vérifient les 110 annonces, les prix, les tableaux JSON natifs, les 110 galeries dédiées, la recherche, le filtre de catégorie, la pagination et le garde-fou. Les captures desktop et mobile confirment que le catalogue et une fiche Cars/SUV s’affichent sans erreur.

## 5. Vérification SQL du catalogue actuel — 18 août 2026

Une vérification en lecture seule de la base confirme **472 annonces publiées**, dont **231 images principales distinctes** ; **241 affectations de `mainImage` sont donc historiquement partagées**. Cette situation concerne principalement les fiches seed historiques et ne doit pas être traitée par suppression ou par l’attribution d’images non vérifiées. Les 28 annonces agricoles et poids lourds ajoutées par lots ont été protégées par le garde-fou d’unicité au moment de leur affectation.

Le nettoyage complet reste **explicitement différé** jusqu’à la réception d’un volume suffisant de nouvelles photographies authentiques et catégorisées. Cette décision préserve les 472 annonces, évite les images génériques ou hors catégorie et ne modifie pas le correctif de navigation récemment livré.
