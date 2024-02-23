"""
Les classes de base des magies.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from ..action import NonRepetable
from ..caste import Caste
from ..action_skill import ActionSkill

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant, Item
    from ...effet import EnchantementAgissant, EnchantementItem
    from ...systeme import Actif

class Magie(Caste,ActionSkill):
    """La classe des magies. Précédemment un effet."""
    gain_xp: float
    def __init__(self,skill:Actif,agissant:Agissant):
        Caste.__init__(self,agissant)
        ActionSkill.__init__(self,agissant,skill)

class MagieDirigee(Magie) :
    """La classe des magies qui nécessitent une direction."""
    direction:crt.Direction|None = None
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)

class MagieCout(Magie, NonRepetable):
    """La classe des magies dont le coût peut varier."""
    def __init__(self,skill:Actif,agissant:Agissant):
        Magie.__init__(self,skill,agissant)
        NonRepetable.__init__(self,agissant)
        self.cout = 0

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
    portee_limite:float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCible.__init__(self,skill,agissant)

class CibleAgissant(MagieCible):
    """La classe des magies qui ciblent des agissants."""
    cible:Agissant|None = None
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCible.__init__(self,skill,agissant)

class CibleAgissants(MultiCible):
    """La classe des magies qui ciblent plusieurs agissants."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MultiCible.__init__(self,skill,agissant)
        self.cible:list[Agissant] = []

class CibleItem(MagieCible):
    """La classe des magies qui ciblent des items."""
    cible:Item|None = None
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCible.__init__(self,skill,agissant)

class CibleItems(MultiCible):
    """La classe des magies qui ciblent plusieurs items."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MultiCible.__init__(self,skill,agissant)
        self.cible:list[Item] = []

class CibleCase(MagieCible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    cible:crt.Position = crt.POSITION_ABSENTE
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCible.__init__(self,skill,agissant)

class CibleCases(MultiCible):
    """La classe des magies qui ciblent plusieurs cases."""
    def __init__(self,skill:Actif,agissant:Agissant):
        MultiCible.__init__(self,skill,agissant)
        self.cible:list[crt.Position] = []

# Normalement on en a fini avec les magies ciblées

class InvocationAgissant(Magie):
    """La classe des magies qui créent un agissant."""
    def __init__(self,skill:Actif,agissant:Agissant,agissant_invoque:Agissant):
        Magie.__init__(self,skill,agissant)
        self.agissant_invoque = agissant_invoque

    def invoque(self) -> Agissant:
        """Renvoie l'agissant invoquée."""
        return self.agissant_invoque

class Enchante(MagieCible, NonRepetable):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    duree: float
    def __init__(self,skill:Actif,agissant:Agissant):
        MagieCible.__init__(self,skill,agissant)
        NonRepetable.__init__(self,agissant)

class EnchanteItem(Enchante, CibleItem):
    """La classe des magies qui enchantent un item."""
    enchantement:EnchantementItem
    def __init__(self,skill:Actif,agissant:Agissant):
        Enchante.__init__(self,skill,agissant)
        CibleItem.__init__(self,skill,agissant)

    def action(self):
        if not self.cible: # NOTHING is falsy
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)

class EnchanteAgissant(Enchante, CibleAgissant):
    """La classe des magies qui enchantent un agissant."""
    enchantement:EnchantementAgissant
    def __init__(self,skill:Actif,agissant:Agissant):
        Enchante.__init__(self,skill,agissant)
        CibleAgissant.__init__(self,skill,agissant)

    def action(self):
        if not self.cible: # NOONE is falsy
            self.interrompt()
        else:
            self.cible.effets.append(self.enchantement)
