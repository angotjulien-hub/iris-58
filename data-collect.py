import json
import os

def run_analysis():
    print("Analyse du couplage IRIS-58 en cours...")
    # Logique de tri des données GPS collectées
    if os.path.exists('data/collect.json'):
        with open('data/collect.json', 'r') as f:
            data = json.load(f)
            # Traitement...
            print("Collecte synchronisée.")

if __name__ == "__main__":
    run_analysis()
