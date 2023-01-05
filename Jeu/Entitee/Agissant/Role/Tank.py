from Jeu.Entitee.Agissant.Role.Bourrin import *

class Tank(Bourrin):
    """Les agissants avec une bonne défense, supposés prendre les dégats."""

    def comporte_distance(self,degats:float):
        if (self.pv-degats)/self.pv_max > 0.2:
            return 0
        else:
            return 3

    def veut_attaquer(self,degats:float=0):
        return (self.pv-degats)/self.pv_max > 0.2 #Appliquer un multiplicateur aux dégats en fonction des moyens de défense du tank
