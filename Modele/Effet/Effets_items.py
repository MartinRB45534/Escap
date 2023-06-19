from __future__ import annotations
from typing import TYPE_CHECKING
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Item import Item
    from ..Systeme.Elements import Element

# Imports des classes parentes
from ..Effet.Effet import One_shot, On_fin_tour, Effet

# Imports des valeurs par défaut des paramètres
from ..Systeme.Elements import Element

class En_sursis(One_shot,On_fin_tour):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,item:Item):
        if item.labyrinthe.position_case[item.position].agissant is not None:
            if isinstance(item,(Fragile,Evanescent)):
                item.etat = Etats_items.BRISE
            else :
                item.arret()

class On_hit(Effet):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee:float,degats:float,element:Element=Element.TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self,item:Item):
        zone = item.labyrinthe.a_portee(item.position,self.portee,Deplacement.SPATIAL,Forme.CERCLE,Passage(False,False,False,True,False))
        for position in zone.nodes:
            item.labyrinthe.get_case(position).effets.add(Attaque_case(item.lanceur or NOONE,self.degats,self.element,"distance"))

    def execute(self,item:Item):
        self.action(item)

# Imports utilisés dans le code
from ..Effet.Attaque.Attaque import Attaque_case
from ..Entitee.Item.Projectile.Projectiles import Fragile,Evanescent
from ..Entitee.Item.Etats import Etats_items
from ..Entitee.Agissant.Agissant import NOONE
from ..Labyrinthe.Deplacement import Deplacement
from ..Labyrinthe.Passage import Passage
from ..Labyrinthe.Forme import Forme