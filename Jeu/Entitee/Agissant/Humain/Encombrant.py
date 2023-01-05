from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Controleur import Controleur

from Jeu.Entitee.Agissant.Humain.Humain import *

class Encombrant(Dps,Humain): #Le sixième humain du jeu, à l'étage 5 (moyennement apprèciable, surtout si on essaye de draguer sa copine)
    """La classe de l'encombrant."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'encombrant'
        self.place = 5

        Humain.__init__(self,controleur,position,self.identite,1,6) #En plus il a fallu que ce soit un combattant relativement aguerri...

        self.antagonise_offensifs = True #Il a un bon instinct pour sentir le danger

        self.appreciations = [0,1,-1,6,0,5,0,3,3,0]
        self.dialogue = 1

        #Penser à l'équipper

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats=0):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.4 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return (self.pv-degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
        elif self.dialogue == -2: #Le joueur nous a offensé !
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1"]
        elif self.dialogue == 1: #Le joueur vient de passer la porte
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1","dialogue1reponse1.2"] #/!\ N'afficher la réplique du copain que si on a discuté de son copain avec la peureuse
        elif self.dialogue == 2:
            self.replique = "dialogue2phrase1"
            self.repliques = ["dialogue2reponse1.1","dialogue2reponse1.2","dialogue2reponse1.3"]

    def interprete(self,replique:str):

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "dialogue1reponse1.1":
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1","dialogue1reponse1.1.2"]
        elif replique in ["dialogue1reponse1.1.1","dialogue1reponse1.2.1.1"]:
            self.replique="dialogue1phrase1.1.1"
            ID_clee = self.inventaire.get_clee("Porte_sortie_encombrant_5")
            self.inventaire.drop(None,ID_clee)
            self.controleur.joueur.inventaire.ramasse_item(ID_clee)
            self.repliques = ["dialogue1reponse1.1.1.1"]
            self.controleur.get_esprit(self.controleur.joueur.esprit).merge(self.esprit)
        elif replique == "dialogue1reponse1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1"]
        elif replique == "dialogue1reponse1.1.1.1.1":
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "dialogue1reponse1.1.2":
            self.replique="dialogue1phrase1.1.2"
            self.repliques = ["dialogue1reponse1.1.2.1"]
        elif replique == "dialogue1reponse1.1.2.1":
            self.end_dialogue(-2)
            self.statut_humain = "exploration"
            self.attente = False
        elif replique == "dialogue1reponse1.2":
            self.replique="dialogue1phrase1.2"
            self.repliques = ["dialogue1reponse1.2.1","dialogue1reponse1.2.2"]
        elif replique == "dialogue1reponse1.2.1":
            self.replique="dialogue1phrase1.2.1"
            self.repliques = ["dialogue1reponse1.2.1.1"]
        elif replique == "dialogue1reponse1.2.2":
            #self.controleur.get_esprit(self.esprit).antagonise(truc comme ça ou une offense ?
            #+ modifier le role, ou quelque chose, pour qu'il combatte
            self.attente = False
            self.end_dialogue(-2)
            self.statut_humain = "exploration"

        #Septième dialogue
        #Le joueur a utilisé un téléporteur
        elif replique == "dialogue2reponse1.1":
            self.replique="dialogue2phrase1.1"
            self.repliques = ["dialogue2reponse1.1.1","dialogue2reponse1.1.2","dialogue2reponse1.1.3"]
        elif replique == "dialogue2reponse1.2":
            self.replique="dialogue2phrase1.2"
            self.repliques = ["dialogue2reponse1.2.1"]
        elif replique == "dialogue2reponse1.3":
            self.end_dialogue()
            self.appreciations[0] -= 0.2
        elif replique == "dialogue2reponse1.1.1":
            self.replique="dialogue2phrase1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1","dialogue2reponse1.1.1.2"]
        elif replique == "dialogue2reponse1.1.2":
            self.replique="dialogue2phrase1.1.2"
            self.repliques = ["dialogue2reponse1.1.2.1"]
        elif replique == "dialogue2reponse1.1.3":
            self.appreciations[0] -= 0.1
            self.replique="dialogue2phrase1.1.3"
            self.repliques = ["dialogue2reponse1.1.3.1","dialogue2reponse1.1.3.2"]
        elif replique == "dialogue2reponse1.2.1":
            self.replique="dialogue2phrase1.1"
            self.repliques = ["dialogue2reponse1.1.1","dialogue2reponse1.1.2","dialogue2reponse1.1.3"]
        elif replique == "dialogue2reponse1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1","dialogue2reponse1.1.1.1.2"]
        elif replique == "dialogue2reponse1.1.1.2":
            self.end_dialogue()
        elif replique == "dialogue2reponse1.1.2.1":
            self.replique="dialogue2phrase1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1","dialogue2reponse1.1.1.2"]
        elif replique == "dialogue2reponse1.1.3.1":
            self.appreciations[0] -= 0.1
            self.replique="dialogue2phrase1.1.3.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1","dialogue2reponse1.1.1.1.2"]
        elif replique == "dialogue2reponse1.1.3.2":
            self.end_dialogue()
            self.appreciations[0] -= 0.2
        elif replique == "dialogue2reponse1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1","dialogue2reponse1.1.1.1.1.2"]#Euh, non/oui, l'épéiste
        elif replique == "dialogue2reponse1.1.1.1.2":
            self.end_dialogue()
        elif replique == "dialogue2reponse1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1","dialogue2reponse1.1.1.1.1.1.2"]#Oulà, zone/je m'en souviens
        elif replique == "dialogue2reponse1.1.1.1.1.2":
            self.replique="dialogue2phrase1.1.1.1.1.2"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1"]#Tout ce que je veux ?
        elif replique == "dialogue2reponse1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1"]#il ne se passe rien
        elif replique == "dialogue2reponse1.1.1.1.1.1.2":
            self.replique="dialogue2phrase1.1.1.1.1.2"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1"]#Tout ce que je veux ?
        elif replique == "dialogue2reponse1.1.1.1.1.2.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1"]#Ah zut
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.1","dialogue2reponse1.1.1.1.1.2.1.1.1.2"]#Euh... rappel/oui, dans quel zone?
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.2":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.2.1"]#Je vois merci
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.2.1":
            self.end_dialogue()
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.2.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue2phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue2reponse1.1.1.1.1.2.1.1.1.2.1"]

        #Dialogue par défaut -2
        elif replique == "":
            self.end_dialogue(-2)
            self.statut_humain = "exploration"

        #Dialogue par défaut:
        elif replique == "dialogue-1reponse1.1":
            self.replique = "dialogue-1phrase1.1"
            self.repliques = ["dialogue-1reponse1.1.1","dialogue-1reponse1.1.2","dialogue-1reponse1.1.3"]
        elif replique == "dialogue-1reponse1.1.1":
            self.mouvement = 0
            self.replique = "dialogue-1phrase1.1.1"
            self.repliques = ["dialogue-1reponse1.1.1.1","dialogue-1reponse1.1.1.2"]
        elif replique == "dialogue-1reponse1.1.1.1":
            self.replique = "dialogue-1phrase1.1.3"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3"]
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
        elif replique == "dialogue-1reponse1.1.1.2":
            self.controleur.set_phase(AGISSANT_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.2":
            self.controleur.set_phase(CASE_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.3":
            self.replique = "dialogue-1phrase1.1.3"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3"]
            self.mouvement = 1
        elif replique == "dialogue-1reponse1.3":
            self.end_dialogue(-1)
        elif replique == "dialogue-1reponse1.2":
            self.replique = "dialogue-1phrase1.2"
            self.repliques = ["dialogue-1reponse1.2.1"]
        elif replique == "dialogue-1reponse1.2.1":
            self.end_dialogue(-1)

        else:
            self.end_dialogue(self.dialogue)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def get_replique(self,code:str):
        return REPLIQUES_ENCOMBRANT[code]

    def get_skin_tete(self):
        return SKIN_TETE_ENCOMBRANT

    def get_texte_descriptif(self):
        return [f"Un humain (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un aventurier épéiste. Il a été capturé par les gobelins."]
