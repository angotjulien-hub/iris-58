# 🚍 IRIS Prime - Ligne 58 (SRIG 2025)

> **Vision Stratégique :** La Fréquence Prime sur le Kilométrage. 
> Priorité au couplage et à la régularité perçue par le voyageur.

---

### 📊 Indicateurs de Performance (Audit IDFM)
| Indicateur | Objectif 2025 | Méthode de calcul IRIS |
| :--- | :--- | :--- |
| **Indice de Régularité** | > 85% | Écart moyen aux points pivots (18J / Alésia) |
| **ROT (Offre Transport)** | 98% | KM Effectués (incl. Déviation Jaurès) |
| **Taux de Couplage** | < 5% | Détection de "bus en paquet" via GPS |

### 🛠️ Verrous & Actions de Régulation
* **Verrou 18 Juin :** Point de décision critique. Si EID > 1.5x, activer le mode couplage.
* **Relèves Porte de Vanves :** Alerte automatique si le retard impacte la fin de vacation (Objectif +1,8 JA).
* **Déviation Jean Jaurès :** Bascule kilométrique automatique (+0,4 km/tour).

---
### 📁 Structure du Projet
* `/moteur` : Scripts de calcul de la régularité et de l'audit.
* `/referentiel` : Fichiers théoriques (LAV10, SAM30, DIM10).
* `/rapports` : Synthèses de fin de service pour l'unité SRG.
