from Jeu.Entitees.Item.Equippement.Roles.Reparateur_magique.Reparateur_magique import *

class Pompe_a_pm(Reparateur_magique): #Régénère une quantité fixe de pm
    def __init__(self,position,pm):
        Equipement.__init__(self,position)
        self.pm = pm

    def regen_pm(self,regen_pm):
        pm = self.pm
        for taux in self.taux_stats.values():
            pm *= taux
        return regen_pm + pm

class Renforce_regen_pm(Reparateur_magique): #Démultiplie l'efficacité de la régénération
    def __init__(self,position,taux_pm):
        Equipement.__init__(self,position)
        self.taux_pm = taux_pm

    def regen_pm(self,regen_pm):
        taux_pm = self.pm
        for taux in self.taux_stats.values():
            taux_pm *= taux
        return regen_pm * taux_pm
