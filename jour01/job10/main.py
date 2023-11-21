class SimulationInvestissement:
    def __init__(self, montant_initial, taux_rendement_annuel):
        self.montant_initial = montant_initial
        self.taux_rendement_annuel = taux_rendement_annuel

    def calculer_gain_annuel(self):
        gain_annuel = self.montant_initial * (self.taux_rendement_annuel / 100)
        return gain_annuel

    def augmenter_capital(self, augmentation, augmentation_taux):
        self.montant_initial += augmentation
        self.taux_rendement_annuel += augmentation_taux

    def retirer_capital(self, pourcentage_retrait, diminution_taux):
        retrait = self.montant_initial * (pourcentage_retrait / 100)
        self.montant_initial -= retrait
        self.taux_rendement_annuel -= diminution_taux

    def afficher_resultats(self):
        print(f"\nMontant initial de l'investissement : {self.montant_initial} euros")
        print(f"Taux de rendement annuel : {self.taux_rendement_annuel}%")
        print(f"Gain annuel actuel : {self.calculer_gain_annuel()} euros")


# Initialisation de l'investissement
investissement = SimulationInvestissement(montant_initial=50000, taux_rendement_annuel=5)

# Affichage des résultats initiaux
investissement.afficher_resultats()

# Augmentation du capital et du taux de rendement
investissement.augmenter_capital(augmentation=5000, augmentation_taux=2)

# Affichage des résultats après l'augmentation
investissement.afficher_resultats()

# Retrait du capital et diminution du taux de rendement
investissement.retirer_capital(pourcentage_retrait=10, diminution_taux=1)

# Affichage des résultats après le retrait
investissement.afficher_resultats()
