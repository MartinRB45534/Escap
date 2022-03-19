from Jeu.Entitee.Item.Equippement.Haume.Haume import *

class Haume_type(Haume,Defensif_proportion):
    """Un haume type : défend contre les attaques."""
    def __init__(self,position,taux_degats):
        Haume.__init__(self,position)
        Defensif_proportion.__init__(self,position,taux_degats)
