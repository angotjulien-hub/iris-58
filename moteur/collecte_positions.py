import json
import datetime

class HubReceptionP2P:
    def __init__(self):
        self.log_file = "referentiel/flux_live_2026.json"

    def connecter_machiniste(self, id_voiture, position_actuelle, retard_secondes):
        """
        Simule la réception d'une donnée P2P
        """
        timestamp = datetime.datetime.now().isoformat()
        donnee = {
            "timestamp": timestamp,
            "voiture": id_voiture,
            "gps": position_actuelle,
            "retard_sec": retard_secondes,
            "statut": "CONNECTÉ"
        }
        
        # Traitement immédiat : Alerte couplage si retard > 600s (10min)
        if retard_secondes > 600:
            donnee["alerte"] = "⚠️ RISQUE COUPLAGE - Rétention suggérée"
        
        self._sauvegarder_flux(donnee)
        return donnee

    def _sauvegarder_flux(self, donnee):
        # On simule l'écriture dans un registre de flux permanent
        with open(self.log_file, "a") as f:
            f.write(json.dumps(donnee) + "\n")

# --- TEST DE CONNEXION LIVE ---
if __name__ == "__main__":
    hub = HubReceptionP2P()
    # Le machiniste de la voiture 14 se connecte à Alésia
    print("📡 En attente de connexion machiniste...")
    flux = hub.connecter_machiniste("V14", "48.828, 2.327", 720) # 12 min de retard
    print(f"✅ Donnée reçue : {flux['voiture']} - {flux.get('alerte', 'Régulier')}")
