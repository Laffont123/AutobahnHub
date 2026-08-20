# Audit du lot 13 — Cars / SUV

**Statut :** reçu et audité techniquement, non exporté et non intégré au catalogue.

Le lot 13 contient 10 fichiers JPEG fournis par l’utilisateur. Les empreintes SHA-256 ci-dessous ont été calculées sur les fichiers locaux reçus. Une comparaison exacte a également été effectuée avec les 40 fichiers JPEG actuellement présents dans `/home/ubuntu/upload/`, afin de détecter une réutilisation binaire.

| Fichier | SHA-256 | Résultat exact |
|---|---|---|
| `65468.jpg` | `e0bbe99c6c385754a4027ed1261428102a779dbb9675ceb8aed9a005d9873dad` | Unique dans les fichiers reçus |
| `65466.jpg` | `4c462c142c7e0bbcad62b54d8604ec19e4a71817a885bb5a4d8e1d585e1dd869` | Unique dans les fichiers reçus |
| `65465.jpg` | `f9669a0f00c90bf807bef245223134be232d088cd0b1623db0e132db80a91924` | Unique dans les fichiers reçus |
| `65464.jpg` | `29bad98e9074e5c73147fdcd8d32c15d5f1e52d60407927d2227d73cd7759628` | Unique dans les fichiers reçus |
| `65463.jpg` | `f54588223080e4164863fd3bcef7769af9d9d32975f6ce5ea1d230968b8ff22e` | Unique dans les fichiers reçus |
| `65455.jpg` | `b80914aa14548f2196f33041fa03b4a1a2c498e57e29094c08d8f9445dc1ece2` | Unique dans les fichiers reçus |
| `65454.jpg` | `d4bf1667f14960c2a73364a5a6a657bea0ab98e31ed22e871d215909f30558b7` | Unique dans les fichiers reçus |
| `65452.jpg` | `db2539ff91a1398e47cdde90acf288f899c64f208058bda917281d498113d5e9` | Unique dans les fichiers reçus |
| `65462.jpg` | `062fdb2e0d6258e0587254fb2b25bea28701ea6d4675ef6f90f8d3466bc5dc2b` | Unique dans les fichiers reçus |
| `65442.jpg` | `b2fbb2bfcdbda705ed8efe15faef5d8b7cb56662814d9e25827b4bca6f4b60b6` | Unique dans les fichiers reçus |

## Conclusion

Les 10 fichiers possèdent des empreintes SHA-256 distinctes. Aucun doublon binaire exact n’a été trouvé entre le lot 13 et les 30 autres fichiers JPEG déjà présents dans le dossier d’upload au moment du contrôle. Les images reçues montrent des véhicules pertinents pour les catégories Cars/SUV ; aucune image de paysage, d’océan, de forêt, de maison ou d’un autre sujet non automobile n’a été retenue dans ce lot.

Certaines images présentent le même modèle ou une même famille de modèle, notamment des Volkswagen T-Roc, et deux fichiers sont des compositions de plusieurs vues. Elles doivent donc rester des **assets photo distincts à analyser par identité de véhicule**, sans créer automatiquement une annonce par fichier. Les vues d’un même véhicule seront regroupées dans une seule galerie lors de l’intégration finale, après confirmation de fin de collecte.

Aucune ligne de véhicule n’a été créée, modifiée ou supprimée. Aucune photo n’a été exportée vers le catalogue et aucun asset n’a été enregistré comme affecté à une annonce.
