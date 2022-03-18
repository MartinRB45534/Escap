from Jeu.Entitees.Item.Item import *

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire (ne requièrent pas de magie pour être activés)."""
    def __init__(self,position,effet):
        Item.__init__(self,position)
        self.effet = effet

    def utilise(self,agissant):
        agissant.ajoute_effet(self.effet)
        self.etat = "brisé"

    def get_description(self,observation):
        return ["Une potion","Tu veux la boire ?"]

    def get_classe(self):
        return Potion

    def get_skin(self):
        return SKIN_POTION

    def get_image():
        return SKIN_POTION
