from Jeu.Entitee.Item.Equippement.Haume.Haume import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Haume_type(Haume,Defensif_proportion):
    """Un haume type : défend contre les attaques."""
    def __init__(self,controleur:Controleur,taux_degats:float,position:Position=ABSENT):
        Haume.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats)
