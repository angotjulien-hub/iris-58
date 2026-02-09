import os

# Récupération sécurisée du token via les variables d'environnement
# Cela évite d'écrire le token en clair dans le code
TOKEN = os.getenv('COLLECTION_TOKEN')

def collecter_positions():
    if not TOKEN:
        print("Erreur : Aucun token de collecte trouvé.")
        return
    print("Connexion établie. Collecte des positions des chauffeurs en cours...")
    # Logique de collecte ici
