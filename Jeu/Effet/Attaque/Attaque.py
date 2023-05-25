from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Case import Case
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Jeu.Effet.Effet import *

# Valeurs par défaut des paramètres
from Jeu.Constantes import TERRE

class Attaque_magique(Attaque):
    """Une attaque créée par magie."""
    def __init__(self,responsable:Agissant,degats,element=TERRE,distance="proximité",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque.__init__(self,responsable,degats,element,distance,portee,propagation,direction,autre,taux_autre)

    def action(self,controleur:Controleur):
        position = self.responsable.get_position()
        positions_touches = controleur.get_pos_touches(position,self.portee,self.propagation,self.direction,"tout",self.responsable)
        for position_touche in positions_touches:
            controleur.case_from_position(position_touche).effets.append(Attaque_case(self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_decentree(Attaque_magique):
    """Une attaque magique qui affecte une zone plus ou moins éloignée."""
    def __init__(self,position:Position,responsable:Agissant,degats,element=TERRE,distance="distance",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque_magique.__init__(self,responsable,degats,element,distance,portee,propagation,direction,autre,taux_autre)
        self.position = position

    def action(self,controleur:Controleur):
        positions_touches = controleur.get_pos_touches(self.position,self.portee,self.propagation,self.direction,"tout",self.responsable)
        for position_touche in positions_touches:
            controleur.case_from_position(position_touche).effets.append(Attaque_case(self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_delayee(Attaque_magique):
    """Une attaque qui se fera plus tard."""
    def __init__(self,delai,responsable:Agissant,degats,element=TERRE,distance="distance",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque_magique.__init__(self,responsable,degats,element,distance,portee,propagation,direction,autre,taux_autre)
        self.delai = delai

class Attaque_decentree_delayee(Attaque_decentree,Attaque_delayee):
    """Une attaque magique typique : affecte une zone éloignée après un temps de retard."""
    def __init__(self,position:Position,delai,responsable:Agissant,degats,element=TERRE,distance="distance",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque_magique.__init__(self,responsable,degats,element,distance,portee,propagation,direction,autre,taux_autre)
        self.position = position
        self.delai = delai

    def action(self,controleur:Controleur):
        positions_touches = controleur.get_pos_touches(self.position,self.portee,self.propagation,self.direction,"tout",self.responsable)
        for position_touche in positions_touches:
            controleur.case_from_position(position_touche).effets.append(Attaque_case_delayee(self.delai,self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_case(One_shot):
    """L'effet d'attaque dans sa version intermédiaire. Créée par une attaque (version générale), chargé d'attacher une attaque particulière aux agissants de la case, en passant d'abord les défenses de la case. Attachée à la case."""
    def __init__(self,responsable:Agissant,degats:float,element:int=TERRE,distance:str="contact",direction:Optional[Direction] = None,autre:Optional[str]=None,taux_autre:Optional[float]=None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.autre = autre
        self.taux_autre = taux_autre
        self.distance = distance

    def action(self,case:Case):
        victimes_potentielles = case.controleur.trouve_agissants_courants(case.position)
        for victime_potentielle in victimes_potentielles:
            if not victime_potentielle in self.responsable.esprit.get_corps():
                if self.autre is None :
                    victime_potentielle.effets.append(Attaque_particulier(self.responsable,self.degats,self.element,self.distance,self.direction))
                elif self.autre == "piercing":
                    if self.taux_autre is None:
            self.interrompt()
        else:
                        victime_potentielle.effets.append(Attaque_percante(self.responsable,self.degats,self.element,self.distance,self.direction,self.taux_autre))

    def execute(self,case):
        if self.phase == "démarrage":
            self.action(case)
            self.termine()

    def get_skin(self):
        if self.element == TERRE:
            return SKIN_ATTAQUE_TERRE
        elif self.element == FEU:
            return SKIN_ATTAQUE_FEU
        elif self.element == GLACE:
            return SKIN_ATTAQUE_GLACE
        elif self.element == OMBRE:
            return SKIN_ATTAQUE_OMBRE
        else:
            print("Euh, quel est cet élément ?")
            print(self.element)
            return SKIN_VIDE

class Attaque_case_delayee(Attaque_case,Delaye):
    def __init__(self,delai,responsable,degats,element,distance="distance",direction = None,autre=None,taux_autre=None):
        Attaque_case.__init__(self,responsable,degats,element,distance,direction,autre,taux_autre)
        self.affiche = False
        self.delai=delai

    def execute(self,case:Case):
        if self.phase == "démarrage":
            if self.delai > 0:
                self.delai -= 1
            else:
                self.affiche = True
                self.action(case)
                self.termine()

class Attaque_particulier(One_shot):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable,degats,element,distance="contact",direction = None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.distance = distance

    def action(self,victime:Agissant):
        victime.subit(self.responsable,self.degats,self.distance,self.element)

    def get_skin(self):
        return SKIN_BLESSURE

class Attaque_percante(Attaque_particulier): #Attention ! Perçant pour une attaque signifie qu'elle traverse les defenses. C'est totalement différend pour un item !
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version générale), chargé d'infligé les dégats, en passant d'abord les défenses de la case puis celles de l'agissant. Attachée à la victime. En prime, une partie de ses dégats ne sont pas bloquables."""
    def __init__(self,responsable:Agissant,degats:float,element:int,distance:str="contact",direction:Optional[Direction] = None,taux_perce:float = 0):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats * taux_perce
        self.degats_imbloquables = degats - self.degats #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction
        self.distance = distance

    def action(self,victime:Agissant):
        self.degats += self.degats_imbloquables
        victime.subit(self.responsable,self.degats,self.distance,self.element)

    def get_skin(self):
        return SKIN_BLESSURE

class Purification_lumineuse(Attaque):
    """L'effet de purification. Une attaque de 'lumière'."""
    def __init__(self,responsable:Agissant,degats,portee):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.portee = portee

    def action(self,controleur:Controleur):
        position = self.responsable.get_position()
        positions_touches = controleur.get_pos_touches(position,self.portee,"C__S___",None,"tout")
        for position_touche in positions_touches:
            for victime_potentielle in controleur.trouve_agissants_classe_courants(position_touche):
                if not "humain" in victime_potentielle.especes:
                    victime_potentielle.pv -= self.degats * victime_potentielle.get_aff(OMBRE)

# Imports utilisés dans le code
from Jeu.Constantes import *
from Affichage.Skins.Skins import SKIN_BLESSURE, SKIN_ATTAQUE_TERRE, SKIN_ATTAQUE_FEU, SKIN_ATTAQUE_GLACE, SKIN_ATTAQUE_OMBRE, SKIN_VIDE