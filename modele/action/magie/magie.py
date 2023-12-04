"""
Les classes de base des magies.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import carte as crt

# Imports des classes parentes
from ..action import NonRepetable
from ..caste import Caste
from ..action_skill import ActionSkill

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.entitee import Entitee
    from ...entitee.agissant.agissant import Agissant
    from ...entitee.item.projectile.projectile import Projectile
    from ...entitee.item.item import Item
    from ...effet.effet import Effet
    from ...effet.enchantement import Enchantement
    from ...effet.agissant.enchantement import EnchantementAgissant
    from ...effet.case.enchantement import EnchantementCase
    from ...effet.item.enchantement import EnchantementItem
    from ...systeme.skill.actif import Actif

class Magie(Caste,ActionSkill):
    """La classe des magies. Précédemment un effet."""
    nom = "magie" # Vraiment utile ?
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float): #Toutes ces caractéristiques sont déterminées par la sous-classe au moment de l'instanciation, en fonction de la magie utilisée et du niveau.
        super().__init__(agissant, latence)
        self.skill = skill
        self.gain_xp = gain_xp
        self.cout = cout_pm

class MagiesOffensives(Magie):
    """Les magies qui produisent un effet d'attaque"""

class MagieDirigee(Magie) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,direction:Optional[crt.Direction]):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.direction = direction

class MagieCout(Magie, NonRepetable):
    """La classe des magies dont le coût peut varier."""

    def set_cout(self,cout:float):
        """Change le coût de la magie."""
        self.cout = cout
    
class MagieCible(Magie) :
    """La classe des magies qui nécessitent une (ou parfois plusieurs) cible(s)."""

class MultiCible(MagieCible) :
    """La classe des magies qui nécessitent plusieurs cibles."""

class MagieCibleDirigee(MagieCible,MagieDirigee):
    """La classe des magies qui nécessitent une direction et une cible."""

class PorteeLimitee(MagieCible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee_limite:float):
        MagieCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.portee_limite = portee_limite

class CibleAgissant(MagieCible):
    """La classe des magies qui ciblent des agissants."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cible:Agissant):
        MagieCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.cible = cible

class CibleAgissants(MultiCible):
    """La classe des magies qui ciblent plusieurs agissants."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cible:list[Agissant]):
        MultiCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.cible = cible

class CibleItem(MagieCible):
    """La classe des magies qui ciblent des items."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cible:Item):
        MagieCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.cible = cible

class CibleItems(MultiCible):
    """La classe des magies qui ciblent plusieurs items."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cible:list[Item]):
        MultiCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.cible = cible

class CibleCase(MagieCible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cible:crt.Position):
        MagieCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.cible = cible

class CibleCases(MultiCible):
    """La classe des magies qui ciblent plusieurs cases."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,cible:list[crt.Position]):
        MultiCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.cible = cible

# Normalement on en a fini avec les magies ciblées

class Invocation(Magie):
    """La classe des magies qui créent une entitée (un agissant pour se battre à vos côtés, un projectile magique pour attaquer les ennemis, un item à utiliser plus tard..."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Entitee):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.entitee = entitee

    def invoque(self) -> Entitee:
        """Renvoie l'entitée invoquée."""
        return self.entitee

class InvocationProjectile(Invocation,MagieDirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Projectile,direction:Optional[crt.Direction]):
        self.entitee:Projectile
        Invocation.__init__(self,skill,agissant,gain_xp,cout_pm,latence,entitee)
        MagieDirigee.__init__(self,skill,agissant,gain_xp,cout_pm,latence,direction)

    def invoque(self) -> Projectile:
        return self.entitee

class CreationEffet(Magie):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,effet:Effet):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.effet = effet

    def get_effet(self):
        """Renvoie l'effet créé."""
        return self.effet

class Enchante(CreationEffet, MagieCible, NonRepetable):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement):
        CreationEffet.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        MagieCible.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        NonRepetable.__init__(self,agissant,latence)
        self.enchantement = enchantement

    def get_enchantement(self):
        """Renvoie l'enchantement créé."""
        return self.enchantement

class EnchanteItem(Enchante, CibleItem):
    """La classe des magies qui enchantent un item."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:EnchantementItem,item:Item):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        CibleItem.__init__(self,skill,agissant,gain_xp,cout_pm,latence,item)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)

class EnchanteCases(Enchante, CibleCases):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:EnchantementCase,cases:list[crt.Position]):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        CibleCases.__init__(self,skill,agissant,gain_xp,cout_pm,latence,cases)

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            for case in self.cible:
                self.agissant.labyrinthe.get_case(case).effets.add(self.enchantement)

class EnchanteAgissant(Enchante, CibleAgissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:EnchantementAgissant,cible:Agissant):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        CibleAgissant.__init__(self,skill,agissant,gain_xp,cout_pm,latence,cible)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)
