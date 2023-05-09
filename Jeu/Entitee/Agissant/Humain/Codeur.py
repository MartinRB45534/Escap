from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Controleur import Controleur

from Jeu.Entitee.Agissant.Humain.Humain import *

class Codeur(Humain): #Le cinquième humain du jeu, à l'étage 4 (répond au nom de Dev, quand Il n'est pas occupé à programmer un autre jeu)
    """Ma classe."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'codeur'
        self.place = 4

        Humain.__init__(self,controleur,position,self.identite,1,1) #La notion de niveau n'a pas d'emprise sur Dev... Il peut modifier son niveau simple 'self.niveau = '

        self.appreciations = [5,0,0,0,0,0,0,0,0,0]

    def fuite(self,degats:float=0):
        return False

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef (c'est la seule option pour parler à Dev dans le tuto)
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
        elif self.dialogue == -2: #Le joueur nous a dit qu'il s'était perdu
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1","dialogue-2reponse1.2"]
        elif self.dialogue == -3: #Le joueur ne s'intéresse qu'aux combats
            self.replique = "dialogue-3phrase1"
            self.repliques = ["dialogue-3reponse1.1"]
        elif self.dialogue == -4: #Le joueur est revenu mentir
            self.replique = "dialogue-4phrase1"
            self.repliques = ["dialogue-4reponse1.1"]
        elif self.dialogue == -5: #Le joueur a écouté nos conseils
            self.replique = "dialogue-5phrase1"
            self.repliques = ["dialogue-5reponse1.1","dialogue-5reponse1.2"]

    def interprete(self,replique:str):

        #Premier dialogue
        #Le joueur arrive vers Dev
        if replique == "dialogue-1reponse1.1":
            self.replique="dialogue-1phrase1.1"
            self.repliques = ["dialogue-1reponse1.1.1"]
        elif replique == "dialogue-1reponse1.1.1":
            self.end_dialogue(-2)
        elif replique == "dialogue-1reponse1.2":
            self.replique="dialogue-1phrase1.2"
            self.repliques = ["dialogue-1reponse1.2.1","dialogue-1reponse1.2.2"]
        elif replique == "dialogue-1reponse1.2.1":
            self.replique="dialogue-1phrase1.2.1"
            self.repliques = ["dialogue-1reponse1.2.1.1"]
        elif replique == "dialogue-1reponse1.2.1.1":
            self.end_dialogue(-3)
        elif replique == "dialogue-1reponse1.2.2":
            self.replique="dialogue-1phrase1.2.2"
            self.repliques = ["dialogue-1reponse1.2.2.1"]
        elif replique == "dialogue-1reponse1.2.2.1":
            self.appreciations[0] += 0.5
            self.end_dialogue(-5)

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.replique="dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.1.1":
            self.end_dialogue(-2)
        elif replique == "dialogue-2reponse1.2":
            self.replique="dialogue-2phrase1.2"
            self.repliques = ["dialogue-2reponse1.2.1"]
        elif replique == "dialogue-2reponse1.2.1":
            self.replique="dialogue-2phrase1.2.1"
            self.repliques = ["dialogue-2reponse1.2.1.1"]
        elif replique == "dialogue-2reponse1.2.1.1":
            self.replique="dialogue-2phrase1.2.1.1"
            self.repliques = ["dialogue-2reponse1.2.1.1.1"]
        elif replique == "dialogue-2reponse1.2.1.1.1":
            self.end_dialogue(-4)

        #Dialogue par défaut -3
        elif replique == "dialogue-3reponse1.1":
            self.end_dialogue(-3)

        #Dialogue par défaut -4
        elif replique == "dialogue-4reponse1.1":
            self.end_dialogue(-4)

        #Dialogue par défaut -5
        elif replique == "dialogue-5reponse1.2":
            self.replique="dialogue-5phrase1.2"
            self.repliques = ["dialogue-5reponse1.2.1"]
        elif replique == "dialogue-5reponse1.2.1":
            self.end_dialogue(-5)
        elif replique == "dialogue-5reponse1.1":
            self.replique="dialogue-5phrase1.1"
            self.repliques = ["dialogue-5reponse1.1.1"]
        elif replique == "dialogue-5reponse1.1.1":
            self.end_dialogue(-5)

        else:
            self.end_dialogue(self.dialogue)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def get_replique(self,code:str):
        return REPLIQUES_CODEUR[code]

    def get_skin(self):
        return SKIN_CODEUR

    def get_skins_vue(self):
        return [SKIN_CODEUR_VUE]

    def get_texte_descriptif(self):
        return ["Vous voulez bien éviter de fouiller la vie privée des gens ?"]
