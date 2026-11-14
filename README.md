# Quartier Connecté

## Présentation

Quartier Connecté est un projet open source visant à créer une plateforme numérique de proximité comprenant :

- Un accès Wi-Fi gratuit et sécurisé.
- Un portail captif personnalisé.
- Un mini-site communautaire.
- Des informations sur la vie du quartier.
- Un espace dédié aux commerces et associations.
- Des outils d'entraide et de signalement.
- Une interface d'administration.

Premier déploiement :

> **Mermoz WiFi gratuit – Le Quartier Connecté**

---

## État du projet

### Fonctionnel

- Debian 13 installé et configuré.
- Dépôt GitHub opérationnel.
- Point d'accès Wi-Fi Hostapd.
- SSID : `Mermoz WiFi gratuit`.
- DHCP avec dnsmasq.
- Routage Internet et NAT.
- Portail captif OpenNDS.
- Authentification des utilisateurs.
- Notifications Telegram lors des connexions et déconnexions Wi-Fi.
- Notifications Telegram après validation du portail captif.
- Registre local des appareils connus.
- Association d'un nom aux appareils enregistrés.

### En cours de développement

- Personnalisation complète du portail captif.
- Page de présentation du projet.
- Inscription des utilisateurs.
- Mini-site communautaire.
- Commandes d'administration Telegram.
- Statistiques de fréquentation et de consommation.

---

## Architecture technique

\`\`\`
                    INTERNET
                       |
                Dongle Wi-Fi USB
             wlx90f652138020
                       |
                    Debian 13
                       |
             Routage IPv4 et NAT
                       |
              Carte Wi-Fi interne
                     wlo1
                       |
              Hostapd / dnsmasq
                       |
              Mermoz WiFi gratuit
                       |
                 Appareils clients
                       |
                  Portail captif
                    OpenNDS
                       |
             Validation des conditions
                       |
                 Accès Internet
\`\`\`

### Plan d'adressage

| Élément | Valeur |
|---|---|
| Interface Internet | `wlx90f652138020` |
| Interface Wi-Fi AP | `wlo1` |
| Adresse de la passerelle | `10.42.0.1` |
| Réseau local | `10.42.0.0/24` |
| DHCP | `10.42.0.20` à `10.42.0.200` |
| SSID | `Mermoz WiFi gratuit` |

---

## Services

| Service | Fonction |
|---|---|
| Hostapd | Point d'accès Wi-Fi |
| dnsmasq | DHCP et DNS |
| OpenNDS | Portail captif |
| nftables | NAT |
| Python | Scripts et notifications |
| Telegram Bot | Alertes et administration |

---

## Scripts du projet

Les scripts personnalisés sont conservés dans le dépôt :

- `scripts/quartier-connecte-hostapd-event.py` : événements de connexion et déconnexion Wi-Fi.
- `scripts/quartier-connecte-auth-notify.py` : notification après authentification.
- `config/opennds/custombinauth.sh` : intégration avec OpenNDS.

Les paramètres sensibles sont conservés localement dans `/etc/quartier-connecte/` et ne doivent jamais être publiés dans Git.

---

## Commandes utiles

### Vérifier les services

\`\`\`bash
sudo systemctl status hostapd
sudo systemctl status dnsmasq
sudo systemctl status opennds
sudo systemctl status quartier-connecte-nat
sudo systemctl status quartier-connecte-hostapd-events
\`\`\`

### Consulter les journaux

\`\`\`bash
sudo journalctl -u hostapd -f
sudo journalctl -u dnsmasq -f
sudo journalctl -u opennds -f
sudo journalctl -u quartier-connecte-hostapd-events -f
\`\`\`

### Vérifier le réseau

\`\`\`bash
ip addr
ip route
sudo iw dev
sudo ndsctl status
\`\`\`

---

## Sauvegarde et versionnement

Le projet est versionné sur GitHub.

Dépôt :

https://github.com/Anto57/quartier-connecte

Après chaque évolution validée :

\`\`\`bash
git add .
git diff --cached --check
git commit -m "Description des modifications"
git push origin main
\`\`\`

Ne jamais ajouter au dépôt les tokens, mots de passe, fichiers de configuration personnels, adresses MAC ou journaux contenant des données personnelles.

---

## Prochaines étapes

- [ ] Mettre en place le nouveau portail captif.
- [ ] Créer le mini-site Quartier Connecté.
- [ ] Ajouter une page d'information et de présentation.
- [ ] Concevoir l'inscription des utilisateurs.
- [ ] Ajouter les mentions légales et informations RGPD.
- [ ] Développer les commandes Telegram `/status`, `/clients`, `/usage`.
- [ ] Mettre en place les statistiques de consommation.
- [ ] Développer l'interface d'administration.
- [ ] Étudier le déploiement Docker.

---

## Technologies

- Debian 13
- Hostapd
- dnsmasq
- OpenNDS
- nftables
- Python
- Bash
- HTML / CSS / JavaScript
- Git / GitHub

---

## Licence

À définir.
