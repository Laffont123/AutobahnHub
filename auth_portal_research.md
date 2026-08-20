# Recherche du flux d’authentification Manus

Le 18 août 2026, une recherche publique sur le portail Manus a trouvé la page générale de connexion `https://manus.im/login`, qui présente des fournisseurs OAuth (Facebook, Google, Microsoft et Apple), mais aucun paramètre public documenté permettant de forcer un flux Magic Link depuis `/app-auth`. Les résultats Magic Link trouvés concernaient des fournisseurs tiers et ne documentaient pas Manus.

La page navigateur observée pendant la tentative de connexion a redirigé vers Google OAuth et affichait `Sign in with Google`, l’adresse `francoislaffont42@gmail.com` et `Enter your password`. Cette invite provient du fournisseur Google externe, pas d’un formulaire de mot de passe AutobahnHub.

Sources consultées :
- https://manus.im/login — page publique de connexion Manus.
- https://auth0.com/docs/authenticate/passwordless/authentication-methods/email-magic-link — documentation générale Auth0 sur les Magic Links, non spécifique à Manus.
