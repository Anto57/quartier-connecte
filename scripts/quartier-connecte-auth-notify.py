#!/usr/bin/python3
import sys
import urllib.parse
import urllib.request

ENV_FILE = "/etc/quartier-connecte/telegram.env"
DEVICES_FILE = "/etc/quartier-connecte/appareils.conf"


def read_config(path):
    config = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config


def get_device_name(mac):
    try:
        with open(DEVICES_FILE) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                known_mac, name = line.split("=", 1)
                if known_mac.strip().lower() == mac.lower():
                    return name.strip()
    except OSError:
        pass

    return f"Appareil inconnu ({mac[-5:].upper()})"


try:
    if len(sys.argv) < 2:
        sys.exit(0)

    mac = sys.argv[1]
    config = read_config(ENV_FILE)
    device_name = get_device_name(mac)

    message = (
        "✅ Connexion au portail captif acceptée\n"
        f"Nom : {device_name}\n"
        "Réseau : Mermoz WiFi gratuit"
    )

    data = urllib.parse.urlencode({
        "chat_id": config["CHAT_ID"],
        "text": message
    }).encode()

    url = (
        "https://api.telegram.org/bot"
        + config["BOT_TOKEN"]
        + "/sendMessage"
    )

    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError("Réponse Telegram inattendue")

except Exception as error:
    print(
        f"Erreur notification portail : {type(error).__name__}",
        file=sys.stderr
    )
