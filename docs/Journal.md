# Journal de développement

## 26 juillet 2026

### Réalisé

- Création du dépôt GitHub
- Configuration Git
- Authentification SSH GitHub
- Installation VS Code Remote SSH
- Création de l'arborescence du projet

### Décisions

- GitHub comme dépôt central.
- Documentation en Markdown.
- Cahier des charges officiel en Word.
- Développement sur Debian via VS Code Remote.

### Prochaine étape

Installation du hotspot et création du portail captif.
## 14 novembre 2026

### Réalisé

- Installation et configuration de Debian 13.
- Mise en service du point d'accès Wi-Fi `Mermoz WiFi gratuit`.
- Configuration de Hostapd et dnsmasq.
- Configuration du routage Internet et du NAT.
- Installation et configuration d'OpenNDS.
- Mise en service du portail captif.
- Notifications Telegram lors des connexions et déconnexions Wi-Fi.
- Notifications Telegram après validation du portail captif.
- Création d'un registre local des appareils connus.
- Association d'un nom aux appareils enregistrés.
- Sauvegarde des scripts dans le dépôt GitHub.

### Architecture technique actuelle

- Interface Internet : `wlx90f652138020`
- Interface point d'accès : `wlo1`
- Réseau Wi-Fi : `10.42.0.0/24`
- Passerelle : `10.42.0.1`
- Portail captif : OpenNDS
- Notifications : bot Telegram
- Scripts : Python et Bash
- Système : Debian 13

### Sécurité et sauvegardes

- Secrets Telegram conservés hors du dépôt Git.
- Registre des appareils conservé localement.
- Scripts sauvegardés dans GitHub.
- Commit : `668e202`

### Prochaines étapes

- Mettre à jour la documentation générale.
- Concevoir le nouveau portail captif personnalisé.
- Créer la page d'accueil de Quartier Connecté.
- Développer le mini-site communautaire.
- Ajouter l'inscription des utilisateurs.
- Développer les commandes d'administration Telegram.
