from __future__ import annotations
from typing import TYPE_CHECKING, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Jeu.Entitee.Entitee import Entitee_superieure
from Jeu.Entitee.Agissant.PNJ.PNJs import PNJ

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT
from Jeu.Constantes import TERRE

class Humain(PNJ,Entitee_superieure):
    """La classe des pnjs et du joueur. A un comportement un peu plus complexe, et une personnalité."""
    def __init__(self,controleur:Controleur,identite:str,niveau:int,ID:int,position:Position=ABSENT):
        PNJ.__init__(self,controleur,identite,niveau,ID,position)

        self.appreciations:List[float]=[0,0,0,0,0,0,0,0,0,0]
        self.place:int

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_CORPS_HUMAIN
        else:
            return SKIN_CADAVRE

    def subit(self,responsable:Agissant,degats:float,distance="contact",element=TERRE): #L'ID 0 ne correspond à personne
        gravite = degats/self.pv_max
        dangerosite = 0
        if distance == "contact":
            dangerosite = degats*2
        elif distance == "proximité":
            dangerosite = degats
        elif distance == "distance":
            dangerosite = degats*0.2
        if gravite > 1: #Si c'est de l'overkill, ce n'est pas la faute de l'attaquant non plus !
            gravite = 1
        if self.pv <= self.pv_max//3: #Frapper un blessé, ça ne se fait pas !
            gravite += 0.2
        if self.pv <= self.pv_max//9: #Et un mourrant, encore moins !!
            gravite += 0.3
        if element not in self.immunites :
            self.pv -= degats/self.get_aff(element)
        if self.pv <= 0: #Alors tuer les gens, je ne vous en parle pas !!!
            gravite += 0.5
            print(f"{self.identite} a été tué par :")
            print(degats,element)
            print(responsable.ID)
            print(responsable)
            self.effets_mortuaires = self.effets
            self.effets_mortuaires_tueur = responsable.effets
            self.controleur.pause = True
        self.insurge(responsable,gravite,dangerosite)

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_CORPS_HUMAIN, SKIN_CADAVRE