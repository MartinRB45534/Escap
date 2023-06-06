from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Entitee.Item.Item import Item
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Effet.Effet import One_shot, On_fin_tour, Effet

# Valeurs par défaut des paramètres
from Old_Jeu.Constantes import TERRE

class En_sursis(One_shot,On_fin_tour):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,item:Item):
        if item.controleur.trouve_agissants_courants(item.get_position()):
            if isinstance(item,(Fragile,Evanescent)):
                item.etat = "brisé"
            else :
                item.arret()

class On_hit(Effet):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee:float,degats:float,element:int = TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self,lanceur:Agissant,position:Position,controleur:Controleur):
        positions_touches = controleur.get_pos_touches(position,self.portee)
        for position_touche in positions_touches:
            controleur.case_from_position(position_touche).effets.append(Attaque_case(lanceur,self.degats,self.element,"distance"))

    def execute(self,lanceur,position,controleur):
        self.action(lanceur,position,controleur)

# Imports utilisés dans le code
from Old_Jeu.Effet.Attaque.Attaque import Attaque_case
from Old_Jeu.Entitee.Item.Projectile.Projectiles import Fragile,Evanescent
from Old_Jeu.Constantes import *