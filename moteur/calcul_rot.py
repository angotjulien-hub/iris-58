def calculer_offre_reelle(nb_tours_theo, nb_tours_couples, deviation_active=True):
    # Paramètres Ligne 58
    km_tour_standard = 8.5
    bonus_jaures = 0.4  # +400 mètres par tour
    
    # Calcul
    tours_effectues = nb_tours_theo - nb_tours_couples
    km_theoriques = nb_tours_theo * km_tour_standard
    
    if deviation_active:
        km_reels = tours_effectues * (km_tour_standard + bonus_jaures)
    else:
        km_reels = tours_effectues * km_tour_standard
        
    taux_rot = (km_reels / km_theoriques) * 100
    
    print(f"--- CALCULATEUR ROT IRIS ---")
    print(f"KM Théoriques : {km_theoriques:.2f} km")
    print(f"KM Réels      : {km_reels:.2f} km (Déviation Jaurès: {'OUI' if deviation_active else 'NON'})")
    print(f"Taux de ROT   : {taux_rot:.2f}%")
    
    return taux_rot

# Test : 50 tours prévus, 2 tours sacrifiés pour couplage, mais déviation active
calculer_offre_reelle(50, 2, deviation_active=True)
