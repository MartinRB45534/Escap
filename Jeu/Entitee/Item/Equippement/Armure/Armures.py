from Jeu.Entitee.Item.Equippement.Armure.Armure import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Armure_type(Armure,Defensif_proportion):
    """Une armure type : défend contre les attaques."""
    def __init__(self,controleur:Controleur,taux_degats:float,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats)
