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
    from ...entitee import Entitee, Agissant, Projectile, Item
    from ...effet import Effet, Enchantement, EnchantementAgissant, EnchantementCase, EnchantementItem
    from ...systeme import Actif, Magie

class ActionMagie(Caste,ActionSkill):
    """La classe des magies. Précédemment un effet."""
    nom = "magie" # Vraiment utile ?
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float): #Toutes ces caractéristiques sont déterminées par la sous-classe au moment de l'instanciation, en fonction de la magie utilisée et du niveau.
        Caste.__init__(self,agissant,latence)
        ActionSkill.__init__(self,agissant,latence,skill,gain_xp)
        self.magie = magie
        self.gain_xp = gain_xp
        self.cout = cout_pm

class ActionMagiesOffensives(ActionMagie):
    """Les magies qui produisent un effet d'attaque"""

class ActionMagieDirigee(ActionMagie) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,direction:Optional[crt.Direction]):
        ActionMagie.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.direction = direction

class ActionMagieCout(ActionMagie, NonRepetable):
    """La classe des magies dont le coût peut varier."""

    def set_cout(self,cout:float):
        """Change le coût de la magie."""
        self.cout = cout
    
class ActionMagieCible(ActionMagie) :
    """La classe des magies qui nécessitent une (ou parfois plusieurs) cible(s)."""

class MultiCible(ActionMagieCible) :
    """La classe des magies qui nécessitent plusieurs cibles."""

class ActionMagieCibleDirigee(ActionMagieCible,ActionMagieDirigee):
    """La classe des magies qui nécessitent une direction et une cible."""

class PorteeLimitee(ActionMagieCible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,portee_limite:float):
        ActionMagieCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.portee_limite = portee_limite

class CibleAgissant(ActionMagieCible):
    """La classe des magies qui ciblent des agissants."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        ActionMagieCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.cible:Agissant|None = None

class CibleAgissants(MultiCible):
    """La classe des magies qui ciblent plusieurs agissants."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        MultiCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.cible:list[Agissant] = []

class CibleItem(ActionMagieCible):
    """La classe des magies qui ciblent des items."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        ActionMagieCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.cible:Item|None = None

class CibleItems(MultiCible):
    """La classe des magies qui ciblent plusieurs items."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        MultiCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.cible:list[Item] = []

class CibleCase(ActionMagieCible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        ActionMagieCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.cible:crt.Position = crt.POSITION_ABSENTE

class CibleCases(MultiCible):
    """La classe des magies qui ciblent plusieurs cases."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float):
        MultiCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.cible:list[crt.Position] = []

# Normalement on en a fini avec les magies ciblées

class Invocation(ActionMagie):
    """La classe des magies qui créent une entitée (un agissant pour se battre à vos côtés, un projectile magique pour attaquer les ennemis, un item à utiliser plus tard..."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Entitee):
        ActionMagie.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.entitee = entitee

    def invoque(self) -> Entitee:
        """Renvoie l'entitée invoquée."""
        return self.entitee

class InvocationProjectile(Invocation,ActionMagieDirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Projectile,direction:Optional[crt.Direction]):
        self.entitee:Projectile
        Invocation.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,entitee)
        ActionMagieDirigee.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,direction)

    def invoque(self) -> Projectile:
        return self.entitee

class CreationEffet(ActionMagie):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,effet:Effet):
        ActionMagie.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        self.effet = effet

    def get_effet(self):
        """Renvoie l'effet créé."""
        return self.effet

class Enchante(CreationEffet, ActionMagieCible, NonRepetable):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement):
        CreationEffet.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,enchantement)
        ActionMagieCible.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)
        NonRepetable.__init__(self,agissant,latence)
        self.enchantement = enchantement

    def get_enchantement(self):
        """Renvoie l'enchantement créé."""
        return self.enchantement

class EnchanteItem(Enchante, CibleItem):
    """La classe des magies qui enchantent un item."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:EnchantementItem):
        Enchante.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,enchantement)
        CibleItem.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)

class EnchanteCases(Enchante, CibleCases):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:EnchantementCase):
        Enchante.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,enchantement)
        CibleCases.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        if not self.cible: # [] is falsy
            self.interrompt()
        else:
            for case in self.cible:
                self.agissant.labyrinthe.get_case(case).effets.add(self.enchantement)

class EnchanteAgissant(Enchante, CibleAgissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,skill:Actif,magie:Magie,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:EnchantementAgissant):
        Enchante.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence,enchantement)
        CibleAgissant.__init__(self,skill,magie,agissant,gain_xp,cout_pm,latence)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)
