import pandas as pd

class GestionnaireDeviations:
    def __init__(self):
        # Référentiel des déviations ligne 58
        self.catalogue = {
            "JAURES": {"nom": "Jean Jaurès", "bonus": 0.4, "active": True},
            "ALESIA": {"nom": "Travaux Alésia", "bonus": 0.2, "active": False},
            "MARCHE": {"nom": "Marché de Vanves", "bonus": -0.15, "active": False}
        }

    def obtenir_bonus_total(self):
        """Calcule le supplément km total par tour"""
        return sum(d["bonus"] for d in self.catalogue.values() if d["active"])

    def generer_rapport_textuel(self):
        """Prépare le texte pour le Dashboard GitHub"""
        actives = [d["nom"] for d in self.catalogue.values() if d["active"]]
        if not actives:
            return "✅ Parcours Standard (Aucune déviation)"
        return "🚧 Actives : " + ", ".join(actives)

# Test rapide
if __name__ == "__main__":
    g = GestionnaireDeviations()
    print(f"Bonus actuel : {g.obtenir_bonus_total()} km/tour")
    print(g.generer_rapport_textuel())
