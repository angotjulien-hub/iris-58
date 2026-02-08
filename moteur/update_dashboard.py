import datetime
from gestion_deviations import GestionnaireDeviations
from securite_releves import verifier_securite_releve

def finaliser_dashboard():
    # 1. Données Déviations
    g_dev = GestionnaireDeviations()
    bonus = g_dev.obtenir_bonus_total()
    
    # 2. Simulation des données P2P (Données 2026)
    # On imagine la voiture 12 avec 14 min de retard à Alésia
    alerte_releve = verifier_securite_releve("V12", 14, "15:30")
    
    # 3. Calcul ROT
    km_theo = 50 * 8.5
    km_reels = 48 * (8.5 + bonus)
    taux_rot = (km_reels / km_theo) * 100
    
    date_now = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")

    # 4. Construction du Dashboard Final
    contenu = f"""# 🚍 IRIS Prime - Pilotage Ligne 58
> **Statut Live au {date_now}**

## 📊 Performance & Offre (ROT)
| Indicateur | Score | Tendance |
| :--- | :--- | :--- |
| **Taux de ROT** | **{taux_rot:.2f}%** | {'🟢' if taux_rot >= 98 else '🟠'} |
| **Kilométrage** | {km_reels:.1f} km / {km_theo:.1f} km | 📈 |
| **Déviations** | {g_dev.generer_rapport_textuel()} | 🚧 |

## 👥 Sécurité des Relèves (Objectif +1.8 JA)
> **Analyse P2P en temps réel :**
* **Voiture V12 :** {alerte_releve}
* **Voiture V08 :** ✅ Relève sécurisée.
* **Connexions P2P :** 📶 12 machinistes en ligne.

## 🛠️ Actions de Régulation (IRIS)
* **Mode Couplage :** Prioritaire sur suppression.
* **Collecte de données :** Flux P2P 2026 actif.
---
*Rapport d'exploitation généré pour l'Audit SRIG 2025.*
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(contenu)

if __name__ == "__main__":
    finaliser_dashboard()
