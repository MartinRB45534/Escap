"""Contient les classes de murs vus par le joueur."""

from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import affichage as af
import carte as crt

from ....labyrinthe import Mur, MurPlein, MurOuvert, Porte, Barriere, Teleporteur, PorteALoquet, Escalier

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Entitee

class MurVu(crt.Mur):
    """Un mur vu par le joueur."""
    def __init__(self,niveau:int):
        super().__init__()
        self.niveau = niveau

class MurImpassableVu(MurVu):
    """Un mur qui ne peut pas être traversé."""
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.ferme = True

class MurPleinVu(MurVu):
    """Un mur ferme"""
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.casse = False

class PorteVue(MurPleinVu):
    """Une porte qui peut être ouverte avec une clé"""
    def __init__(self,niveau:int,code:str):
        super().__init__(niveau)
        self.code = code
        self.ouvert = False
        self.casse = False

class MurOuvertVu(MurVu):
    """Un mur qui peut être ouvert ou fermé"""

class BarriereVue(MurOuvertVu):
    """Une barrière qui peut s'ouvrir sous certaines conditions"""
    def __init__(self,niveau:int,condition:Callable[[Entitee],bool]):
        super().__init__(niveau)
        self.condition = condition

class TeleporteurVu(MurOuvertVu): # La seule différence avec un mur ouvert est que les téléporteurs sont affichés différemment
    """Un téléporteur sans notion de haut et de bas"""

# Quelques murs pas symétriques
class PorteALoquetVue(PorteVue):
    """Une porte qui peut s'ouvrir sans clé de l'autre côté"""

class EscalierVu(MurOuvertVu):
    """Un téléporteur avec une notion graphique de haut et de bas"""
    def __init__(self, niveau: int, direction: af.DirectionAff):
        super().__init__(niveau)
        self.direction = direction

def voit_mur(mur:Mur) -> MurVu:
    """Transforme un mur en mur vu."""
    if isinstance(mur,Escalier):
        return EscalierVu(mur.niveau,mur.direction)
    elif isinstance(mur,PorteALoquet) and mur.loquet:
        return PorteALoquetVue(mur.niveau,mur.code)
    elif isinstance(mur,Porte):
        return PorteVue(mur.niveau,mur.code)
    elif isinstance(mur,Barriere):
        return BarriereVue(mur.niveau,mur.condition)
    elif isinstance(mur,Teleporteur):
        return TeleporteurVu(mur.niveau)
    elif isinstance(mur,MurPlein):
        return MurPleinVu(mur.niveau)
    elif isinstance(mur,MurOuvert):
        return MurOuvertVu(mur.niveau)
    else:
        raise TypeError(f"Le type {type(mur)} n'est pas reconnu comme un mur.")
