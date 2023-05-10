from Jeu.Entitee.Item.Equippement.Armure.Armure import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Armure_type(Armure,Defensif_proportion):
    """Une armure type : défend contre les attaques."""
    def __init__(self,position:Optional[Position]=None,taux_degats:float):
        Armure.__init__(self,position)
        Defensif_proportion.__init__(self,position,taux_degats)
