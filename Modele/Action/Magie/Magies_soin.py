from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Agissant import Agissant
    from ...Systeme.Skill.Actif import Actif

# Imports des classes parentes
from ..Action import Non_repetable
from .Magie import Cible_agissant,Cible_case,Portee_limitee,Magie,Cible_agissants

class Magie_soin(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie soin"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,niveau:int,cible:Optional[Agissant]=None):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_agissant.__init__(self,cible)
        self.gain_pv = gain_pv

    def action(self,lanceur:Agissant):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(Soin(lanceur,self.gain_pv))

class Magie_multi_soin(Cible_agissants):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""
    nom = "magie multi soin"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,niveau:int,cible:List[Agissant]=[]):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_agissants.__init__(self,cible)
        self.gain_pv = gain_pv

    def action(self,lanceur:Agissant):
        for cible in self.cible:
            cible.effets.append(Soin(lanceur,self.gain_pv))

class Magie_soin_de_zone(Cible_case):
    """La magie qui invoque un effet de soin sur une zone."""
    nom = "magie zone de soin"
    def __init__(self,niveau:int,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,portee:float,case:Optional[crt.Position]=None):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_case.__init__(self,case)
        self.gain_pv = gain_pv
        self.portee = portee

    def action(self,lanceur:Agissant):
        if self.cible is None:
            self.interrompt()
        else:
            poss = lanceur.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for pos in poss:
                lanceur.labyrinthe.get_case(pos).effets.add(Soin_case(self.gain_pv,lanceur))

class Magie_auto_soin(Magie):
    """La magie qui invoque un effet de soin sur son lanceur."""
    nom = "magie auto soin"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,gain_pv:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.gain_pv = gain_pv
        self.niveau = niveau

class Magie_resurection(Magie, Non_repetable):
    """La magie qui invoque un effet de resurection."""
    nom = "magie resurection"
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)

    def action(self,lanceur:Agissant):
        cadavre = lanceur.inventaire.get_item_courant() # TODO : la notion d'item courant n'existe plus
        if isinstance(cadavre,Cadavre):
            lanceur.inventaire.drop(lanceur.labyrinthe.get_case(lanceur.position),cadavre)
            cadavre.effets.append(Resurection())

class Magie_reanimation_de_zone(Cible_case,Portee_limitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    nom = "magie reanimation"
    def __init__(self,niveau:int,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,taux_pv:float,portee:float,portee_limite:float,superiorite:int,case:Optional[crt.Position]=None):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Cible_case.__init__(self,case)
        self.taux_pv = taux_pv
        self.portee = portee
        self.portee_limite = portee_limite
        self.superiorite = superiorite

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            zone = self.agissant.labyrinthe.a_portee(self.cible,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(True, False, False, True, True))
            for position in zone:
                for item in self.agissant.labyrinthe.get_case(position).items:
                    if isinstance(item,Cadavre):
                        if item.get_priorite()+self.superiorite < self.agissant.get_priorite():
                            item.effets.append(Reanimation(self.taux_pv,self.agissant.esprit))

# Imports utilisés dans le code
from ...Entitee.Item.Cadavre import Cadavre
from ...Effet.Sante.Reanimation import Reanimation
from ...Effet.Sante.Resurection import Resurection
from ...Effet.Sante.Soins import Soin, Soin_case
from ...Labyrinthe.Deplacement import Deplacement
from ...Labyrinthe.Forme import Forme
from ...Labyrinthe.Passage import Passage