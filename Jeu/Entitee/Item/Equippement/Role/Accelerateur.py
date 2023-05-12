from Jeu.Entitee.Item.Equippement.Equippement import *

class Accelerateur(Equipement):
    """La classe des équipements qui augmentent la vitesse."""
    def __init__(self,taux_vitesse:float):
        self.taux_vitesse = taux_vitesse

    def augmente_vitesse(self,vitesse:float):
        taux_vitesse = self.taux_vitesse
        for taux in self.taux_stats.values():
            taux_vitesse *= taux
        return vitesse * taux_vitesse
