from Jeu.Entitee.Item.Equippement.Equippement import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Armure(Equipement):
    """La classe des équipements de type armure. On ne peut en porter qu'une à la fois."""
    def __init__(self,position):
        Equipement.__init__(self,position)
        self.poids = 10 #C'est lourd !
        self.frottements = 8 #Il y a pire.

    def get_classe(self):
        return Armure

    def get_titre(self,observation):
        return "Armure"

    def get_description(self,observation):
        return ["Une armure","Essaye de l'enfiler !"]

    def get_image():
        return SKIN_ARMURE

    def get_skin(self):
        return SKIN_ARMURE_BASIQUE
