"""
Contient les classes liées aux pavages
"""

from __future__ import annotations
from typing import Optional

from .affichable import Affichable
from .conteneur import Conteneur
from .marge import MargeHorizontale, MargeVerticale

from .erreur import DisplayError

class Pavage(Conteneur):
    """Contient des objets, qui s'adaptent au pavage"""
    def __init__(self):
        super().__init__()
        self.repartition = [] #La répartition des objets contenus

    def set_contenu(self, contenu:list[Affichable], repartition:Optional[list[int]]=None):
        if repartition is None:
            repartition = [0]*len(contenu)
        elif len(contenu) != len(repartition):
            raise ValueError(f"Hey, {contenu} et {repartition} ne sont pas de même taille !")
        else:
            self.contenu = contenu
            self.repartition = repartition

class PavageHorizontal(Pavage):
    """Un pavage horizontal"""
    def set_contenu(self, contenu:list[Affichable], repartition:Optional[list[int]]=None):
        if any(isinstance(objet,MargeHorizontale) for objet in contenu):
            raise ValueError("Il y a une marge horizontale dans un pavage horizontal !")
        return super().set_contenu(contenu, repartition)

    def set_tailles(self,tailles:tuple[int,int]):
        libre = tailles[0] - sum(
            self.repartition[i] if self.repartition[i]>0 else
            self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else
            0 for i in range(len(self.repartition)))
        if libre < 0:
            if tailles == (0,0):
                raise ValueError(f"Tailles nulles pour {self} !")
            else:
                raise RuntimeError(f"""Je ne peux pas faire rentrer {self.contenu} ({
                    [self.repartition[i] if self.repartition[i]>0 else
                     self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else
                     0 for i in range(len(self.contenu))]
                    }) en {self.repartition} ({tailles[0]}) dans {self} !""")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            somme = 0
            for i, contenu in enumerate(self.contenu):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=contenu.get_tailles(tailles)[0]
                contenu.set_tailles((int(taille),tailles[1]))
                contenu.set_position((int(somme),0))
                somme += taille
        self.tailles = tailles

    def get_tailles(self,tailles:tuple[int,int]):
        somme = 0
        maxi = 0
        libre = tailles[0] - sum(
            self.repartition[i] if self.repartition[i]>0 else
            self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else
            0 for i in range(len(self.repartition)))
        if libre < 0:
            raise RuntimeError(f"""Je ne peux pas faire rentrer {self.contenu} ({
                [self.repartition[i] if self.repartition[i]>0 else
                 self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else
                 0 for i in range(len(self.contenu))]
                }) en {self.repartition} ({tailles[0]}) dans {self} !""")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            for i, contenu in enumerate(self.contenu):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=contenu.get_tailles(tailles)[0]
                tailles_effectives = contenu.get_tailles((int(taille),tailles[1]))
                somme += tailles_effectives[0]
                maxi = max(maxi,tailles_effectives[1])
        return (somme,maxi)

class PavageVertical(Pavage):
    """Un pavage vertical"""
    def set_contenu(self, contenu:list[Affichable], repartition:Optional[list[int]]=None):
        if any(isinstance(objet,MargeVerticale) for objet in contenu):
            raise ValueError("Il y a une marge verticale dans un pavage vertical !")
        return super().set_contenu(contenu, repartition)

    def set_tailles(self,tailles:tuple[int,int]):
        libre = tailles[1] - sum(
            self.repartition[i] if self.repartition[i]>0 else
            self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else
            0 for i in range(len(self.repartition)))
        if libre < 0:
            if tailles == (0,0):
                raise DisplayError(f"Tailles nulles pour {self} !")
            else:
                raise RuntimeError(f"""Je ne peux pas faire rentrer {self.contenu} ({
                    [self.repartition[i] if self.repartition[i]>0 else
                     self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i])
                     else 0 for i in range(len(self.contenu))
                    ]}) en {self.repartition} ({tailles[1]}) dans {self} !""")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            somme = 0
            for i, contenu in enumerate(self.contenu):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=contenu.get_tailles(tailles)[1]
                contenu.set_tailles((tailles[0],int(taille)))
                contenu.set_position((0,int(somme)))
                somme += taille
        self.tailles = tailles

    def get_tailles(self,tailles:tuple[int,int]):
        somme = 0
        maxi = 0
        libre = tailles[1] - sum(
            self.repartition[i] if self.repartition[i]>0 else
            self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else
            0 for i in range(len(self.repartition)))
        if libre < 0:
            raise RuntimeError(f"""Je ne peux pas faire rentrer {self.contenu} ({
                [self.repartition[i] if self.repartition[i]>0 else
                 self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else
                 0 for i in range(len(self.contenu))
                ]}) en {self.repartition} ({tailles[1]}) dans {self} !""")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            for i, contenu in enumerate(self.contenu):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=contenu.get_tailles(tailles)[1]
                tailles_effectives = contenu.get_tailles((tailles[0],int(taille)))
                somme += tailles_effectives[1]
                maxi = max(maxi,tailles_effectives[0])
        return (maxi,somme)

class PavageMarge(Pavage):
    """Une liste avec des marges automatiques."""
    def __init__(self, marge: int = 5):
        Pavage.__init__(self)
        self.marge = marge

    def set_contenu(self, contenu: list[Affichable], repartition: Optional[list[int]] = None):
        if repartition is None:
            repartition = [0] * len(contenu)
        elif len(contenu) != len(repartition):
            raise ValueError(f"Hey, {contenu} et {repartition} ne sont pas de même taille !")
        self.contenu = [(MargeHorizontale() if isinstance(self, PavageVertical) else
                         MargeVerticale()) if i % 2 else
                         contenu[i // 2] for i in range(2 * len(contenu) - 1)]
        self.repartition = [self.marge if i%2 else
                            repartition[i//2] for i in range(2*len(repartition)-1)]

class PavageHorizontalMarge(PavageMarge, PavageHorizontal):
    """Un pavage horizontal avec des marges automatiques."""

class PavageVerticalMarge(PavageMarge, PavageVertical):
    """Un pavage vertical avec des marges automatiques."""
