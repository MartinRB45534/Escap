"""
Contient la classe maladie.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import random

# Imports des classes parentes
from ...timings import OnFinTourAgissant
from .....systeme import Nomme

# Imports utilisés dans le code
from .....commons import Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....entitee.agissant.agissant import Agissant

class FamilleMaladie:
    """Une famille qui regroupe plusieurs maladies."""
    maladies:set[type[Maladie]]
    def __init__(self, maladies:set[type[Maladie]]):
        self.maladies = maladies

class Maladie(OnFinTourAgissant, Nomme):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    contagiosite:float
    infectabilite:float
    persistence:float
    distance:float
    virulence:float
    famille:FamilleMaladie
    perte_contagiosite:float
    perte_infectabilite:float
    perte_persistence:float
    guerit_sans_contagiosite:bool
    guerit_sans_infectabilite:bool
    guerit_sans_persistence:bool

    def __init__(self):
        self.guerit = False
        self._virulence = self.virulence

    def fin_tour(self,agissant:Agissant):
        self.contamine(agissant)
        agissant.statistiques.augmente_non_contagieux(self.__class__,self.perte_contagiosite)
        agissant.statistiques.augmente_non_infectable(self.__class__,self.perte_infectabilite)
        agissant.statistiques.augmente_non_affecte(self.__class__,self.perte_persistence)
        self.set_virulence(agissant)
        if (
            (self.guerit_sans_contagiosite or self.contagieux(agissant) == 0) and
            (self.guerit_sans_infectabilite or self.infectable(agissant) == 0) and
            (self.guerit_sans_persistence or self.affecte(agissant) == 0)
        ):
            self.guerit = True

    def contamine(self,agissant:Agissant):
        """Contamine les voisins de l'agissant."""
        contagieux = self.contagieux(agissant)
        zone = agissant.labyrinthe.a_portee(
            agissant.position,self.distance*contagieux,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone :
            voisin = agissant.labyrinthe.get_case(position).agissant
            if voisin:
                self.infecte(voisin)

    def infecte(self,voisin:Agissant):
        """Infecte un agissant."""
        if random.random() < self.infectable(voisin):
            for effet in [*voisin.effets]:
                if isinstance(effet, Maladie) and effet.nom == self.nom:
                    if effet.niveau < self.niveau:
                        voisin.effets.remove(effet)
                        voisin.effets.add(self.__class__()) #Nid à problèmes très potentiel !

    def contagieux(self, agissant:Agissant):
        """Retourne la contagiosité de la maladie pour l'agissant donné."""
        non_contagieux = agissant.statistiques.get_non_contagieux(self.__class__)
        non_contagieux -= self.contagiosite
        return min(1, max(0, 10 - non_contagieux)/10)

    def infectable(self, agissant:Agissant):
        """Retourne l'infectabilité de la maladie pour l'agissant donné."""
        non_infectable = agissant.statistiques.get_non_infectable(self.__class__)
        non_infectable -= self.infectabilite
        return min(1, max(0, 10 - non_infectable)/10)

    def affecte(self, agissant:Agissant):
        """Retourne l'affectabilité de la maladie pour l'agissant donné."""
        non_affecte = agissant.statistiques.get_non_affecte(self.__class__)
        non_affecte -= self.persistence
        return min(1, max(0, 10 - non_affecte)/10)

    def set_virulence(self, agissant:Agissant):
        """Retourne la virulence de la maladie pour l'agissant donné."""
        self._virulence = self.affecte(agissant) * self.virulence

    def termine(self):
        return self.guerit
