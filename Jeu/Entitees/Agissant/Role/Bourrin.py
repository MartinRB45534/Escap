from Jeu.Entitees.Agissant.Agissant import *

class Bourrin(Agissant):
    """Les agissants qui combattent en fonçant dans le tas."""

    def veut_fuir(self,degats=0):
        return not(self.veut_attaquer(degats)) #Il n'y a pas d'autre choix que fuir ou attaquer