import json
import datetime
import os

def update_iris_config(new_data):
    file_path = 'iris_config.json'
    
    # S'assurer que le fichier existe
    if not os.path.exists(file_path):
        config = {"last_update": "", "fleet_status": [], "line": "58"}
    else:
        with open(file_path, 'r') as f:
            config = json.load(f)

    # Mise à jour de la flotte
    bus_id = new_data.get('id', 'V-UNKNOWN')
    updated = False
    
    for bus in config['fleet_status']:
        if bus['id'] == bus_id:
            bus.update({
                "lat": new_data['lat'],
                "lon": new_data['lon'],
                "gap_front": new_data.get('gap_front', "00:00"),
                "last_ping": datetime.datetime.now().isoformat()
            })
            updated = True
            break
            
    if not updated:
        config['fleet_status'].append(new_data)

    config['last_update'] = datetime.datetime.now().isoformat()

    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)
    
    # --- GÉNÉRATION DE LA HEATMAP ---
    generer_heatmap_file(config['fleet_status'])
    print(f"✅ Audit IRIS : {bus_id} archivé et Heatmap mise à jour.")

def generer_heatmap_file(fleet_status):
    """Transforme les positions des bus en points de chaleur pour index.html"""
    heatmap_points = []
    for bus in fleet_status:
        # On ajoute la lat, lon et une intensité (0.7 par défaut)
        heatmap_points.append([bus['lat'], bus['lon'], 0.7])
    
    with open('heatmap_coords.json', 'w') as f:
        json.dump(heatmap_points, f)

def archiver_audit():
    # S'exécute le dimanche ( weekday 6 )
    if datetime.datetime.now().weekday() == 6:
        if not os.path.exists('referentiel'):
            os.makedirs('referentiel')
            
        try:
            with open('iris_config.json', 'r') as f:
                data = json.load(f)
            
            date_str = datetime.datetime.now().strftime("%Y_S%U")
            archive_path = f'referentiel/archive_{date_str}.json'
            
            with open(archive_path, 'w') as f_arch:
                json.dump(data, f_arch)
                
            # Reset pour la nouvelle semaine
            data['fleet_status'] = []
            with open('iris_config.json', 'w') as f:
                json.dump(data, f)
            print(f"📁 Archive créée : {archive_path}")
        except FileNotFoundError:
            print("⚠️ Aucun fichier config à archiver.")

if __name__ == "__main__":
    # Ce bloc permet au Workflow GitHub de faire tourner l'archiveur
    archiver_audit()
