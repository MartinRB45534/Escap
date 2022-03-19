from Jeu.Entitee.Item.Equippement.Equippement import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Haume(Equipement):
    """La classe des équipements de type haume. On ne peut en porter qu'un à la fois."""
    def __init__(self,position):
        Equipement.__init__(self,position)
        self.poids = 3 #C'est plutôt léger.
        self.frottements = 6

    def get_classe(self):
        return Haume

    def get_titre(self,observation):
        return "Haume"

    def get_description(self,observation):
        return ["Un haume","..."]

    def get_image():
        return SKIN_CASQUE

    def get_skin(self):
        return SKIN_CASQUE_BASIQUE
