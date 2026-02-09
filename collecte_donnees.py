import os
import time
import json

TOKEN = os.getenv('COLLECTION_TOKEN')

def effectuer_la_collecte():
    if not TOKEN:
        print("Erreur : COLLECTION_TOKEN manquant.")
        return
    
    # On récupère l'heure actuelle
    heure_actuelle = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{heure_actuelle}] Collecte Ligne 58 en cours...")

    # On prépare la donnée (ici on simule une position, à remplacer par ton API)
    data = {
        "derniere_mise_a_jour": heure_actuelle,
        "ligne": "58",
        "statut": "en_service"
    }

    # On sauvegarde dans le fichier JSON
    with open('iris_config.json', 'w') as f:
        json.dump(data, f, indent=4)

# Boucle de 5 minutes
for i in range(5):
    effectuer_la_collecte()
    if i < 4:
        time.sleep(60)
