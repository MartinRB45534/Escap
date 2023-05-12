from Jeu.Entitee.Item.Equippement.Anneau.Anneau import *
from Jeu.Entitee.Item.Equippement.Role.Roles import *

class Anneau_magique(Anneau,Renforce_regen_pm):
    """Un anneau magique : augmente la régénération des pm."""
    def __init__(self,controleur:Controleur,taux_regen:float,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        Renforce_regen_pm.__init__(self,taux_regen)

class Anneau_de_vitalite(Anneau,Renforce_regen_pv):
    """Un anneau un peu moins magique : augmente la régénération des pv."""
    def __init__(self,controleur:Controleur,taux_regen:float,position:Position=ABSENT):
        Equipement.__init__(self,controleur,position)
        Renforce_regen_pv.__init__(self,taux_regen)
