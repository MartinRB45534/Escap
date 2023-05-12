from Jeu.Entitee.Item.Item import *

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire (ne requièrent pas de magie pour être activés)."""
    def __init__(self,controleur:Controleur,effet:Effet,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.effet = effet

    def utilise(self,agissant):
        agissant.ajoute_effet(self.effet)
        self.etat = "brisé"

    def get_description(self,observation=0):
        return ["Une potion","Tu veux la boire ?"]

    def get_classe(self):
        return Potion

    def get_skin(self):
        return SKIN_POTION

    @staticmethod
    def get_image():
        return SKIN_POTION
