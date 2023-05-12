from Jeu.Entitee.Item.Equippement.Equippement import *

class Equipement_tribal(Equipement):
    def __init__(self,espece:str,taux:float):
        self.espece = espece
        self.taux = taux

    def equippe(self,agissant:Agissant):
        if not self.espece in agissant.especes :
            self.taux_stats["incompatibilité porteur"] = self.taux
