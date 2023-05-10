from Jeu.Entitee.Item.Equippement.Haume.Haume import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Haume_type(Haume,Defensif_proportion):
    """Un haume type : défend contre les attaques."""
    def __init__(self,position:Optional[Position]=None,taux_degats:float):
        Haume.__init__(self,position)
        Defensif_proportion.__init__(self,position,taux_degats)
