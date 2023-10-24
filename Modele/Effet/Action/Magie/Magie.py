from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....entitee.entitee import Entitee
    from ....entitee.agissant.agissant import Agissant
    from ....entitee.item.projectile.projectile import Projectile
    from ....entitee.item.item import Item
    from ...effet import Effet
    from ...enchantements import Enchantement
    from ....systeme.skill.actif import Actif

# Imports des classes parentes
from ..action import Non_repetable
from ..caste import Caste
from ..action_skill import Action_skill

class Magie(Caste,Action_skill):
    """La classe des magies. Précédemment un effet."""
    nom = "magie" # Vraiment utile ?
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,niveau:int): #Toutes ces caractéristiques sont déterminées par la sous-classe au moment de l'instanciation, en fonction de la magie utilisée et du niveau.
        super().__init__(agissant, latence)
        self.skill = skill
        self.gain_xp = gain_xp
        self.cout = cout_pm
        self.niveau = niveau

class Magies_offensives(Magie):
    """Les magies qui produisent un effet d'attaque"""

class Magie_dirigee(Magie) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,direction:Optional[crt.Direction]=None):
        self.direction = direction

class Magie_cout(Magie, Non_repetable):
    """La classe des magies dont le coût peut varier."""

    def set_cout(self,cout:float):
        self.cout = cout
    
class Magie_cible(Magie) :
    """La classe des magies qui nécessitent une (ou parfois plusieurs) cible(s)."""

class Multi_cible(Magie_cible) :
    """La classe des magies qui nécessitent plusieurs cibles."""

class Magie_cible_dirigee(Magie_cible,Magie_dirigee):
    """La classe des magies qui nécessitent une direction et une cible."""

class Portee_limitee(Magie_cible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,portee_limite:float):
        self.portee_limite = portee_limite

class Cible_agissant(Magie_cible):
    """La classe des magies qui ciblent des agissants."""
    def __init__(self, cible:Optional[Agissant]):
        self.cible = cible

class Cible_agissants(Multi_cible):
    """La classe des magies qui ciblent plusieurs agissants."""
    def __init__(self, cible:List[Agissant]):
        self.cible = cible

class Cible_item(Magie_cible):
    """La classe des magies qui ciblent des items."""
    def __init__(self, cible:Optional[Item]):
        self.cible = cible

class Cible_items(Multi_cible):
    """La classe des magies qui ciblent plusieurs items."""
    def __init__(self, cible:List[Item]):
        self.cible = cible

class Cible_case(Magie_cible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    def __init__(self, cible:Optional[crt.Position]):
        self.cible = cible

class Cible_cases(Multi_cible):
    """La classe des magies qui ciblent plusieurs cases."""
    def __init__(self, cible:List[crt.Position]):
        self.cible = cible

# Normalement on en a fini avec les magies ciblées

class Invocation(Magie):
    """La classe des magies qui créent une entitée (un agissant pour se battre à vos côtés, un projectile magique pour attaquer les ennemis, un item à utiliser plus tard..."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Entitee,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Invocation_projectile(Invocation,Magie_dirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Projectile,direction:Optional[crt.Direction],niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        Magie_dirigee.__init__(self,direction)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Creation_effet(Magie):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,effet:Effet,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.effet = effet

    def get_effet(self):
        return self.effet

class Enchante(Creation_effet, Magie_cible, Non_repetable):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.enchantement = enchantement

    def get_enchantement(self):
        return self.enchantement

class Enchante_item(Enchante, Cible_item):
    """La classe des magies qui enchantent un item."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement,item:Optional[Item],niveau:int):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement,niveau)
        Cible_item.__init__(self,item)

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)

class Enchante_cases(Enchante, Cible_cases):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement,cases:List[crt.Position],niveau:int):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement,niveau)
        Cible_cases.__init__(self,cases)

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            for case in self.cible:
                self.agissant.labyrinthe.get_case(case).effets.add(self.enchantement)

class Enchante_agissant(Enchante, Cible_agissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement,cible:Optional[Agissant],niveau:int):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement,niveau)
        Cible_agissant.__init__(self,cible)

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)