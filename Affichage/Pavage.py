from __future__ import annotations
from typing import List
from warnings import warn

from .Affichable import Affichable
from .Conteneur import Conteneur
from .Marge import Marge_horizontale, Marge_verticale

class Pavage(Conteneur):
    """Contient des objets, qui s'adaptent au pavage"""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.repartition = [] #La répartition des objets contenus
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_contenu(self,contenu,repartition):
        if all(taille >= 0 for taille in repartition):
            warn("Il n'y a pas d'élément ajustable dans ce pavage !?")
        if len(contenu) != len(repartition):
            warn(f"Hey, {contenu} et {repartition} ne sont pas de même taille !")
        else:
            self.contenu = contenu
            self.repartition = repartition

class Pavage_horizontal(Pavage):
    def set_contenu(self, contenu, repartition):
        if any(isinstance(objet,Marge_horizontale) for objet in contenu):
            warn("Il y a une marge horizontale dans un pavage horizontal !")
        return super().set_contenu(contenu, repartition)

    def set_tailles(self,tailles):
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            if tailles == (0,0):
                warn(f"Tailles nulles pour {self} !")
            else:
                raise RuntimeError(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[0]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            somme = 0
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[0]
                self.contenu[i].set_tailles([int(taille),tailles[1]])
                self.contenu[i].set_position([somme,0])
                somme += taille
        self.tailles = tailles

    def get_tailles(self,tailles):
        somme = 0
        maxi = 0
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            warn(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[0]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[0]
                tailles_effectives = self.contenu[i].get_tailles([int(taille),tailles[1]])
                somme += tailles_effectives[0]
                maxi = max(maxi,tailles_effectives[1])
        return [somme,maxi]

class Pavage_vertical(Pavage):
    def set_contenu(self, contenu, repartition):
        if any(isinstance(objet,Marge_verticale) for objet in contenu):
            warn("Il y a une marge verticale dans un pavage vertical !")
        return super().set_contenu(contenu, repartition)

    def set_tailles(self,tailles):
        libre = tailles[1] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            if tailles == (0,0):
                warn(f"Tailles nulles pour {self} !")
            else:
                raise RuntimeError(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[1]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            somme = 0
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[1]
                self.contenu[i].set_tailles([tailles[0],int(taille)])
                self.contenu[i].set_position([0,somme])
                somme += taille
        self.tailles = tailles

    def get_tailles(self,tailles):
        somme = 0
        maxi = 0
        libre = tailles[1] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            warn(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[1]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[1]
                tailles_effectives = self.contenu[i].get_tailles([tailles[0],int(taille)])
                somme += tailles_effectives[1]
                maxi = max(maxi,tailles_effectives[0])
        return [maxi,somme]
