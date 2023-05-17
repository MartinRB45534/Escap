from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Item import Consommable
    from Jeu.Entitee.Item.Potion.Potion import Potion
    from Jeu.Entitee.Item.Parchemin.Parchemin import Parchemin
    from Jeu.Effet.Effet import Effet
    from Jeu.Action.Magie.Magie import Magie

# Imports des classes parentes
from Jeu.Action.Action import Action
from Jeu.Action.Caste import Caste, Caste_continu, Caste_final, Caste_initial, Caste_fractionnaire

class Vole(Action):
    """
    L'action des items qui volent.
    """
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

class Consomme(Action):
    """
    L'action d'utilisation d'un consommable (potion ou parchemin) lorsque celui-ci se contente de placer un effet.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Consommable,effet:Effet):
        super().__init__(agissant,latence)
        self.item = item
        self.item.etat = "utilise"
        self.effet = effet

    def termine(self):
        """L'action est terminée."""
        self.agissant.effets.append(self.effet)
        self.item.etat = "brisé"

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = "intact"

class Boit(Consomme):
    """
    L'action de boire une potion.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Potion,effet:Effet):
        super().__init__(agissant,latence,item,effet)
        
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

class Lit(Caste):
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

class Lit_effet(Lit,Consomme):
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

class Impregne(Lit):
    """
    L'action d'imprégner une magie sur un parchemin.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin):
        super().__init__(agissant,latence,item)
        self.taux_cout_impregne = 0.5
        self.taux_cout_caste = 0.5
        self.taux_latence_impregne = 0.1
        self.taux_latence_caste = 0.9
        self.magie:Optional[Magie] = None

    def termine(self):
        """L'action est terminée."""
        if self.magie is not None:
            self.item.action = self.magie # Le parchemin est imprégné de la magie
            self.item.etat = "intact"
        else:
            self.interrompt()