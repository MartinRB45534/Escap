from Jeu.Entitee.Item.Equippement.Role.Reparateur.Reparateur import *

class Pompe_a_pv(Reparateur): #Régénère une quantité fixe de pm
    def __init__(self,position,pv):
        Equipement.__init__(self,position)
        self.pv = pv

    def regen_pv(self,regen_pv):
        pv = self.pv
        for taux in self.taux_stats.values():
            pv *= taux
        return regen_pv + pv

class Renforce_regen_pv(Reparateur): #Démultiplie l'efficacité de la régénération
    def __init__(self,position,taux_pv):
        Equipement.__init__(self,position)
        self.taux_pv = taux_pv

    def regen_pv(self,regen_pv):
        taux_pv = self.pv
        for taux in self.taux_stats.values():
            taux_pv *= taux
        return regen_pv * taux_pv
