from Jeu.Entitee.Item.Equippement.Armure.Armure import *

class Armure_type(Armure,Defensif_proportion):
    """Une armure type : défend contre les attaques."""
    def __init__(self,position,taux_degats):
        Armure.__init__(self,position)
        Defensif_proportion.__init__(self,position,taux_degats)
