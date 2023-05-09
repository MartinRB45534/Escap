from Jeu.Entitee.Agissant.Agissant import *

class Support_lointain(Agissant):
    """Les agissants qui combattent loin de la ligne de front."""

    def comporte_distance(self,degats:float):
        if (self.pv-degats)/self.pv_max >= 0.7:
            return 2
        else:
            return 3

    def veut_attaquer(self,degats:float):
        return (self.pv+degats) <= self.pv_max and (self.pv-degats)/self.pv_max >= 0.7

    def veut_fuir(self,degats:float=0):
        return (self.pv+degats)/self.pv_max < 0.7
