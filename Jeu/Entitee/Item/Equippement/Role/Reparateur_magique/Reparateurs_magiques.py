from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Item.Equippement.Role.Reparateur_magique.Reparateur_magique import Reparateur_magique

class Pompe_a_pm(Reparateur_magique): #Régénère une quantité fixe de pm
    def __init__(self,pm:float):
        self.pm = pm

    def regen_pm(self,regen_pm:float):
        pm = self.pm
        for taux in self.taux_stats.values():
            pm *= taux
        return regen_pm + pm

class Renforce_regen_pm(Reparateur_magique): #Démultiplie l'efficacité de la régénération
    def __init__(self,taux_pm:float):
        self.taux_pm = taux_pm

    def regen_pm(self,regen_pm:float):
        taux_pm = self.taux_pm
        for taux in self.taux_stats.values():
            taux_pm *= taux
        return regen_pm * taux_pm
