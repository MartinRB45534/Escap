from Jeu.Entitee.Item.Equippement.Equippement import *
# from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Anneau(Equipement):
    """La classe des équipements de type anneau. Le nombre d'anneaux qu'on peut porter dépend de l'espèce. Les anneaux peuvent avoir des effets très différends (magiques pour la plupart)."""
    def __init__(self,position:Optional[Position]=None):
        Equipement.__init__(self,position)
        self.poids = 1 #C'est très léger !
        self.frottement = 2 #Il y a mieux.

    def get_titre(self,observation=0):
        return "Anneau"

    def get_description(self,observation=0):
        return ["Un anneau","Tu peux en porter plusieurs."]

    def get_classe(self):
        return Anneau

    def get_skin(self):
        return SKIN_ANNEAU

    def get_image():
        return SKIN_ANNEAU
