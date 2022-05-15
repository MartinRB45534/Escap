from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Controleur import Controleur

from Jeu.Entitee.Agissant.Humain.Humain import *

class Bombe_atomique(Attaquant_magique_case,Support,Humain): #La neuvième humaine du jeu, à l'étage 8 (une magicienne légèrement aguicheuse)
    """La classe de la bombe atomique."""
    def __init__(self,controleur:Controleur,position:Position):

        self.identite = 'bombe_atomique'
        self.place = 8

        Humain.__init__(self,controleur,position,self.identite,1,9) #Ses magies sont littéralement explosives !

        self.comportement_corps_a_corps = 2 #0 pour attaquer, 1 pour ignorer, 2 pour fuir
        self.comportement_distance = 1 #0 pour foncer dans le tas, 1 pour tenter une attaque à distance puis se rapprocher, 2 pour tenter une attaque à distance puis fuir, 3 pour fuir puis tenter une attaque à distance
        self.antagonise_offensifs = True #Si True, sera offensé par les neutres qui veulent l'attaquer

        self.appreciations = [3,-1,1,-1,0,2,1,-1,3,0]
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
        #On fuit si on est en danger (pv trop bas) ou en présence d'un monstre à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.5 + 0.01*self.appreciations[8] #Quand on se hait, on devient plus suicidaire
        return (self.pv-degats) / self.pv_max <= taux_limite

    def peut_caster(self):
        return self.peut_payer(cout_pm_volcan[trouve_skill(self.classe_principale,Skill_magie).niveau-1])

    def caste(self):
        return "magie volcan"

    def attaque(self,direction:Direction):
        #Quelle est sa magie de prédilection ? Pour l'instant on va prendre l'avalanche
        if self.peut_payer(cout_pm_poing_ardent[trouve_skill(self.classe_principale,Skill_magie).niveau-1]):
            self.skill_courant = Skill_magie
            self.magie_courante = "magie poing ardent"
        else:
            self.skill_courant = Skill_stomp
        self.statut = "attaque"

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.joueur.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
        elif self.dialogue == -2:
            self.replique = "dialogue-2phrase1"
            self.repliques = ["dialogue-2reponse1.1","dialogue-2reponse1.2"]
        elif self.dialogue == -3:
            self.replique = "dialogue-3phrase1"
            self.repliques = ["dialogue-3reponse1.1"]
        elif self.dialogue == 1:
            self.replique = "dialogue1phrase1"
            self.repliques = ["dialogue1reponse1.1","dialogue1reponse1.2"]

    def interprete(self,replique:str):

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "dialogue1reponse1.1":
            self.appreciations[0] += 0.5
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1","dialogue1reponse1.1.2"]
        elif replique == "dialogue1reponse1.1.1":
            self.replique="dialogue1phrase1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2"]
        elif replique in ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.2.1","dialogue1reponse1.1.3.1.1","dialogue1reponse1.1.4.1.1","dialogue1reponse1.1.4.2.2","dialogue1reponse1.2.1.1.1","dialogue1reponse1.2.2.2.2"]:
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.joueur.esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "dialogue1reponse1.1.1.2":
            self.end_dialogue(-2)
            self.statut_humain = "exploration"
        elif replique == "dialogue1reponse1.1.2":
            self.appreciations[0] += 0.5
            self.replique="dialogue1phrase1.1.2"
            self.repliques = ["dialogue1reponse1.1.2.1","dialogue1reponse1.1.1.2"]
        elif replique == "dialogue1reponse1.2":
            self.replique="dialogue1phrase1.2"
            self.repliques = ["dialogue1reponse1.2.1","dialogue1reponse1.2.2"]
        elif replique == "dialogue1reponse1.2.1":
            self.replique="dialogue1phrase1.2.1"
            self.repliques = ["dialogue1reponse1.2.1.1","dialogue1reponse1.2.1.2"]
        elif replique == "dialogue1reponse1.2.1.1":
            self.replique="dialogue1phrase1.2.1.1"
            self.repliques = ["dialogue1reponse1.2.1.1.1"]
            self.controleur.get_esprit(self.controleur.joueur.esprit).merge(self.esprit)
        elif replique == "dialogue1reponse1.2.1.2":
            self.end_dialogue(-2)
            self.statut_humain = "exploration"
        elif replique == "dialogue1reponse1.2.2":
            self.replique="dialogue1phrase1.2.2"
            self.repliques = ["dialogue1reponse1.2.2.1","dialogue1reponse1.2.2.2"]
        elif replique == "dialogue1reponse1.2.2.1":
            self.replique="dialogue1phrase1.2.2.1"
            self.repliques = ["dialogue1reponse1.2.2.1.1"]
            self.controleur.get_esprit(self.controleur.joueur.esprit).merge(self.esprit)
        elif replique == "dialogue1reponse1.2.2.2":
            self.replique="dialogue1phrase1.2.2.2"
            self.repliques = ["dialogue1reponse1.2.2.2.1","dialogue1reponse1.2.2.2.2"]
        elif replique == "dialogue1reponse1.2.2.2.1":
            self.replique="dialogue1phrase1.2.2.2.1"
            self.repliques = ["dialogue1reponse1.2.2.2.1.1"]
        elif replique == "dialogue1reponse1.2.2.2.1.1":
            self.end_dialogue(-3)
            self.offenses.append([2,0.01,0])
            self.statut_humain = "exploration"
            self.attente = False

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.replique="dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1.1"]
        elif replique == "dialogue-2reponse1.1.1":
            self.appreciations[0] -= 0.5
            self.end_dialogue()
        elif replique == "dialogue-2reponse1.2":
            self.end_dialogue(-2)

        #Dialogue par défaut -3
        elif replique == "dialogue-3reponse1.1":
            self.replique = "dialogue-3phrase1.1"
            self.repliques = ["dialogue-3reponse1.1.1"]
        elif replique == "dialogue-3reponse1.1.1":
            self.end_dialogue(-3)

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
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
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
        elif replique == "dialogue-1reponse1.4":
            self.end_dialogue(-1)

        else:
            self.end_dialogue(self.dialogue)
            print(replique)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def set_cible(self,cible:Union[int,Position]):
        self.cible_deplacement = cible
        self.replique = "dialogue-1phrase1.1.1.2"
        self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
        if self.controleur.joueur.inventaire.a_parchemin_vierge():
            self.repliques.append("dialogue-1reponse1.3")
        self.repliques.append("dialogue-1reponse1.4")

    def get_replique(self,code:str):
        return REPLIQUES_BOMBE_ATOMIQUE[code]

    def impregne(self,nom:str):
        skill = trouve_skill(self.classe_principale,Skill_magie)
        latence,magie = skill.utilise(nom)
        self.latence += latence
        cout = magie.cout_pm
        if self.peut_payer(cout):
            self.controleur.joueur.inventaire.consomme_parchemin_vierge()
            self.paye(cout)
            parch = Parchemin_impregne(None,magie,cout//2)
            self.controleur.ajoute_entitee(parch)
            self.controleur.joueur.inventaire.ajoute(parch)
            self.replique = "dialogue-1phrase1.3.1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.joueur.inventaire.a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")
        else:
            self.replique = "dialogue-1phrase1.3.1echec"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3","dialogue-1reponse1.4"]

    def get_skin_tete(self):
        return SKIN_TETE_BOMBE_ATOMIQUE

    def get_texte_descriptif(self):
        return [f"Une humaine (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Une aventurière magicienne. Spécialisée dans les sorts de feu."]
