import os
import time
import json

TOKEN = os.getenv('COLLECTION_TOKEN')

def effectuer_la_collecte():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Collecte Ligne 58 en cours...")
    
    # Simulation de données (à remplacer par l'API plus tard)
    data = {"date": now, "ligne": "58", "status": "actif"}
    
    with open('iris_config.json', 'w') as f:
        json.dump(data, f)

for i in range(5):
    effectuer_la_collecte()
    if i < 4:
        time.sleep(60)
