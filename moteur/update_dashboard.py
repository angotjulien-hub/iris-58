import datetime
import os
# On importe ton nouveau module
from gestion_deviations import GestionnaireDeviations

def mettre_a_jour_dashboard():
    # 1. Initialisation des modules
    g_dev = GestionnaireDeviations()
    bonus_km = g_dev.obtenir_bonus_total()
    texte_deviations = g_dev.generer_rapport_textuel()

    # 2. Simulation des calculs de performance
    # Imaginons 50 tours prévus et 2 couplages (suppressions partielles)
    nb_tours_theo = 50
    nb_tours_reels = 48
    km_par_tour = 8.5
    
    km_theo = nb_tours_theo * km_par_tour
    # On ajoute le bonus km sur les tours réellement effectués
    km_reels = nb_tours_reels * (km_par_tour + bonus_km)
    
    taux_rot = (km_reels / km_theo) * 100
    date_jour = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")

    # 3. Rédaction du Dashboard (Markdown)
    contenu = f"""# 🚍 IRIS Prime - Pilotage Ligne 58 (Audit 2025)
> **Dernière analyse :** {date_jour}

## 📊 Performance Kilométrique (ROT)
| Indicateur | Valeur | État |
| :--- | :--- | :--- |
| **Taux de ROT** | **{taux_rot:.2f}%** | {'🟢' if taux_rot >= 98 else '🟠'} |
| **Kilomètres Théoriques** | {km_theo:.1f} km | - |
| **Kilomètres Réels (+Bonus)** | {km_reels:.1f} km | 📈 |

## 🚧 État des Déviations (Moteur IRIS)
* **Statut actuel :** {texte_deviations}
* **Impact cumulé :** +{bonus_km} km / tour effectué.

## 🚨 Alertes Régulation
* **Priorité Couplage :** Active (Conforme instruction 01/02).
* **Relèves PoVa :** En attente de connexion flux 2026.

---
*Rapport automatique généré pour l'unité Seine Rive Gauche.*
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(contenu)
    print("🚀 Dashboard mis à jour avec le bonus déviation !")

if __name__ == "__main__":
    mettre_a_jour_dashboard()
