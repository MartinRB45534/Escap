from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import affichage as af
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Entitee

class MurVu(crt.Mur):
    def __init__(self,niveau:int):
        self.niveau = niveau
        self.ferme = False

class MurImpassable_vu(MurVu):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.ferme = True

class MurPlein_vu(MurVu):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.casse = False

class Porte_vue(MurPlein_vu):
    def __init__(self,niveau:int,code:str):
        super().__init__(niveau)
        self.code = code
        self.ouvert = False
        self.casse = False

class MurOuvert_vu(MurVu):
    def __init__(self,niveau:int):
        super().__init__(niveau)

class Barriere_vue(MurOuvert_vu):
    def __init__(self,niveau:int,condition:Callable[[Entitee],bool]):
        super().__init__(niveau)
        self.condition = condition

class Teleporteur_vu(MurOuvert_vu): # La seule différence avec un mur ouvert est que les téléporteurs sont affichés différemment
    def __init__(self,niveau:int):
        super().__init__(niveau)

# Quelques murs pas symétriques
class Porte_a_loquet_vue(Porte_vue):
    """Une porte qui peut s'ouvrir sans clé de l'autre côté"""
    def __init__(self, niveau: int, code: str):
        super().__init__(niveau, code)

class Escalier_vu(MurOuvert_vu):
    """Un téléporteur avec une notion graphique de haut et de bas"""
    def __init__(self, niveau: int, direction: af.DirectionAff):
        super().__init__(niveau)
        self.direction = direction

def voit_mur(mur:Mur) -> MurVu:
    if isinstance(mur,Escalier):
        return Escalier_vu(mur.niveau,mur.direction)
    elif isinstance(mur,Porte_a_loquet) and mur.loquet:
        return Porte_a_loquet_vue(mur.niveau,mur.code)
    elif isinstance(mur,Porte):
        return Porte_vue(mur.niveau,mur.code)
    elif isinstance(mur,Barriere):
        return Barriere_vue(mur.niveau,mur.condition)
    elif isinstance(mur,Teleporteur):
        return Teleporteur_vu(mur.niveau)
    elif isinstance(mur,MurPlein):
        return MurPlein_vu(mur.niveau)
    elif isinstance(mur,MurOuvert):
        return MurOuvert_vu(mur.niveau)
    else:
        raise TypeError(f"Le type {type(mur)} n'est pas reconnu comme un mur.")


from ....labyrinthe.mur import Mur, MurPlein, MurOuvert, Porte, Barriere, Teleporteur, Porte_a_loquet, Escalier