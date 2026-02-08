import json
import datetime

def update_iris_config(new_data):
    file_path = 'iris_config.json'
    
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {"last_update": "", "fleet_status": []}

    # Mise à jour de la flotte
    bus_id = new_data['id']
    updated = False
    
    for bus in config['fleet_status']:
        if bus['id'] == bus_id:
            bus.update({
                "lat": new_data['lat'],
                "lon": new_data['lon'],
                "gap_front": new_data['gap_front'],
                "last_ping": new_data['timestamp']
            })
            updated = True
            break
            
    if not updated:
        config['fleet_status'].append(new_data)

    config['last_update'] = datetime.datetime.now().isoformat()

    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)
        print(f"Audit IRIS : {bus_id} archivé.")

# Exemple d'appel par le moteur GitHub Actions
# update_iris_config(data_from_peerjs)
