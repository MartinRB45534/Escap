from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Agissant.Humain.Humain import Humain
from Jeu.Entitee.Agissant.Role.Dps import Dps

class Marchand(Dps,Humain): #Le dixième humain du jeu, à l'étage 9 (le seul lien avec l'extérieur)
    """La classe du marchand."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'marchand'
        self.place = 9

        Humain.__init__(self,controleur,self.identite,1,10,position) #Il a un skill d'échange d'objet avec son patron à l'extérieur

        self.appreciations = [0,0,-1,0,0,-1,0,3,0,2]
        self.dialogue = 1

        #Est-ce qu'il a un minimum d'équippement ? Ou est-ce qu'il achète son équippement de base après avoir rencontré le joueur ?

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats:float=0):
        #On fuit si on est en danger (pv trop bas)
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.4 + 0.01*self.appreciations[9] #Quand on se hait, on devient plus suicidaire
        return (self.pv+degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3"]
        elif self.dialogue == -2:
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1","dialogue-2reponse1.2"]
        elif self.dialogue == 1:
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1"]

    def interprete(self,replique:str):
        assert isinstance(self.controleur.joueur, Humain)

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "dialogue1reponse1.1":
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1","dialogue1reponse1.1.2"]
        elif replique == "dialogue1reponse1.1.2":
            self.replique="dialogue1phrase1.1.2" #/!\ Donner un peu de sous
            self.repliques = ["dialogue1reponse1.1.2.1"]
        elif replique == "dialogue1reponse1.1.2.1":
            self.replique="dialogue1phrase1.1.2.1"
            self.repliques = ["dialogue1reponse1.1.2.1.1","dialogue1reponse1.1.2.1.2"]
        elif replique == "dialogue1reponse1.1.2.1.1":
            self.end_dialogue()
            self.controleur.joueur.esprit.merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue1reponse1.1.2.1.2":
            self.end_dialogue(-2)
        elif replique == "dialogue1reponse1.1.1":
            self.replique="dialogue1phrase1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1"]
            self.controleur.joueur.esprit.merge(self.esprit)
        elif replique == "dialogue1reponse1.1.1.1":
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur

        #Dialogue par défaut:
        elif replique == "dialogue-1reponse1.1":
            self.replique = "dialogue-1phrase1.1"
            self.repliques = ["dialogue-1reponse1.1.1"]
        elif replique == "dialogue-1reponse1.1.1":
            self.replique = "dialogue-1phrase1.1.1"
            self.repliques = ["dialogue-1reponse1.1.1.1","dialogue-1reponse1.1.1.2","dialogue-1reponse1.1.1.3"]
        elif replique == "dialogue-1reponse1.1.1.1":
            self.mouvement = 0
            self.replique = "dialogue-1phrase1.1.1.1"
            self.repliques = ["dialogue-1reponse1.1.1.1.1","dialogue-1reponse1.1.1.1.2"]
        elif replique == "dialogue-1reponse1.1.1.1.1":
            self.replique = "dialogue-1phrase1.1.1.1.1"
            self.repliques = ["dialogue-1reponse1.1.1","dialogue-1reponse1.1.2","dialogue-1reponse1.1.3"]
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue-1reponse1.1.1.1.2":
            self.controleur.set_phase(AGISSANT_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.1.2":
            self.controleur.set_phase(CASE_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.1.3":
            self.replique = "dialogue-1phrase1.1.1.1.2"
            self.repliques = ["dialogue-1reponse1.1.1","dialogue-1reponse1.1.2","dialogue-1reponse1.1.3"]
            self.mouvement = 1
        elif replique == "dialogue-1reponse1.1.3":
            self.end_dialogue(-1)
        elif replique == "dialogue-1reponse1.1.2":
            self.replique = "dialogue-1phrase1.1.2"
            self.repliques = ["dialogue-1reponse1.1.2.1"]
        elif replique == "dialogue-1reponse1.1.2.1":
            self.end_dialogue(-1)

        elif replique == "dialogue-2reponse1.1":
            self.replique = "dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.2":
            self.replique = "dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.1.1":
            self.end_dialogue(-2)

        else:
            self.end_dialogue(self.dialogue)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def set_cible(self,cible):
        self.cible_deplacement = cible
        self.replique = "dialogue-1phrase1.1.1.1.2"
        self.repliques = ["dialogue-1reponse1.1.1","dialogue-1reponse1.1.2","dialogue-1reponse1.1.3"]

    def get_replique(self,code:str):
        return REPLIQUES_MARCHAND[code]

    def get_skin_tete(self):
        return SKIN_TETE_MARCHAND

    def get_texte_descriptif(self):
        return [f"Un humain (niveau {self.niveau})",f"ID : {self}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un marchand perdu dans le labyrinthe. Il peut obtenir des objets de l'extérieur ou en envoyer, mais il ne peut pas sortir lui-même..."]

# Imports utilisés dans le code:
from Jeu.Constantes import *
from Affichage.Skins.Skins import SKIN_TETE_MARCHAND
from Jeu.Dialogues.Dialogues_marchand import REPLIQUES_MARCHAND