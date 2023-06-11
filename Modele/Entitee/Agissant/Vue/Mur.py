from __future__ import annotations
from typing import TYPE_CHECKING, Type, Callable
import Affichage as af
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee import Entitee

class Mur_vu(crt.Mur):
    def __init__(self,niveau:int):
        self.niveau = niveau
        self.ferme = False

class Mur_impassable_vu(Mur_vu):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.ferme = True

class Mur_plein_vu(Mur_vu):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.casse = False

class Porte_vue(Mur_plein_vu):
    def __init__(self,niveau:int,code:str):
        super().__init__(niveau)
        self.code = code
        self.ouvert = False
        self.casse = False

class Mur_ouvert_vu(Mur_vu):
    def __init__(self,niveau:int):
        super().__init__(niveau)

class Barriere_vue(Mur_ouvert_vu):
    def __init__(self,niveau:int,condition:Callable[[Entitee],bool]):
        super().__init__(niveau)
        self.condition = condition

class Teleporteur_vu(Mur_ouvert_vu): # La seule différence avec un mur ouvert est que les téléporteurs sont affichés différemment
    def __init__(self,niveau:int):
        super().__init__(niveau)

# Quelques murs pas symétriques
class Porte_a_loquet_vue(Porte_vue):
    """Une porte qui peut s'ouvrir sans clé de l'autre côté"""
    def __init__(self, niveau: int, code: str):
        super().__init__(niveau, code)

class Escalier_vu(Mur_ouvert_vu):
    """Un téléporteur avec une notion graphique de haut et de bas"""
    def __init__(self, niveau: int, direction: af.Direction_aff):
        super().__init__(niveau)
        self.direction = direction

def voit_mur(mur:Mur) -> Mur_vu:
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
    elif isinstance(mur,Mur_plein):
        return Mur_plein_vu(mur.niveau)
    elif isinstance(mur,Mur_ouvert):
        return Mur_ouvert_vu(mur.niveau)
    else:
        raise TypeError(f"Le type {type(mur)} n'est pas reconnu comme un mur.")


from ....Labyrinthe.Mur import Mur, Mur_plein, Mur_ouvert, Porte, Barriere, Teleporteur, Mur_asymétrique, Porte_a_loquet, Escalier