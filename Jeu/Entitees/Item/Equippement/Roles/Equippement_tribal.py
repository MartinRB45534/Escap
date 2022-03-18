from Jeu.Entitees.Item.Equippement.Equippement import *

class Equipement_tribal(Equipement):
    def __init__(self,position,espece,taux):
        self.espece = espece
        self.taux = taux

    def equippe(self,agissant):
        if not self.espece in agissant.especes :
            self.taux_stats["incompatibilité porteur"] = self.taux
            if agissant.ID==2:
                agissant.affichage.message("Cet équipement est destiné aux {self.espece}s, donc ses stats ont été réduites.")
