from Jeu.Entitees.Agissant.Role.Bourrin import *

class Dps(Bourrin):
    """Les agissants chargé d'infliger les dégats."""

    def comporte_distance(self,degats):
        if (self.pv-degats)/self.pv_max > 0.3:
            return 0
        else:
            return 3

    def veut_attaquer(self,degats):
        return (self.pv-degats)/self.pv_max > 0.3 #Appliquer un multiplicateur aux dégats en fonction des moyens de défense du DPS