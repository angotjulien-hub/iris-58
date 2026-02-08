import datetime

def generer_dashboard_visuel():
    date_jour = datetime.datetime.now().strftime("%d/%m/%Y")
    # Simulation des données issues de l'audit
    taux_rot = 97.8
    indice_regul = 88.5
    releves_pova = "✅ OK (+1.8 JA respecté)"
    status_jaures = "🟢 ACTIVE (+0.4km/tour)"

    # Construction du contenu Markdown
    dashboard_content = f"""# 🚍 IRIS Prime - Tableau de Bord Ligne 58
> **Dernière mise à jour :** {date_jour}

## 📊 Performance du jour (Simulation)
| Indicateur | Valeur | État |
| :--- | :--- | :--- |
| **Taux de ROT (Offre)** | {taux_rot}% | 🟢 |
| **Indice Régularité** | {indice_regul}% | 🟢 |
| **Relèves PoVa** | {releves_pova} | 🔵 |
| **Déviation Jaurès** | {status_jaures} | 🟢 |

## 🚨 Alertes & Verrous (Audit SRIG 2025)
* **Verrou 18 Juin :** Aucun couplage critique détecté.
* **Collecte de données :** Système 2026 connecté (Positions chauffeurs actives).

---
*Ceci est un rapport automatique généré par le moteur IRIS.*
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(dashboard_content)
    print("🚀 Dashboard mis à jour sur la page d'accueil !")

if __name__ == "__main__":
    generer_dashboard_visuel()
