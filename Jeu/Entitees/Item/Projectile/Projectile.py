from Jeu.Entitees.Item.Item import *

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,position,vitesse,effets):
        Item.__init__(self,position)
        self.vitesse = vitesse
        self.effets = effets #Les effets déclenché lors du choc avec un agissant.

    def get_classe(self):
        return Projectile

    def get_titre(self,observation):
        return "Projectile"

    def get_image():
        return SKIN_PROJECTILE