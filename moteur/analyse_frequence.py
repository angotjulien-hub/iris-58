import pandas as pd
from datetime import datetime, timedelta

def analyser_couplage(file_path):
    # Chargement propre du référentiel
    df = pd.read_csv(file_path, sep=';', encoding='utf-8', quoting=3)
    df.columns = [c.replace('"', '').strip() for c in df.columns]
    
    # On trie par heure de passage pour comparer les bus qui se suivent
    # Note : Assure-toi que ta colonne s'appelle 'Heure' ou adapte ici
    df = df.sort_values(by='Heure')

    alertes = []
    
    # On boucle sur les lignes pour comparer la voiture N avec la voiture N+1
    for i in range(len(df) - 1):
        h1 = datetime.strptime(df.iloc[i]['Heure'], '%H:%M:%S')
        h2 = datetime.strptime(df.iloc[i+1]['Heure'], '%H:%M:%S')
        
        ecart = (h2 - h1).total_seconds() / 60
        
        if ecart < 3: # Seuil de couplage
            alertes.append({
                'V1': df.iloc[i]['Voiture'],
                'V2': df.iloc[i+1]['Voiture'],
                'Ecart': ecart,
                'Action': "⚠️ RÉTENTION REQUISE (Couplage détecté)"
            })
            
    return alertes

# Test sur ton fichier actuel
alertes_detectees = analyser_couplage('referentiel/058LAV10.csv')
for a in alertes_detectees:
    print(f"Bus {a['V1']} et {a['V2']} : {a['Ecart']}min d'écart -> {a['Action']}")
