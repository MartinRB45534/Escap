from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Entitee.Agissant.Agissant import Agissant
    from ....Labyrinthe.Case import Case

# Imports des classes parentes
from ...Effet import One_shot
from ..Agissant import Effet_agissant
from ...Case.Case import Effet_case

class Antidote(One_shot, Effet_agissant):
    """Effet qui supprime les effets de poison du joueur."""
    def __init__(self, agissant:Agissant):
        self.agissant = agissant

    def action(self):
        for effet in self.agissant.effets:
            if isinstance(effet,Poison):
                self.agissant.effets.remove(effet)

class Medicament(One_shot, Effet_agissant):
    """Effet qui supprime les effets de maladie du joueur."""
    def __init__(self, agissant:Agissant):
        self.agissant = agissant

    def action(self):
        for effet in self.agissant.effets:
            if isinstance(effet,Maladie): # Créer des médicaments différents selon les maladies ?
                self.agissant.effets.remove(effet)

class Purification(One_shot, Effet_agissant):
    """Effet qui supprime les effets de poison ou maladie du joueur."""
    def __init__(self, agissant:Agissant):
        self.agissant = agissant

    def action(self):
        for effet in self.agissant.effets:
            if isinstance(effet,(Maladie,Poison)):
                self.agissant.effets.remove(effet)

class Soin_case(One_shot, Effet_case):
    """Un effet de soin. À répercuter sur les occupants éventuels de la case."""
    def __init__(self,case:Case,gain_pv:float,responsable:Agissant,cible:str="alliés"):
        self.case = case
        self.gain_pv = gain_pv
        self.responsable = responsable
        self.cible = cible

    def action(self):
        cible_potentielle = self.case.agissant
        if cible_potentielle is not None:
            if self.responsable == NOONE: #Pas de responsable. Sérieusement ?
                cible_potentielle.effets.append(Soin(cible_potentielle,self.responsable,self.gain_pv))
            else:
                esprit = self.responsable.esprit
                if esprit == NOBODY: #Pas d'esprit ? Sérieusement ?
                    cible_potentielle.effets.append(Soin(cible_potentielle,self.responsable,self.gain_pv))
                elif self.cible == "alliés" and cible_potentielle in esprit.corps:
                    cible_potentielle.effets.append(Soin(cible_potentielle,self.responsable,self.gain_pv))
                elif self.cible == "neutres" and not cible_potentielle in esprit.corps:
                    cible_potentielle.effets.append(Soin(cible_potentielle,self.responsable,self.gain_pv))

class Soin(One_shot, Effet_agissant):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    def __init__(self,agissant:Agissant,responsable:Agissant,gain_pv:float):
        self.agissant = agissant
        self.responsable = responsable
        self.gain_pv = gain_pv

    def action(self):
        self.agissant.soigne(self.gain_pv)

# Imports utilisés dans le code
from .Maladies.Maladie import Maladie
from .Poison import Poison
from ....Entitee.Agissant.Agissant import NOONE
from ....Esprit.Esprit import NOBODY