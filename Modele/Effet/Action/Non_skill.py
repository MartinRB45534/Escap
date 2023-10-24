from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...entitee.item.item import Consommable
    from ...entitee.item.Potion.Potion import Potion
    from ...entitee.item.Parchemin.Parchemin import Parchemin
    from ...entitee.item.Parchemin.Parchemins import Parchemin_vierge
    from ..effet import Effet
    from .magie.magie import Magie

# Imports des classes parentes
from .action import Action_final, Non_repetable
from .caste import Caste, Caste_continu, Caste_final, Caste_initial, Caste_fractionnaire

class Place_effet(Action_final, Non_repetable):
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

class Boit(Place_effet):
    """
    L'action de boire une potion.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Potion,effet:Effet):
        super().__init__(agissant,latence,item,effet)

class Lit(Caste, Non_repetable):
    """
    L'action de caster un parchemin.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin):
        super().__init__(agissant,latence)
        self.item = item
        self.mana = 0
        self.cout = item.cout
        
    def get_skin(self):
        pass

class Lit_effet(Lit,Place_effet):
    """
    L'action de caster un parchemin qui place un effet.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin,effet:Effet):
        super().__init__(agissant,latence,item)
        self.effet = effet

class Lit_effet_final(Lit_effet,Caste_final):
    pass

class Lit_effet_initial(Lit_effet,Caste_initial):
    pass

class Lit_effet_continu(Lit_effet,Caste_continu):
    pass

class Lit_effet_fractionnaire(Lit_effet,Caste_fractionnaire):
    pass

class Impregne(Lit,Action_final,Caste_final):
    """
    L'action d'imprégner une magie sur un parchemin.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin_vierge,taux_cout_impregne:float,taux_cout_caste:float,taux_latence_impregne:float,taux_latence_caste:float):
        Lit.__init__(self,agissant,latence,item)
        self.item:Parchemin_vierge
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

from ...entitee.item.etats import EtatsItems