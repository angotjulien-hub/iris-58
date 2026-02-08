import pandas as pd

def clean_horaires(file_path):
    # Lecture avec gestion du point-virgule (standard Excel FR)
    df = pd.read_csv(file_path, sep=';', encoding='utf-8')
    
    # Nettoyage des colonnes : on enlève les guillemets résiduels
    df.columns = [c.replace('"', '').strip() for c in df.columns]
    
    # Transformation des colonnes d'heures en format 'Time'
    # On cible les colonnes qui contiennent souvent "H" ou "Passage"
    for col in df.columns:
        if 'Heure' in col or 'Passage' in col:
            df[col] = pd.to_datetime(df[col], format='%H:%M:%S', errors='coerce').dt.time
            
    return df

# Test sur le fichier 58
df_clean = clean_horaires('referentiel/058LAV10.csv')
print("Colonnes détectées :", df_clean.columns.tolist())
