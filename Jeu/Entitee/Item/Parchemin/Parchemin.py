from __future__ import annotations
from typing import Type, TYPE_CHECKING
if TYPE_CHECKING:
    from Jeu.Effet.Magie.Magie import Magie

from Jeu.Entitee.Item.Item import *
from Jeu.Effet.Effets_divers import Enseignement

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,position:Optional[Position]=None,effet:Effet,cout:float):
        Item.__init__(self,position)
        self.effet = effet
        self.cout = cout

    def get_titre(self,observation=0):
        return "Parchemin"

    def get_description(self,observation=0):
        return ["Un parchemin","C'est quoi ces gribouillis ?"]

    def utilise(self,agissant:Agissant):
        if agissant.peut_payer(self.cout) :
            agissant.paye(self.cout)
            agissant.ajoute_effet(self.effet)
            self.etat = "brisé"

    def get_classe(self):
        return Parchemin

    def get_skin(self):
        return SKIN_PARCHEMIN

    def get_image():
        return SKIN_PARCHEMIN

class Poly_de_cours(Parchemin):
    """Un parchemin qui enseigne une magie."""
    def __init__(self,position:Optional[Position]=None,magie:Type[Magie],cout:float):
        Parchemin.__init__(self,position,Enseignement(magie),cout)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Probablement perdu par un élève.","D'après les tâches de sang, il fuyait un monstre."]
