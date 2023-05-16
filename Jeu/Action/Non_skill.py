from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Item import Consommable
    from Jeu.Entitee.Item.Potion.Potion import Potion
    from Jeu.Entitee.Item.Parchemin.Parchemin import Parchemin

# Imports des classes parentes
from Jeu.Action.Action import Action
from Jeu.Action.Caste import Caste_continu

class Vole(Action):
    """
    L'action des items qui volent.
    """
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

class Consomme(Action):
    """
    L'action d'utilisation d'un consommable (potion ou parchemin).
    """
    def __init__(self,agissant:Agissant,latence:float,item:Consommable):
        super().__init__(agissant,latence)
        self.item = item
        self.item.etat = "utilise"

    def termine(self):
        """L'action est terminée."""
        self.item.utilise(self.agissant)

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = "intact"

class Boit(Consomme):
    """
    L'action de boire une potion.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Potion):
        super().__init__(agissant,latence,item)
        
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

class Caste_parchemin(Consomme,Caste_continu):
    """
    L'action de caster un parchemin.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin):
        super().__init__(agissant,latence,item)
        self.mana = 0
        self.cout = item.cout
        
    def get_skin(self):
        pass