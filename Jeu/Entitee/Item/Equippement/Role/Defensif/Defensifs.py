from Jeu.Entitee.Item.Equippement.Role.Defensif.Defensif import *

class Defensif_proportion(Defensif):
    def __init__(self,position,taux_degats):
        Equipement.__init__(self,position)
        self.taux_degats = taux_degats

    def intercepte(self,attaque):
        degats_bloques = self.taux_degats
        for taux in self.taux_stats.values():
            degats_bloques *= taux
        attaque.degats *= (1-degats_bloques)

class Defensif_seuil(Defensif):
    def __init__(self,position,degats):
        Equipement.__init__(self,position)
        self.degats = degats

    def intercepte(self,attaque):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= taux
        if attaque.degats <= degats: #On bloque les attaques trop faibles
            attaque.degats = 0

class Defensif_plafond(Defensif):
    def __init__(self,position,degats):
        Equipement.__init__(self,position)
        self.degats = degats

    def intercepte(self,attaque):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= 1/taux
        if attaque.degats > degats: #On limite la force des attaques
            attaque.degats = degats

class Defensif_valeur(Defensif):
    def __init__(self,position,degats):
        Equipement.__init__(self,position)
        self.degats = degats

    def intercepte(self,attaque):
        degats = self.degats
        for taux in self.taux_stats.values():
            degats *= taux
        if attaque.degats > degats: #On limite la force des attaques
            attaque.degats -= degats
        else:
            attaque.degats = 0
#On suppose pour l'instant qu'un item défensif n'appartient qu'à une seule de ces catégories
