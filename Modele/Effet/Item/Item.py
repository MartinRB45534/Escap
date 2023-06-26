from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Item.Item import Item
    from ...Systeme.Elements import Element

# Imports des classes parentes
from ...Effet import One_shot, Effet

# Imports des valeurs par défaut des paramètres
from ...Systeme.Elements import Element

class Effet_item(Effet):
    """Effet qui est placé sur un item."""
    def __init__(self, item:Item):
        self.item = item

class Sursis(One_shot,Effet_item):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def action(self):
        if self.item.labyrinthe.position_case[self.item.position].agissant is not None:
            if isinstance(self.item,(Fragile,Evanescent)):
                self.item.etat = Etats_items.BRISE
            else :
                self.item.arret()

class On_hit(Effet_item):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee:float,degats:float,element:Element=Element.TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self):
        zone = self.item.labyrinthe.a_portee(self.item.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone:
            self.item.labyrinthe.get_case(position).effets.add(Attaque_case(self.item.lanceur or NOONE,self.degats,self.element,"distance"))

# Imports utilisés dans le code
from ..Attaque.Attaque import Attaque_case
from ...Entitee.Item.Projectile.Projectiles import Fragile,Evanescent
from ...Entitee.Item.Etats import Etats_items
from ...Entitee.Agissant.Agissant import NOONE
from ...Labyrinthe.Deplacement import Deplacement
from ...Labyrinthe.Passage import Passage
from ...Labyrinthe.Forme import Forme