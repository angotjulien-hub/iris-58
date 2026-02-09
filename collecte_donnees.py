import os
import time
import json
import requests

# Récupération sécurisée du Token depuis les secrets GitHub
TOKEN = os.getenv('COLLECTION_TOKEN')
API_URL = "https://api.votre-service.com/positions/ligne58" # <--- Remplace par l'URL réelle

def effectuer_la_collecte():
    if not TOKEN:
        print("Erreur : COLLECTION_TOKEN manquant.")
        return
    
    heure_actuelle = time.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Appel à l'API pour récupérer les positions des chauffeurs connectés
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(API_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            positions = response.json()
            
            # Sauvegarde des données réelles dans ton fichier JSON
            data = {
                "derniere_maj": heure_actuelle,
                "vehicules": positions
            }
            with open('iris_config.json', 'w') as f:
                json.dump(data, f, indent=4)
            print(f"[{heure_actuelle}] ✅ {len(positions)} chauffeurs captés.")
        else:
            print(f"[{heure_actuelle}] ⚠️ Erreur API: {response.status_code}")
            
    except Exception as e:
        print(f"[{heure_actuelle}] ❌ Erreur de connexion: {e}")

# Boucle de 5 minutes (haute fréquence)
for i in range(5):
    effectuer_la_collecte()
    if i < 4:
        time.sleep(60)
