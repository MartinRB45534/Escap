from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports des classes parentes
from .action import ActionFinal, NonRepetable
from .caste import Caste, CasteContinu, CasteFinal, CasteInitial, CasteFractionnaire

# Imports utilisés dans le code
from ..commons import EtatsItems

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.item import Consommable
    from ..entitee.item.potion.potion import Potion
    from ..entitee.item.parchemin.parchemin import Parchemin
    from ..entitee.item.parchemin.parchemins import ParcheminVierge
    from ..effet import Effet
    from .magie.magie import Magie

class PlaceEffet(ActionFinal, NonRepetable):
    """
    L'action d'utilisation d'un consommable (potion ou parchemin) lorsque celui-ci se contente de placer un effet.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Consommable,effet:Effet):
        super().__init__(agissant,latence)
        self.item = item
        self.item.etat = EtatsItems.UTILISE
        self.effet = effet

    def action(self):
        self.agissant.effets.append(self.effet)
        self.item.etat = EtatsItems.BRISE

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = EtatsItems.BRISE

class Boit(PlaceEffet):
    """
    L'action de boire une potion.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Potion,effet:Effet):
        PlaceEffet.__init__(self,agissant,latence,item,effet)

class Lit(Caste, NonRepetable):
    """
    L'action de caster un parchemin.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin):
        Caste.__init__(self,agissant,latence)
        NonRepetable.__init__(self,agissant,latence)
        self.item = item
        self.mana = 0

    def get_skin(self):
        pass

class LitEffet(Lit,PlaceEffet):
    """
    L'action de caster un parchemin qui place un effet.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin,effet:Effet):
        Lit.__init__(self,agissant,latence,item)
        PlaceEffet.__init__(self,agissant,latence,item,effet)

class LitEffetFinal(LitEffet,CasteFinal):
    """Un parchemin qui place un effet, en caste final."""

class LitEffetInitial(LitEffet,CasteInitial):
    """Un parchemin qui place un effet, en caste initial."""

class LitEffetContinu(LitEffet,CasteContinu):
    """Un parchemin qui place un effet, en caste continu."""

class LitEffetFractionnaire(LitEffet,CasteFractionnaire):
    """Un parchemin qui place un effet, en caste fractionnaire."""

class Impregne(Lit,ActionFinal,CasteFinal):
    """
    L'action d'imprégner une magie sur un parchemin.
    """
    def __init__(self,agissant:Agissant,latence:float,item:ParcheminVierge,taux_cout_impregne:float,taux_cout_caste:float,taux_latence_impregne:float,taux_latence_caste:float):
        Lit.__init__(self,agissant,latence,item)
        ActionFinal.__init__(self,agissant,latence)
        CasteFinal.__init__(self,agissant,latence)
        self.item:ParcheminVierge
        self.taux_cout_impregne = taux_cout_impregne
        self.taux_cout_caste = taux_cout_caste
        self.taux_latence_impregne = taux_latence_impregne
        self.taux_latence_caste = taux_latence_caste
        self.magie:Optional[Magie] = None

    def action(self):
        """L'action est terminée."""
        if self.magie is not None:
            self.item.action_portee = self.magie # Le parchemin est imprégné de la magie
            self.item.etat = EtatsItems.INTACT
        else:
            self.interrompt()

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = EtatsItems.INTACT
        self.magie = None

    def set_magie(self,magie:Magie):
        """Définit la magie à imprégner."""
        self.magie = magie
        self.cout = magie.cout*self.taux_cout_impregne
        self.latence = magie.latence*self.taux_latence_impregne
        self.magie.cout*=self.taux_cout_caste
        self.magie.latence*=self.taux_latence_caste
