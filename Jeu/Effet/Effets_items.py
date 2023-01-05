from Jeu.Effet.Effet import *
from Jeu.Effet.Attaque.Attaque import *

class En_sursis(One_shot,On_fin_tour):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,item):
        if item.controleur.trouve_agissants_courants(item.get_position()) != []:
            if isinstance(item,(Fragile,Evanescent)):
                item.etat = "brisé"
            else :
                item.arret()

class On_hit(Effet):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee,degats,element = TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self,lanceur,position,controleur):
        positions_touches = controleur.get_pos_touches(position,self.portee)
        for position_touche in positions_touches:
            controleur[position_touche].effets.append(Attaque_case(lanceur,self.degats,self.element,"distance"))

    def execute(self,lanceur,position,controleur):
        self.action(lanceur,position,controleur)

from Jeu.Entitee.Item.Item import Fragile,Evanescent
from Jeu.Constantes import *