from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Agissant.Humain.Humain import Humain
from Old_Jeu.Entitee.Agissant.PNJ.PNJs import PNJ_mage
from Old_Jeu.Entitee.Agissant.Role.Multi_renforceur import Multi_renforceur
from Old_Jeu.Entitee.Agissant.Role.Support_lointain import Support_lointain

class Peureuse(PNJ_mage,Multi_renforceur,Support_lointain,Humain): #La quatrième humaine du jeu, à l'étage 3 (terrorisée par les monstres)
    """La classe de la peureuse."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'peureuse'
        self.place = 3

        Humain.__init__(self,controleur,self.identite,1,5,position) #Plutôt faible, de base

        self.comportement_corps_a_corps = 2
        self.comportement_distance = 2
        self.antagonise_offensifs = False

        self.appreciations = [1,1,0,-1,0,9,1,6,-1,-1]
        self.dialogue = 1

        #Est-ce qu'elle a un minimum d'équippement ?

        #Peut recevoir l'ordre : d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats:float=0):
        #On fuit si on est en danger (pv trop bas) ou en présence d'un monstre à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.7 + 0.01*self.appreciations[3] #Quand on se hait, on devient plus suicidaire
        return (self.pv+degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : fuire dès qu'il y a un monstre en vue et accessible
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def peut_multi_caster(self):
        return self.peut_payer(cout_pm_multi_boost[self.get_skill_magique().niveau-1])

    def multi_caste(self):
        return "magie multi boost"

    def peut_caster(self):
        return self.peut_payer(cout_pm_boost[self.get_skill_magique().niveau-1])

    def caste(self):
        return "magie boost"

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
        elif self.dialogue == -2: #Le joueur nous a mal traîté
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1"]
        elif self.dialogue == 1: #Le joueur vient d'arriver depuis le deuxième étage
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1","dialogue1reponse1.2"]
        elif self.dialogue == 2: #On a vaincu le premier monstre !
            self.replique = "dialogue2phrase1"
            self.repliques = ["dialogue2reponse1.1","dialogue2reponse1.2","dialogue2reponse1.3"]
        elif self.dialogue == 3: #On a vaincu le premier mage !
            self.replique = "dialogue3phrase1"
            self.repliques = ["dialogue3reponse1.1","dialogue3reponse1.2"]
        elif self.dialogue == 4: #On a atteint les premiers monstres
            self.replique = "dialogue4phrase1"
            self.repliques = ["dialogue4reponse1.1","dialogue4reponse1.2","dialogue4reponse1.3"]
        elif self.dialogue == 5: #On a atteint la prison
            self.replique = "dialogue5phrase1"
            self.repliques = ["dialogue5reponse1.1","dialogue5reponse1.2","dialogue5reponse1.3"]
        elif self.dialogue == 6: #On a progressé dans la prison
            self.replique = "dialogue6phrase1"
            self.repliques = ["dialogue6reponse1.1","dialogue6reponse1.2","dialogue6reponse1.3"]
        elif self.dialogue == 7:
            self.replique = "dialogue7phrase1"
            self.repliques = ["dialogue7reponse1.1","dialogue7reponse1.2","dialogue7reponse1.3"]

    def interprete(self,replique:str):
        assert isinstance(self.controleur.joueur, Humain)

        #Premier dialogue
        #Le joueur arrive par l'escalier
        if replique in ["dialogue1reponse1.1","dialogue1reponse1.2.1"]:
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1","dialogue1reponse1.1.2"]
        elif replique == "dialogue1reponse1.1.1":
            self.replique="dialogue1phrase1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2"]
        elif replique == "dialogue1reponse1.1.2":
            self.replique="dialogue1phrase1.1.2"
            self.repliques = ["dialogue1reponse1.1.2.1"]
        elif replique == "dialogue1reponse1.1.2.1":
            self.replique="dialogue1phrase1.1.2.1"
            self.repliques = ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1","dialogue1reponse1.1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1.2":
            self.appreciations[self.controleur.joueur.place] += 0.5
            self.end_dialogue()
            self.controleur.joueur.esprit.merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue1reponse1.1.1.2":
            self.replique="dialogue1phrase1.1.1.2"
            self.repliques = ["dialogue1reponse1.1.1.2.1","dialogue1reponse1.1.1.2.2"]
        elif replique == "dialogue1reponse1.1.1.2.1":
            self.replique="dialogue1phrase1.1.1.2.1"
            self.repliques = ["dialogue1reponse1.1.1.2.1.1","dialogue1reponse1.1.1.2.1.2"]
        elif replique in ["dialogue1reponse1.1.1.1.1","dialogue1reponse1.1.1.2.1.2"]:
            self.replique="dialogue1phrase1.1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1.1","dialogue1reponse1.1.1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1.1.2":
            self.replique="dialogue1phrase1.1.1.1.1.2"
            self.repliques = ["dialogue1reponse1.1.1.1.1.2.1","dialogue1reponse1.1.1.1.1.2.2"]
        elif replique in ["dialogue1reponse1.1.1.1.1.2.1","dialogue1reponse1.1.1.2.1.1"]:
            self.end_dialogue()
            self.controleur.joueur.esprit.merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue1reponse1.1.1.1.1.2.2":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"
        elif replique == "dialogue1reponse1.1.1.2.2":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"
        elif replique == "dialogue1reponse1.2":
            self.replique="dialogue1phrase1.2"
            self.repliques = ["dialogue1reponse1.2.1","dialogue1reponse1.2.2"]
        elif replique == "dialogue1reponse1.2.2":
            self.replique="dialogue1phrase1.2.2"
            self.repliques = ["dialogue1reponse1.2.1"]

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"

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
            self.repliques = ["dialogue3reponse1.1.1.1","dialogue3reponse1.1.1.2"]
        elif replique in ["dialogue3reponse1.1.2","dialogue3reponse1.2"]:
            self.end_dialogue()
        elif replique == "dialogue3reponse1.1.1.1":
            self.appreciations[self.controleur.joueur.place]+= 0.1
            self.end_dialogue()
        elif replique == "dialogue3reponse1.1.1.2":
            self.appreciations[self.controleur.joueur.place]-= 0.3
            self.end_dialogue()

        #Dialogue de description des monstres
        elif replique == "dialogue4reponse1.1":
            self.replique="dialogue4phrase1.1"
            self.repliques = ["dialogue4reponse1.1.1","dialogue4reponse1.1.2"]
        elif replique == "dialogue4reponse1.1.1":
            self.replique="dialogue4phrase1.1.1"
            self.repliques = ["dialogue4reponse1.1.1.1","dialogue4reponse1.1.1.2"]
        elif replique == "dialogue4reponse1.1.1.1":
            self.replique="dialogue4phrase1.1.1.1"
            self.repliques = ["dialogue4reponse1.1.1.1.1","dialogue4reponse1.1.1.1.2"]
        elif replique in ["dialogue4reponse1.1.1.1.1","dialogue4reponse1.1.1.2"]:
            self.replique="dialogue4phrase1.1.1.2"
            self.repliques = ["dialogue4reponse1.1.1.1.2"]
        elif replique == "dialogue4reponse1.1.1.1.2":
            self.replique="dialogue4phrase1.1.1.1.2"
            self.repliques = ["dialogue4reponse1.1.1.1.2.1","dialogue4reponse1.1.1.1.2.2"]
        elif replique == "dialogue4reponse1.1.1.1.2.1":
            self.replique="dialogue4phrase1.1.1.1.2.1"
            self.repliques = ["dialogue4reponse1.1.1.1.2.1.1"]
        elif replique == "dialogue4reponse1.1.1.1.2.2":
            self.appreciations[self.controleur.joueur.place]+= 0.5
            self.replique="dialogue4phrase1.1.1.1.2.2"
            self.repliques = ["dialogue4reponse1.1.1.1.2.1.1"]
        elif replique == "dialogue4reponse1.1.2":
            self.replique="dialogue4phrase1.1.2"
            self.repliques = ["dialogue4reponse1.1.2.1"]
        elif replique == "dialogue4reponse1.1.2.1":
            self.replique="dialogue4phrase1.1.2.1"
            self.repliques = ["dialogue4reponse1.1.2.1.1","dialogue4reponse1.1.2.1.2"]
        elif replique == "dialogue4reponse1.1.2.1.1":
            self.replique="dialogue4phrase1.1.2.1.1"
            self.repliques = ["dialogue4reponse1.1.2.1.1.1","dialogue4reponse1.1.2.1.1.2"]
        elif replique == "dialogue4reponse1.1.2.1.1.1":
            self.replique="dialogue4phrase1.1.2.1.1.1"
            self.repliques = ["dialogue4reponse1.1.2.1.1.1.1"]
        elif replique == "dialogue4reponse1.1.2.1.1.1.1":
            self.replique="dialogue4phrase1.1.2.1.1.1.1"
            self.repliques = ["dialogue4reponse1.1.2.1.1.1.1.1","dialogue4reponse1.1.2.1.1.1.1.2"]
        elif replique == "dialogue4reponse1.1.2.1.1.1.1.1":
            self.replique="dialogue4phrase1.1.2.1.1.1.1.1"
            self.appreciations[self.controleur.joueur.place]+=0.5
            self.repliques = ["dialogue4reponse1.1.1.1.2.1.1"]
        elif replique == "dialogue4reponse1.1.2.1.1.2":
            self.replique="dialogue4phrase1.1.2.1.1.2"
            self.repliques = ["dialogue4reponse1.1.2.1.1.2.1"]
        elif replique == "dialogue4reponse1.1.2.1.2":
            self.replique="dialogue4phrase1.1.2.1.2"
            self.repliques = ["dialogue4reponse1.1.2.1.1.1.1"]
        elif replique == "dialogue4reponse1.2":
            self.replique="dialogue4phrase1.2"
            self.repliques = ["dialogue4reponse1.2.1"]
        elif replique in ["dialogue4reponse1.2.1","dialogue4reponse1.1.2.1.1.2.1","dialogue4reponse1.1.2.1.1.1.1.2","dialogue4reponse1.1.1.1.2.1.1"]:
            self.end_dialogue()
        elif replique == "dialogue4reponse1.3":
            self.replique="dialogue4phrase1.3"
            self.repliques = ["dialogue4reponse1.2.1"]
            self.appreciations[self.controleur.joueur.place]-= 0.3

        #Dialogue de la prison, première étape
        elif replique == "dialogue5reponse1.1":
            self.replique="dialogue5phrase1.1"
            self.repliques = ["dialogue5reponse1.1.1","dialogue5reponse1.1.2"]
        elif replique == "dialogue5reponse1.1.1":
            self.replique="dialogue5phrase1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1"]
        elif replique == "dialogue5reponse1.1.2":
            self.replique="dialogue5phrase1.1.2"
            self.repliques = ["dialogue5reponse1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1":
            clee = self.inventaire.get_clee("Porte_avant_prison_5")
            assert clee is not None
            self.inventaire.drop(ABSENT,clee)
            self.controleur.joueur.inventaire.ajoute(clee) #On refile au joueur la clé dont il a besoin
            self.replique="dialogue5phrase1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1":
            self.end_dialogue()
        elif replique == "dialogue5reponse1.2":
            clee = self.inventaire.get_clee("Porte_avant_prison_5")
            assert clee is not None
            self.inventaire.drop(ABSENT,clee)
            self.controleur.joueur.inventaire.ajoute(clee) #On refile quand même au joueur la clé dont il a besoin
            self.appreciations[self.controleur.joueur.place]+= 0.5
            self.end_dialogue()
        elif replique == "dialogue5reponse1.3":
            clee = self.inventaire.get_clee("Porte_avant_prison_5")
            assert clee is not None
            self.inventaire.drop(ABSENT,clee)
            self.controleur.joueur.inventaire.ajoute(clee) #On refile quand même au joueur la clé dont il a besoin
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue()

        #Dialogue de la prison, deuxième étape
        elif replique == "dialogue6reponse1.1":
            self.replique="dialogue6phrase1.1"
            self.repliques = ["dialogue6reponse1.1.1"]
        elif replique == "dialogue6reponse1.1.1":
            self.replique="dialogue6phrase1.1.1"
            self.repliques = ["dialogue6reponse1.1.1.1"]
        elif replique == "dialogue6reponse1.1.1.1":
            self.end_dialogue()
        elif replique == "dialogue6reponse1.2":
            self.appreciations[self.controleur.joueur.place]+= 0.5
            self.end_dialogue()
        elif replique == "dialogue6reponse1.3":
            self.appreciations[self.controleur.joueur.place]-= 0.5
            self.end_dialogue()

        #Septième dialogue
        #Le joueur a utilisé un téléporteur
        elif replique == "dialogue7reponse1.1":
            self.replique="dialogue7phrase1.1"
            self.repliques = ["dialogue7reponse1.1.1","dialogue7reponse1.1.2","dialogue7reponse1.1.3"]
        elif replique == "dialogue7reponse1.2":
            self.replique="dialogue7phrase1.2"
            self.repliques = ["dialogue7reponse1.2.1"]
        elif replique == "dialogue7reponse1.3":
            self.end_dialogue()
            self.appreciations[self.controleur.joueur.place] -= 0.2
        elif replique == "dialogue7reponse1.1.1":
            self.replique="dialogue7phrase1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1","dialogue7reponse1.1.1.2"]
        elif replique == "dialogue7reponse1.1.2":
            self.replique="dialogue7phrase1.1.2"
            self.repliques = ["dialogue7reponse1.1.2.1"]
        elif replique == "dialogue7reponse1.1.3":
            self.appreciations[self.controleur.joueur.place] -= 0.1
            self.replique="dialogue7phrase1.1.3"
            self.repliques = ["dialogue7reponse1.1.3.1","dialogue7reponse1.1.3.2"]
        elif replique == "dialogue7reponse1.2.1":
            self.replique="dialogue7phrase1.1"
            self.repliques = ["dialogue7reponse1.1.1","dialogue7reponse1.1.2","dialogue7reponse1.1.3"]
        elif replique == "dialogue7reponse1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1","dialogue7reponse1.1.1.1.2"]
        elif replique == "dialogue7reponse1.1.1.2":
            self.end_dialogue()
        elif replique == "dialogue7reponse1.1.2.1":
            self.replique="dialogue7phrase1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1","dialogue7reponse1.1.1.2"]
        elif replique == "dialogue7reponse1.1.3.1":
            self.appreciations[self.controleur.joueur.place] -= 0.1
            self.replique="dialogue7phrase1.1.3.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1","dialogue7reponse1.1.1.1.2"]
        elif replique == "dialogue7reponse1.1.3.2":
            self.end_dialogue()
            self.appreciations[self.controleur.joueur.place] -= 0.2
        elif replique == "dialogue7reponse1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1","dialogue7reponse1.1.1.1.1.2"]#Euh, non/oui, l'épéiste
        elif replique == "dialogue7reponse1.1.1.1.2":
            self.end_dialogue()
        elif replique == "dialogue7reponse1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1","dialogue7reponse1.1.1.1.1.1.2"]#Oulà, zone/je m'en souviens
        elif replique == "dialogue7reponse1.1.1.1.1.2":
            self.replique="dialogue7phrase1.1.1.1.1.2"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1"]#Tout ce que je veux ?
        elif replique == "dialogue7reponse1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1"]#il ne se passe rien
        elif replique == "dialogue7reponse1.1.1.1.1.1.2":
            self.replique="dialogue7phrase1.1.1.1.1.2"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1"]#Tout ce que je veux ?
        elif replique == "dialogue7reponse1.1.1.1.1.2.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1"]#Ah zut
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.1","dialogue7reponse1.1.1.1.1.2.1.1.1.2"]#Euh... rappel/oui, dans quel zone?
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.2":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.2.1"]#Je vois merci
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.2.1":
            self.end_dialogue()
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.2.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.2.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1"]
        elif replique == "dialogue7reponse1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1":
            self.replique="dialogue7phrase1.1.1.1.1.2.1.1.1.2"
            self.repliques = ["dialogue7reponse1.1.1.1.1.2.1.1.1.2.1"]

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
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue-1reponse1.1.1.2":
            self.controleur.set_phase(AGISSANT_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.2":
            self.controleur.set_phase(CASE_DIALOGUE)
        elif replique == "dialogue-1reponse1.1.3":
            self.replique = "dialogue-1phrase1.1.3"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")
            self.mouvement = 1
        elif replique == "dialogue-1reponse1.4":
            self.end_dialogue(-1)
        elif replique == "dialogue-1reponse1.2":
            self.replique = "dialogue-1phrase1.2"
            self.repliques = ["dialogue-1reponse1.2.1"]
        elif replique == "dialogue-1reponse1.2.1":
            self.end_dialogue(-1)
        elif replique == "dialogue-1reponse1.3":
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.replique = "dialogue-1phrase1.3"
                self.repliques = ["dialogue-1reponse1.3.1"]
            else:
                self.replique = "dialogue-1phrase1.3refus"
                self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.4"]
        elif replique == "dialogue-1reponse1.3.1":
            self.controleur.set_phase(IMPREGNATION)

        else:
            self.end_dialogue(self.dialogue)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def set_cible(self,cible:int|Position):

        self.cible_deplacement = cible
        self.replique = "dialogue-1phrase1.1.1.2"
        self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
        if self.controleur.joueur.inventaire.a_parchemin_vierge():
            self.repliques.append("dialogue-1reponse1.3")
        self.repliques.append("dialogue-1reponse1.4")

    def get_replique(self,code:str):
        return REPLIQUES_PEUREUSE[code]

    def get_skin_tete(self):
        return SKIN_TETE_PEUREUSE

    def get_texte_descriptif(self):
        return [f"Une humaine (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Une humaine terrorisée par les monstres. Elle peut quand-même se rendre utile."]

# Imports utilisés dans le code:
from Old_Jeu.Constantes import *
from Old_Jeu.Systeme.Constantes_magies.Magies import *
from Old_Affichage.Skins.Skins import SKIN_TETE_PEUREUSE
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT
from Old_Jeu.Dialogues.Dialogues_peureuse import REPLIQUES_PEUREUSE