import os
import time

TOKEN = os.getenv('COLLECTION_TOKEN')

def effectuer_la_collecte():
    if not TOKEN:
        print("Erreur : COLLECTION_TOKEN manquant.")
        return
    print(f"[{time.strftime('%H:%M:%S')}] Collecte Ligne 58 en cours...")
    # Ici, tes données seront traitées

for i in range(5):
    effectuer_la_collecte()
    if i < 4:
        time.sleep(60)

print("Cycle terminé.")
