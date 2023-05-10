from Jeu.Entitee.Item.Equippement.Role.Reparateur_magique.Reparateur_magique import *

class Pompe_a_pm(Reparateur_magique): #Régénère une quantité fixe de pm
    def __init__(self,position:Optional[Position]=None,pm:float):
        Equipement.__init__(self,position)
        self.pm = pm

    def regen_pm(self,regen_pm:float):
        pm = self.pm
        for taux in self.taux_stats.values():
            pm *= taux
        return regen_pm + pm

class Renforce_regen_pm(Reparateur_magique): #Démultiplie l'efficacité de la régénération
    def __init__(self,position:Optional[Position]=None,taux_pm:float):
        Equipement.__init__(self,position)
        self.taux_pm = taux_pm

    def regen_pm(self,regen_pm:float):
        taux_pm = self.pm
        for taux in self.taux_stats.values():
            taux_pm *= taux
        return regen_pm * taux_pm
