from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Direction import Direction
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Agissant.Humain.Humain import Humain
from ..Entitee.Agissant.Role.Dps import Dps

class Receptionniste(Dps,Humain): #Le deuxième humain du jeu, à l'étage 1 (engage la conversation après la chute, indique les commandes de base)
    """La classe du récéptionniste."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'receptionniste'
        self.place = 1

        Humain.__init__(self,controleur,self.identite,2,3,position) #À un haut niveau dès le départ

        self.antagonise_offensifs = True #Des années d'expérience lui ont appris à repérer les monstres offensifs

        self.appreciations = [0,3,0,0,0,0,1,3,6,0]
        self.dialogue = 1

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats:float=0):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite, et qu'il n'y ait aucun allié en danger au front
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.2 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return (self.pv+degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : modifier le taux limite en fonction des autres humains en danger au front et de l'appréciation qu'on a pour eux
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -2: #Le joueur est venu nous voir avant d'être sorti du premier couloir
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1","dialogue-2reponse1.2","dialogue-2reponse1.3"]
        elif self.dialogue == 1: #Le joueur vient de tomber
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1"]
        elif self.dialogue == 2: #Le joueur vient de se dégourdir les jambes
            self.replique = "dialogue2phrase1"
            self.repliques = ["dialogue2reponse1.1","dialogue2reponse1.2"]

    def interprete(self,replique:str):
        assert isinstance(self.controleur.joueur, Humain)

        #Premier dialogue
        #Le receptionniste accueil le joueur
        if replique == "dialogue1reponse1.1":
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1"]
        elif replique == "dialogue1reponse1.1.1":
            self.appreciations[self.controleur.joueur.place] += 0.5
            self.end_dialogue(2)

        #Deuxième dialogue
        #Le receptionniste guide le joueur vers l'escalier
        elif replique == "dialogue2reponse1.1":
            self.replique = "dialogue2phrase1.1"
            self.repliques = ["dialogue2reponse1.1.1","dialogue2reponse1.1.2"]
        elif replique == "dialogue2reponse1.1.1":
            self.replique = "dialogue2phrase1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1":
            self.replique = "dialogue2phrase1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.2":
            self.replique = "dialogue2phrase1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1"]
        elif replique == "dialogue2reponse1.2":
            self.replique = "dialogue2phrase1.1.1.1"
            self.repliques = ["dialogue2reponse1.1.1.1.1"]
        elif replique == "dialogue2reponse1.1.1.1.1":
            self.end_dialogue(-2)

        elif replique == "dialogue-2reponse1.1":
            self.replique="dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.2":
            self.replique = "dialogue-2phrase1.2"
            self.repliques = ["dialogue-2reponse1.2.1"]
        elif replique == "dialogue-2reponse1.2.1":
            self.replique = "dialogue-2phrase1.2.1"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.3":
            self.replique = "dialogue-2phrase1.3"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.1.1":
            self.end_dialogue(-2)

        else:
            self.end_dialogue(self.dialogue)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def get_replique(self,code:str):
        return REPLIQUES_RECEPTIONNISTE[code]

    def get_skin_tete(self):
        return SKIN_TETE_RECEPTIONNISTE

    def get_texte_descriptif(self):
        return [f"Un humain (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un aventurier épéiste."]

# Imports utilisés dans le code:
from Old_Affichage.Skins.Skins import SKIN_TETE_RECEPTIONNISTE
from ..Dialogues.Dialogues_receptionniste import REPLIQUES_RECEPTIONNISTE