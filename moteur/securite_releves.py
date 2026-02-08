def verifier_securite_releve(voiture, retard_actuel, heure_fin_service):
    # On définit une marge de sécurité de 5 minutes
    marge_securite = 5 
    
    # Simulation du calcul
    impact_fin_service = retard_actuel + marge_securite
    
    print(f"--- ANALYSE RELÈVE VOITURE {voiture} ---")
    if impact_fin_service > 15:
        return f"🚨 ALERTE ROUGE : Relève compromise (+{impact_fin_service}min). Suggérer SERVICE PARTIEL."
    elif impact_fin_service > 10:
        return f"⚠️ VIGILANCE : Relève tendue. Surveillance accrue à Porte de Vanves."
    else:
        return f"✅ Relève sécurisée (Marge : {15 - impact_fin_service}min)."

# Test pour une voiture à Alésia qui a 12min de retard
print(verifier_securite_releve("V58-12", 12, "14:30"))
