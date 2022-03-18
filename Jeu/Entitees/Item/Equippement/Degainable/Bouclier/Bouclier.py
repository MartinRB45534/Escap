from Jeu.Entitees.Item.Equippement.Degainable.Degainable import *

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    def __init__(self,position,degats_bloques,taux_degats):
        Equipement.__init__(self,position)
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats
        self.taux_stats = {}
        self.poids = 5
        self.frottements = 1 #En mode frisbee ça volle très bien !

    def intercepte(self,attaque):
        attaque.degats -= self.degats_bloques
        if attaque.degats < 0:
            attaque.degats = 0
        else :
            for taux in self.taux_stats.values():
                attaque.degats *=  taux
            attaque.degats *= self.taux_degats

    def get_classe(self):
        return Bouclier

    def get_titre(self,observation):
        return "Bouclier"

    def get_description(self,observation):
        return ["Un frisbee","Ah non, c'est un bouclier !"]

    def get_image():
        return SKIN_BOUCLIER
