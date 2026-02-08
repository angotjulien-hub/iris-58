import json
import datetime
import os

class HubReceptionP2P:
    def __init__(self):
        # Tes deux fichiers cibles
        self.log_file = "referentiel/flux_live_2026.json"
        self.heatmap_file = "heatmap_coords.json"

    def connecter_machiniste(self, id_voiture, position_actuelle, retard_secondes):
        timestamp = datetime.datetime.now().isoformat()
        
        # Nettoyage de la position pour le calcul (extraction lat/lon)
        try:
            lat, lon = map(float, position_actuelle.split(','))
        except:
            lat, lon = 48.828, 2.327 # Valeur par défaut Alésia

        donnee = {
            "timestamp": timestamp,
            "voiture": id_voiture,
            "lat": lat,
            "lon": lon,
            "retard_sec": retard_secondes,
            "statut": "CONNECTÉ"
        }
        
        if retard_secondes > 600:
            donnee["alerte"] = "⚠️ RISQUE COUPLAGE - Rétention suggérée"
        
        self._sauvegarder_flux(donnee)
        self._generer_heatmap() # On met à jour la carte de chaleur
        return donnee

    def _sauvegarder_flux(self, donnee):
        # 1. Archive historique (ton mode actuel)
        with open(self.log_file, "a") as f:
            f.write(json.dumps(donnee) + "\n")

    def _generer_heatmap(self):
        # 2. Génération du fichier pour le PCC (le moteur de la carte)
        if not os.path.exists(self.log_file):
            return
            
        heatmap_points = []
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            # On prend les 50 dernières positions pour ne pas saturer le PCC
            last_lines = lines[-50:] 
            for line in last_lines:
                d = json.loads(line)
                # Intensité basée sur le retard (plus de retard = plus rouge)
                intensite = 0.9 if d.get('retard_sec', 0) > 600 else 0.5
                heatmap_points.append([d['lat'], d['lon'], intensite])

        with open(self.heatmap_file, "w") as f:
            json.dump(heatmap_points, f)

# --- TEST DE CONNEXION LIVE ---
if __name__ == "__main__":
    hub = HubReceptionP2P()
    print("📡 Système IRIS : En attente de flux...")
    # Simulation
    flux = hub.connecter_machiniste("V14", "48.828, 2.327", 720)
    print(f"✅ Audit & Heatmap mis à jour : {flux['voiture']} à Alésia")
