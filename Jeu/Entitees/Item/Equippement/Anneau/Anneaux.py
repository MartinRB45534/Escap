from Jeu.Entitees.Item.Equippement.Anneau.Anneau import *

class Anneau_magique(Anneau,Renforce_regen_pm):
    """Un anneau magique : augmente la régénération des pm."""
    def __init__(self,position,taux_regen):
        Equipement.__init__(self,position)
        Renforce_regen_pm.__init__(self,position,taux_regen)

class Anneau_de_vitalite(Anneau,Renforce_regen_pv):
    """Un anneau un peu moins magique : augmente la régénération des pv."""
    def __init__(self,position,taux_regen):
        Equipement.__init__(self,position)
        Renforce_regen_pv.__init__(self,position,taux_regen)