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
from Old_Jeu.Entitee.Agissant.Role.Multi_soigneur import Multi_soigneur
from Old_Jeu.Entitee.Agissant.Role.Support_lointain import Support_lointain
from Old_Jeu.Entitee.Agissant.Role.Attaquant_magique_poing import Attaquant_magique_poing

class Peste(PNJ_mage,Multi_soigneur,Attaquant_magique_poing,Support_lointain,Humain): #La huitième humaine du jeu, à l'étage 7 (une sainte très à cheval sur beaucoup trop de trucs)
    """La classe de la peste."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'peste'
        self.place = 7

        Humain.__init__(self,controleur,self.identite,1,8,position) #Très bonne soigneuse, accessoirement

        self.comportement_corps_a_corps = 2
        self.comportement_distance = 2
        self.antagonise_neutre = True

        self.appreciations = [1,-1,-2,-2,0,-3,-1,9,-4,-1]
        self.dialogue = 1

        #Penser à l'équipper

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats:float=0):
        #On fuit si on est en danger (pv trop bas)
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.1 + 0.01*self.appreciations[7] #Quand on se hait, on devient plus suicidaire
        return (self.pv+degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir et ne pas fuir si on n'est pas à portée de monstre

    def peut_caster(self):
        return self.peut_payer(cout_pm_soin[self.get_skill_magique().niveau-1])

    def caste(self):
        return "magie soin"

    def peut_multi_caster(self):
        return self.peut_payer(cout_pm_multi_soin[self.get_skill_magique().niveau-1])

    def multi_caste(self):
        return "magie multi soin"
    
    def peut_frapper(self):
        return self.peut_payer(cout_pm_purification[self.get_skill_magique().niveau-1])
    
    def frappe(self):
        return "magie purification"

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
        elif self.dialogue == -2: #Le joueur veut se débrouiller seul
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1","dialogue-2reponse1.2"]
        elif self.dialogue == -3: #Le joueur ne veut pas tuer tous les monstres
            self.replique = "dialogue-3phrase1"
            self.repliques = ["dialogue-3reponse1.1"]
        elif self.dialogue == -4:
            self.replique = "dialogue-4phrase1"
            self.repliques = ["dialogue-4reponse1.1"]
        elif self.dialogue == 1:
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1","dialogue1reponse1.2"]

    def interprete(self,replique:str):
        assert isinstance(self.controleur.joueur, Humain)

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "dialogue1reponse1.1":
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1","dialogue1reponse1.1.2"]
        elif replique == "dialogue1reponse1.1.1":
            self.replique="dialogue1phrase1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2"]
            self.controleur.joueur.esprit.merge(self.esprit)
        elif replique == "dialogue1reponse1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1"]
        elif replique in ["dialogue1reponse1.1.1.1.1","dialogue1reponse1.1.1.2","dialogue1reponse1.1.2.1.2","dialogue1reponse1.2.1.1.1.1"]:
            self.end_dialogue()
            self.controleur.joueur.esprit.merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur
        elif replique == "dialogue1reponse1.1.2":
            self.appreciations[self.controleur.joueur.place] -= 0.5
            self.replique="dialogue1phrase1.1.2"
            self.repliques = ["dialogue1reponse1.1.2.1","dialogue1reponse1.1.2.2"]
        elif replique == "dialogue1reponse1.1.2.1":
            self.replique="dialogue1phrase1.1.2.1"
            self.repliques = ["dialogue1reponse1.1.2.1.1","dialogue1reponse1.1.2.1.2"]
        elif replique in ["dialogue1reponse1.1.2.1.1","dialogue1reponse1.2.1.1.2","dialogue1reponse1.2.2.1"]:
            self.end_dialogue(-2)
            self.statut_pnj = "exploration"
        elif replique == "dialogue1reponse1.1.2.2":
            self.end_dialogue(-3)
            self.statut_pnj = "exploration"
        elif replique == "dialogue1reponse1.2":
            self.replique="dialogue1phrase1.2"
            self.repliques = ["dialogue1reponse1.2.1","dialogue1reponse1.2.2"]
        elif replique == "dialogue1reponse1.2.1":
            self.replique="dialogue1phrase1.2.1"
            self.repliques = ["dialogue1reponse1.2.1.1"]
        elif replique == "dialogue1reponse1.2.1.1":
            self.replique="dialogue1phrase1.2.1.1"
            self.repliques = ["dialogue1reponse1.2.1.1.1","dialogue1reponse1.2.1.1.2"]
        elif replique == "dialogue1reponse1.2.1.1.1":
            self.replique="dialogue1phrase1.2.1.1.1"
            self.repliques = ["dialogue1reponse1.2.1.1.1.1"]
            self.controleur.joueur.esprit.merge(self.esprit)
        elif replique == "dialogue1reponse1.2.2":
            self.replique="dialogue1phrase1.2.2"
            self.repliques = ["dialogue1reponse1.2.2.1"]

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.replique="dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1"]
        elif replique == "dialogue-2reponse1.1":
            self.end_dialogue(-4)
            self.offenses.append((self.controleur.joueur,0.01,0))
            self.statut_pnj = "exploration"
        elif replique == "dialogue-2reponse1.2":
            self.replique="dialogue-2phrase1.2"
            self.repliques = ["dialogue-2reponse1.2.1"]
            self.controleur.joueur.esprit.merge(self.esprit)
        elif replique == "dialogue-2reponse1.2.1":
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = self.controleur.joueur

        #Dialogue par défaut -3
        elif replique == "dialogue-3reponse1.1":
            self.end_dialogue(-3)

        #Dialogue par défaut -4
        elif replique == "dialogue-4reponse1.1":
            self.end_dialogue(-4)

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
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
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
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
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
        return REPLIQUES_PESTE[code]

    def get_skin_tete(self):
        return SKIN_TETE_PESTE

    def get_texte_descriptif(self):
        return [f"Une humaine (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Une sainte envoyée par son église pour purifier les monstres du labyrinthe."]

# Imports utilisés dans le code:
from Old_Jeu.Constantes import *
from Old_Jeu.Systeme.Constantes_magies.Magies import *
from Old_Affichage.Skins.Skins import SKIN_TETE_PESTE
from Old_Jeu.Dialogues.Dialogues_peste import REPLIQUES_PESTE