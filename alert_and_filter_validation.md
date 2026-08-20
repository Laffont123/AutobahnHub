# Validation des alertes et des filtres — 17 août 2026

La vérification du catalogue après les derniers correctifs confirme que le catalogue affiche 472 véhicules sans filtre et que la sélection « Agricultural & Tractors » utilise désormais le slug `agricultural-machinery`. Cette sélection retourne 19 véhicules, correspondant aux 19 annonces agricoles uniques intégrées après déduplication SHA-256.

La page d’accueil conserve le thème sombre premium, la navigation existante et la section d’inscription aux alertes pour Volkswagen Golf et sportives allemandes. Les liens d’alerte restent relatifs pendant la prévisualisation (`/vehicles/{id}`) et deviendront absolus après configuration de `VITE_APP_URL` une fois le site publié.

Les validations techniques exécutées après les changements sont les suivantes : la suite Vitest passe avec 7 fichiers de tests et 15 tests réussis ; la compilation TypeScript avec `pnpm exec tsc --noEmit` ne remonte aucune erreur ; les captures de `/`, `/vehicles` et `/vehicles?category=agricultural-machinery` ont été réalisées sans erreur de serveur.
