from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Agissant.Humain.Humain import Humain
from Old_Jeu.Entitee.Agissant.Role.Tank import Tank
from Old_Jeu.Entitee.Agissant.Role.Sentinelle import Sentinelle

class Paume(Tank,Sentinelle,Humain): #Le troisième humain du jeu, à l'étage 2 (complêtement paumé, rejoint le joueur sauf rares exceptions)
    """La classe du mec paumé."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'paume'
        self.place = 2

        Humain.__init__(self,controleur,self.identite,1,4,position) #Plutôt faible, de base

        self.appreciations = [1,1,3,2,0,0,0,7,4,-1]
        self.dialogue = 1

        #Est-ce qu'il a un minimum d'équippement ?

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats:float=0):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.1 + 0.01*self.appreciations[2] #Quand on se hait, on devient plus suicidaire
        return (self.pv+degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : modifier le taux limite en fonction des autres humains en danger au front et de l'appréciation qu'on a pour eux (exceptionnel, pour le cas où le paumé serait amoureux, sinon il obéit et fuit normalement)
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
        elif self.dialogue == -2: #Le joueur nous a très mal traité
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1","dialogue-2reponse1.2","dialogue-2reponse1.3"]
        elif self.dialogue == 1: #Le joueur vient d'arriver depuis le premier étage
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1","dialogue1reponse1.2"]
        elif self.dialogue == 2: #On a vaincu le premier monstre !
            self.replique = "dialogue2phrase1"
            self.repliques = ["dialogue2reponse1.1","dialogue2reponse1.2","dialogue2reponse1.3"]
        elif self.dialogue == 3: #On a vaincu le premier mage !
            self.replique = "dialogue3phrase1"
            self.repliques = ["dialogue3reponse1.1","dialogue3reponse1.2"]
        elif self.dialogue == 4: #On a atteint la prison
            self.replique = "dialogue4phrase1"
            self.repliques = ["dialogue4reponse1.1","dialogue4reponse1.2","dialogue4reponse1.3"]
        elif self.dialogue == 5:
            self.replique = "dialogue5phrase1"
            self.repliques = ["dialogue5reponse1.1","dialogue5reponse1.2","dialogue5reponse1.3"]

    def interprete(self,replique:str):
        assert isinstance(self.controleur.joueur, Humain)

        #Premier dialogue
        #Le joueur arrive par l'escalier
        if replique == "dialogue1reponse1.1":
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1"]
        elif replique == "dialogue1reponse1.1.1":
            self.replique="dialogue1phrase1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.2":
            self.replique="dialogue1phrase1.1.1.2"
            self.repliques = ["dialogue1reponse1.1.1.2.1"]
        elif replique in ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2.1"]:
            self.replique="dialogue1phrase1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1","dialogue1reponse1.1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1.1"]
            self.appreciations[self.controleur.joueur.place]+= 0.5
            self.controleur.joueur.esprit.merge(self.esprit)
        elif replique == "dialogue1reponse1.1.1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1.1.1"
            self.repliques=["dialogue1reponse1.1.1.1.1.1.1"]
        elif replique == "dialogue1reponse1.1.1.1.1.1.1":
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue1reponse1.1.1.1.2":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"
        elif replique == "dialogue1reponse1.2":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"
        elif replique == "dialogue-2reponse1.2":
            self.replique="dialogue-2phrase1.2"
            self.repliques = ["dialogue-2reponse1.2.1"]
        elif replique == "dialogue-2reponse1.2.1":
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"
        elif replique == "dialogue-2reponse1.3":
            self.replique="dialogue-2phrase1.3"
            self.repliques = ["dialogue-2reponse1.3.1"]
            self.appreciations[self.controleur.joueur.place]+= 0.5
        elif replique == "dialogue-2reponse1.3.1":
            self.replique="dialogue-2phrase1.3.1"
            self.repliques = ["dialogue-2reponse1.3.1.1","dialogue-2reponse1.3.1.2"]
            self.controleur.joueur.esprit.merge(self.esprit)
        elif replique == "dialogue-2reponse1.3.1.1":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue-2reponse1.3.1.2":
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur

        #Deuxième dialogue
        #On vient de tuer le premier gobelin
        elif replique == "dialogue2reponse1.1":
            self.replique = "dialogue2phrase1.1"
            self.repliques = ["dialogue2reponse1.1.1","dialogue2reponse1.1.2"]
        elif replique in ["dialogue2reponse1.1.1","dialogue2reponse1.2","dialogue2reponse1.3.1.1"]:
            self.end_dialogue()
        elif replique in ["dialogue2reponse1.3","dialogue2reponse1.1.2","dialogue2reponse1.3.1.2"]:
            self.replique = "dialogue2phrase1.3"
            self.repliques = ["dialogue2reponse1.3.1","dialogue2reponse1.3.2","dialogue2reponse1.3.3"]
        elif replique == "dialogue2reponse1.3.1":
            self.replique = "dialogue2phrase1.3.1" #/!\ Modifier si la "barre rouge" bouge
            self.repliques = ["dialogue2reponse1.3.1.1","dialogue2reponse1.3.1.2"]
        elif replique == "dialogue2reponse1.3.2":
            self.replique = "dialogue2phrase1.3.2" #/!\ Modifier pour mentionner l'attaque avec une arme quand les skins auront été créés
            if self.controleur.agissants[5].esprit == "heros":
                self.replique = "dialogue2phrase1.3.2/peureuse"
            self.repliques = ["dialogue2reponse1.3.1.1","dialogue2reponse1.3.1.2"]
        elif replique == "dialogue2reponse1.3.3":
            self.replique = "dialogue2phrase1.3.3"
            self.repliques = ["dialogue2reponse1.3.1.1","dialogue2reponse1.3.1.2"]

        #Troisième dialogue
        #On vient de tuer le premier mage gobelin
        elif replique == "dialogue3reponse1.1":
            self.replique = "dialogue3phrase1.1"
            self.repliques = ["dialogue3reponse1.1.1","dialogue3reponse1.1.2"]
        elif replique == "dialogue3reponse1.1.1":
            self.replique = "dialogue3phrase1.1.1"
            self.repliques = ["dialogue3reponse1.1.1.1"]
        elif replique == "dialogue3reponse1.1.2":
            self.replique = "dialogue3phrase1.1.2"
            self.repliques = ["dialogue3reponse1.1.2.1"]
        elif replique in ["dialogue3reponse1.2","dialogue3reponse1.1.2.1","dialogue3reponse1.1.1.1"]:
            self.end_dialogue()

        #Dialogue de la prison
        elif replique == "dialogue4reponse1.1":
            self.replique="dialogue4phrase1.1"
            self.repliques = ["dialogue4reponse1.1.1"]
        elif replique == "dialogue4reponse1.1.1":
            self.replique="dialogue4phrase1.1.1"
            self.repliques = ["Ok, je regarderai autour de moi."]
        elif replique == "dialogue4reponse1.1.1.1":
            self.end_dialogue()
        elif replique == "dialogue4reponse1.2":
            self.replique="dialogue4phrase1.2"
            self.repliques = ["dialogue4reponse1.1.1"]
        elif replique == "dialogue4reponse1.3":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue()

        #Cinquième dialogue
        #Le joueur a utilisé un téléporteur
        elif replique == "dialogue5reponse1.1":
            self.replique="dialogue5phrase1.1"
            self.repliques = ["dialogue5reponse1.1.1","dialogue5reponse1.1.2","dialogue5reponse1.1.3"]
        elif replique == "dialogue5reponse1.2":
            self.replique="dialogue5phrase1.2"
            self.repliques = ["dialogue5reponse1.2.1"]
        elif replique == "dialogue5reponse1.3":
            self.end_dialogue()
            self.appreciations[self.controleur.joueur.place] -= 0.2
        elif replique == "dialogue5reponse1.1.1":
            self.replique="dialogue5phrase1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1","dialogue5reponse1.1.1.2"]
        elif replique == "dialogue5reponse1.1.2":
            self.replique="dialogue5phrase1.1.2"
            self.repliques = ["dialogue5reponse1.1.2.1"]
        elif replique == "dialogue5reponse1.1.3":
            self.appreciations[self.controleur.joueur.place] -= 0.1
            self.replique="dialogue5phrase1.1.3"
            self.repliques = ["dialogue5reponse1.1.3.1","dialogue5reponse1.1.3.2"]
        elif replique == "dialogue5reponse1.2.1":
            self.replique="dialogue5phrase1.1"
            self.repliques = ["dialogue5reponse1.1.1","dialogue5reponse1.1.2","dialogue5reponse1.1.3"]
        elif replique == "dialogue5reponse1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1","dialogue5reponse1.1.1.1.2"]
        elif replique == "dialogue5reponse1.1.1.2":
            self.end_dialogue()
        elif replique == "dialogue5reponse1.1.2.1":
            self.replique="dialogue5phrase1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1","dialogue5reponse1.1.1.2"]
        elif replique == "dialogue5reponse1.1.3.1":
            self.appreciations[self.controleur.joueur.place] -= 0.1
            self.replique="dialogue5phrase1.1.3.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1","dialogue5reponse1.1.1.1.2"]
        elif replique == "dialogue5reponse1.1.3.2":
            self.end_dialogue()
            self.appreciations[self.controleur.joueur.place] -= 0.2
        elif replique == "dialogue5reponse1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1","dialogue5reponse1.1.1.1.1.2"]#Euh, non/oui, l'épéiste
        elif replique == "dialogue5reponse1.1.1.1.2":
            self.end_dialogue()
        elif replique == "dialogue5reponse1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1","dialogue5reponse1.1.1.1.1.1.2"]#Oulà, zone/je m'en souviens
        elif replique == "dialogue5reponse1.1.1.1.1.2":
            self.replique="dialogue5phrase1.1.1.1.1.2"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1"]#Tout ce que je veux ?
        elif replique == "dialogue5reponse1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1"]#il ne se passe rien
        elif replique == "dialogue5reponse1.1.1.1.1.1.2":
            self.replique="dialogue5phrase1.1.1.1.1.2"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1"]#Tout ce que je veux ?
        elif replique == "dialogue5reponse1.1.1.1.1.2.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1"]#Ah zut
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.1","dialogue5reponse1.1.1.1.1.2.1.1.1.2"]#Euh... rappel/oui, dans quel zone?
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.2":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.2.1"]#Je vois merci
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.2.1":
            self.end_dialogue()
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.2.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue5phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue5reponse1.1.1.1.1.2.1.1.1.2.1"]

        #Dialogue par défaut:
        elif replique == "dialogue-1reponse1.1":
            self.replique = "dialogue-1phrase1.1"
            self.repliques = ["dialogue-1reponse1.1.1","dialogue-1reponse1.1.2","dialogue-1reponse1.1.3"]
        elif replique == "dialogue-1reponse1.1.1":
            self.mouvement = 0
            self.replique = "dialogue-1phrase1.1.1"
            self.repliques = ["dialogue-1reponse1.1.1.1","dialogue-1reponse1.1.1.2"]
        elif replique == "dialogue-1reponse1.1.1.1":
            self.replique = "dialogue-1phrase1.1.1.1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3"]
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue-1reponse1.1.1.2":
            self.controleur.set_phase(AGISSANT_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.2":
            self.controleur.set_phase(CASE_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.3":
            self.replique = "dialogue-1phrase1.1.3"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3"]
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
        return REPLIQUES_PAUME[code]

    def get_skin(self):
        return SKIN_CORPS_PAUME

    def get_skin_tete(self):
        return SKIN_TETE_PAUME

    def get_texte_descriptif(self):
        if self.statut is None:
            self.set_statut("")
            print("Hey, mon statut vaut None, pourquoi !?")
        return [f"Un humain (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un humain terrorisé par les labyrinthes. Il espère pouvoir sortir un jour de cet enfer."]

# Imports utilisés dans le code:
from Old_Jeu.Constantes import *
from Old_Affichage.Skins.Skins import SKIN_TETE_PAUME, SKIN_CORPS_PAUME
from Old_Jeu.Dialogues.Dialogues_paume import REPLIQUES_PAUME