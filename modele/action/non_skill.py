from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .action import ActionFinal, NonRepetable
from .caste import Caste, CasteContinu, CasteFinal, CasteInitial, CasteFractionnaire
from ..effet import EffetMixte

# Imports utilisés dans le code
from ..commons import EtatsItems, Deplacement, Forme, Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee import Agissant, Potion, Parchemin
    from ..effet import EffetAgissant
    from .magie import Magie

class Boit(ActionFinal, NonRepetable):
    """
    L'action de boire une potion.
    """
    type_effet: type[EffetAgissant]
    def __init__(self, agissant: Agissant, item: Potion):
        ActionFinal.__init__(self, agissant)
        NonRepetable.__init__(self, agissant)
        self.item = item
        self.effet = self.type_effet()
        self.item.etat = EtatsItems.UTILISE

    def action(self):
        self.agissant.effets.add(self.effet)
        self.item.etat = EtatsItems.BRISE

    def interrompt(self):
        self.item.etat = EtatsItems.INTACT

    @classmethod
    def eclabousse(cls, item: Potion):
        """La potion a été lancée et se brise."""
        case = item.labyrinthe.get_case(item.position)
        if case.agissant is not None:
            case.agissant.effets.add(cls.type_effet())
        elif issubclass(cls.type_effet, EffetMixte):
            cases = item.labyrinthe.a_portee(item.position, cls.type_effet.portee, Deplacement.SPATIAL, Forme.CERCLE, Passage(False, False, False, False, False))
            for position in cases:
                effet = cls.type_effet()
                effet.on_case = True
                item.labyrinthe.get_case(position).effets.add(effet)

class Lit(Caste, NonRepetable):
    """
    L'action de caster un parchemin.
    """
    def __init__(self, agissant: Agissant, item: Parchemin):
        Caste.__init__(self, agissant)
        NonRepetable.__init__(self, agissant)
        self.item = item
        self.mana = 0

    def get_skin(self):
        pass

class LitEffet(Lit, NonRepetable):
    """
    L'action de caster un parchemin qui place un effet.
    """
    def __init__(self, agissant: Agissant, item: Parchemin):
        Lit.__init__(self, agissant, item)
        NonRepetable.__init__(self, agissant)

class LitEffetFinal(LitEffet, CasteFinal):
    """Un parchemin qui place un effet, en caste final."""
    def __init__(self, agissant: Agissant, item: Parchemin, latence: float, effet: EffetAgissant):
        LitEffet.__init__(self, agissant, item)
        CasteFinal.__init__(self, agissant)
        self.latence_max = latence
        self.effet = effet

class LitEffetInitial(LitEffet, CasteInitial):
    """Un parchemin qui place un effet, en caste initial."""
    def __init__(self, agissant: Agissant, item: Parchemin, latence: float, effet: EffetAgissant):
        LitEffet.__init__(self,agissant,item)
        CasteInitial.__init__(self,agissant)
        self.latence_max = latence
        self.effet = effet

class LitEffetContinu(LitEffet, CasteContinu):
    """Un parchemin qui place un effet, en caste continu."""
    def __init__(self, agissant: Agissant, item: Parchemin, latence: float, effet: EffetAgissant):
        LitEffet.__init__(self, agissant, item)
        CasteContinu.__init__(self, agissant)
        self.latence_max = latence
        self.effet = effet

class LitEffetFractionnaire(LitEffet, CasteFractionnaire):
    """Un parchemin qui place un effet, en caste fractionnaire."""
    def __init__(self, agissant: Agissant, item: Parchemin, latence: float, effet: EffetAgissant,
                 parts: int):
        LitEffet.__init__(self,agissant,item)
        CasteFractionnaire.__init__(self,agissant)
        self.latence_max = latence
        self.parts = parts
        self.effet = effet

class Impregne(Lit, ActionFinal, CasteFinal):
    """
    L'action d'imprégner une magie sur un parchemin.
    """
    taux_cout_impregne: float
    taux_cout_caste: float
    taux_latence_impregne: float
    taux_latence_caste: float
    def __init__(self, agissant: Agissant, item: Parchemin):
        Lit.__init__(self, agissant, item)
        ActionFinal.__init__(self, agissant)
        CasteFinal.__init__(self, agissant)
        self.magie: Magie|None = None

    def action(self):
        """L'action est terminée."""
        if self.magie is not None:
            self.item.action_portee = self.magie # Le parchemin est imprégné de la magie
            self.item.impregne = None
            self.item.etat = EtatsItems.INTACT
        else:
            self.interrompt()

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = EtatsItems.INTACT
        self.magie = None

    def set_magie(self, magie: Magie):
        """Définit la magie à imprégner."""
        self.magie = magie
        self.cout = magie.cout * self.taux_cout_impregne
        self.latence = magie.latence * self.taux_latence_impregne
        self.magie.cout *= self.taux_cout_caste
        self.magie.latence *= self.taux_latence_caste
