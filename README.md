# Quartier Connecté

## Présentation

Quartier Connecté est une plateforme open source permettant de déployer :

- un hotspot Wi-Fi sécurisé
- un portail captif moderne
- une plateforme communautaire de quartier
- un espace dédié aux commerces
- une interface d'aide aux livreurs
- un système de signalement et d'entraide

Premier déploiement :

> **Mermoz WiFi gratuit – Le Quartier Connecté**

---

# État du projet

## ✔ Fonctionnel

- Debian 13 installé
- dépôt Git initialisé
- Hostapd opérationnel
- Point d'accès Wi-Fi diffusé
- SSID : **Mermoz WiFi gratuit**
- Interface AP : **wlo1**
- Interface Internet : **wlx90f652138020**
- dnsmasq installé
- OpenNDS installé

---

## Architecture

```
Internet
    │
    │
Dongle Wi-Fi USB
(wlx90f652138020)
    │
Debian
    │
Hostapd
    │
Carte Wi-Fi interne
(wlo1)
    │
Mermoz WiFi gratuit
```

---

## Plan d'adressage

| Élément | Valeur |
|---------|---------|
| Interface AP | wlo1 |
| Interface Internet | wlx90f652138020 |
| Adresse AP | 10.42.0.1 |
| DHCP | 10.42.0.20 → 10.42.0.200 |

---

# Commandes utiles

## Démarrer

```bash
sudo systemctl start hostapd
sudo systemctl start dnsmasq
sudo systemctl start opennds
```

## Arrêter

```bash
sudo systemctl stop opennds
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
```

## Redémarrer

```bash
sudo systemctl restart hostapd dnsmasq opennds
```

## Vérifier

```bash
sudo systemctl status hostapd
sudo systemctl status dnsmasq
sudo systemctl status opennds

sudo iw dev
nmcli device status
ip addr show wlo1
```

## Logs

```bash
sudo journalctl -u hostapd -f
sudo journalctl -u dnsmasq -f
sudo journalctl -u opennds -f
```

---

# Configuration

Hostapd

```
/etc/hostapd/hostapd.conf
```

dnsmasq

```
/etc/dnsmasq.d/hotspot.conf
```

OpenNDS

```
/etc/opennds/opennds.conf
```

---

# Prochaines étapes

- [ ] Configurer OpenNDS
- [ ] Créer le portail captif
- [ ] Authentification des utilisateurs
- [ ] Journalisation des connexions
- [ ] Alertes en temps réel
- [ ] Interface d'administration
- [ ] Déploiement Docker
- [ ] Documentation

---

# Technologies

- Debian
- Hostapd
- dnsmasq
- OpenNDS
- Python / FastAPI
- PostgreSQL
- HTML / CSS / JavaScript
- Docker

---

# Licence

À définir.
