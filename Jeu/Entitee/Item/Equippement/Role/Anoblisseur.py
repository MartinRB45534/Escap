from Jeu.Entitee.Item.Equippement.Equippement import *

class Anoblisseur(Equipement):
    """La classe des équipements qui augmentent la priorité."""
    def __init__(self,position:Position,taux_priorite:float):
        Equipement.__init__(self,position)
        self.taux_priorite = taux_priorite

    def augmente_priorite(self,priorite:float):
        taux_priorite = self.taux_priorite
        for taux in self.taux_stats.values():
            taux_priorite *= taux
        return priorite * taux_priorite