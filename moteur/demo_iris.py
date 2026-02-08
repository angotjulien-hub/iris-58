from audit_performance import IrisEngine
import pandas as pd

def lancer_demo():
    print("🚀 LANCEMENT DU MODE DÉMO - IRIS PRIME LIGNE 58")
    iris = IrisEngine()
    
    # SCÉNARIO : On simule une journée de semaine avec perturbations
    # 1. On crée des données fictives pour l'aperçu
    data_demo = {
        'Voiture': [11, 12, 13, 14, 15],
        'Point_Point': ['18J', '18J', '18J', '18J', '18J'],
        'Ecart_Minutes': [2, 12, 1, 15, 3] # On simule deux gros "trous" de desserte
    }
    df_demo = pd.DataFrame(data_demo)

    # 2. Analyse des alertes de couplage
    print("\n🔍 ANALYSE TEMPS RÉEL (Simulation Verrou 18J) :")
    for index, row in df_demo.iterrows():
        if row['Ecart_Minutes'] > 10:
            print(f"⚠️ Alerte Voiture {row['Voiture']} : Écart {row['Ecart_Minutes']}min -> COUPLAGE SUGGÉRÉ")
        else:
            print(f"✅ Voiture {row['Voiture']} : Intervalle correct")

    # 3. Génération de l'audit final
    print("\n" + "="*40)
    iris.calculer_audit(df_demo)

if __name__ == "__main__":
    lancer_demo()
