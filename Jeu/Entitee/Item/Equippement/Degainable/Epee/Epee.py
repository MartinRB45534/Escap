from Jeu.Entitee.Item.Equippement.Degainable.Degainable import *

class Epee(Arme):
    """La classe des armes de type épée. Permettent de porter des coups semi-circulaires devant l'agissant."""
    def __init__(self,position:Position,element:int,tranchant:float,portee:int):
        Arme.__init__(self,position,element,tranchant,portee)
        self.poids = 5
        self.frottements = 4

    def get_titre(self,observation=0):
        return "Épée"

    def get_description(self,observation=0):
        return ["Une épée","Pour couper le saucisson."]

    def get_skin(self):
        return SKIN_EPEE