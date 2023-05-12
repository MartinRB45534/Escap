from Jeu.Entitee.Agissant.Agissant import *

class Fuyard(Agissant):
    """Des agissants qui ne font que fuire ? À quoi bon ?"""

    def comporte_distance(self,degats:float):
        return 3

    def veut_attaquer(self):
        return False

    def veut_fuir(self,degats:float=0):
        return True
