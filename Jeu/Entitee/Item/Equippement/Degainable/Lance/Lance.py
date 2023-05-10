from Jeu.Entitee.Item.Equippement.Degainable.Degainable import *

class Lance(Arme):
    """La classe des armes de type lance. Permettent de porter des coups rectilignes devant l'agissant."""
    def __init__(self,position:Optional[Position]=None,element:int,tranchant:float,portee:int):
        Arme.__init__(self,position,element,tranchant,portee)
        self.poids = 3
        self.frottements = 3

    def get_titre(self,observation=0):
        return "Lance"

    def get_description(self,observation=0):
        return ["Une lance","Pour faire des trous dans les gens."]

    def get_skin(self):
        return SKIN_LANCE
