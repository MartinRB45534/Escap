from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.item.item import Item
    from ...systeme.elements import Element

# Imports des classes parentes
from ...effet import OneShot, Effet

# Imports des valeurs par défaut des paramètres
from ...systeme.elements import Element

class EffetItem(Effet):
    """Effet qui est placé sur un item."""
    def __init__(self, item:Item):
        self.item = item

class Sursis(OneShot,EffetItem):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def action(self):
        if self.item.labyrinthe.position_case[self.item.position].agissant is not None:
            if isinstance(self.item,(Fragile,Evanescent)):
                self.item.etat = EtatsItems.BRISE
            else :
                self.item.arret()

class OnHit(EffetItem):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee:float,degats:float,element:Element=Element.TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self):
        zone = self.item.labyrinthe.a_portee(self.item.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone:
            self.item.labyrinthe.get_case(position).effets.add(AttaqueCase(self.item.lanceur or NOONE,self.degats,self.element,"distance"))

# Imports utilisés dans le code
from ..attaque.attaque import AttaqueCase
from ...entitee.item.projectile.projectiles import Fragile,Evanescent
from ...entitee.item.etats import EtatsItems
from ...entitee.agissant.agissant import NOONE
from ...labyrinthe.deplacement import Deplacement
from ...labyrinthe.passage import Passage
from ...labyrinthe.forme import Forme
