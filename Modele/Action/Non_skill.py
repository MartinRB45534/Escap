from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Entitee.Item.Item import Consommable
    from Old_Jeu.Entitee.Item.Potion.Potion import Potion
    from Old_Jeu.Entitee.Item.Parchemin.Parchemin import Parchemin
    from Old_Jeu.Entitee.Item.Parchemin.Parchemins import Parchemin_vierge
    from Old_Jeu.Effet.Effet import Effet
    from Old_Jeu.Action.Magie.Magie import Magie

# Imports des classes parentes
from Old_Jeu.Action.Action import Action_final, Non_repetable
from Old_Jeu.Action.Caste import Caste, Caste_continu, Caste_final, Caste_initial, Caste_fractionnaire

class Place_effet(Action_final, Non_repetable):
    """
    L'action d'utilisation d'un consommable (potion ou parchemin) lorsque celui-ci se contente de placer un effet.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Consommable,effet:Effet):
        super().__init__(agissant,latence)
        self.item = item
        self.item.etat = "utilise"
        self.effet = effet

    def action(self):
        self.agissant.effets.append(self.effet)
        self.item.etat = "brisé"

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = "intact"

class Boit(Place_effet):
    """
    L'action de boire une potion.
    """
    def __init__(self,agissant:Agissant,latence:float,item:Potion,effet:Effet):
        super().__init__(agissant,latence,item,effet)
        
    def get_skin(self):
        pass
        # TODO: Ajouter le get_skin

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
    def __init__(self,agissant:Agissant,latence:float,item:Parchemin_vierge):
        Lit.__init__(self,agissant,latence,item)
        self.item:Parchemin_vierge
        self.taux_cout_impregne = 0.5
        self.taux_cout_caste = 0.5
        self.taux_latence_impregne = 0.1
        self.taux_latence_caste = 0.9
        self.magie:Optional[Magie] = None

    def action(self):
        """L'action est terminée."""
        if self.magie is not None:
            self.item.action_portee = self.magie # Le parchemin est imprégné de la magie
            self.item.etat = "intact"
        else:
            self.interrompt()

    def interrompt(self):
        """L'action est interrompue."""
        self.item.etat = "intact"
        self.magie = None

    def set_magie(self,magie:Magie):
        """Définit la magie à imprégner."""
        self.magie = magie
        self.cout = magie.cout*self.taux_cout_impregne
        self.latence = magie.latence*self.taux_latence_impregne
        self.magie.cout*=self.taux_cout_caste
        self.magie.latence*=self.taux_latence_caste