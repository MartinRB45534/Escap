from Jeu.Entitees.Agissant.Humain.Humain import *

class Peste(Multi_soigneur,Support_lointain,Humain): #La huitième humaine du jeu, à l'étage 7 (une sainte très à cheval sur beaucoup trop de trucs)
    """La classe de la peste."""
    def __init__(self,controleur,position):

        self.identite = 'peste'
        self.place = 7

        Humain.__init__(self,controleur,position,self.identite,1,8) #Très bonne soigneuse, accessoirement

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

    def fuite(self,degats=0):
        #On fuit si on est en danger (pv trop bas)
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.1 + 0.01*self.appreciations[7] #Quand on se hait, on devient plus suicidaire
        return (self.pv-degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir et ne pas fuir si on n'est pas à portée de monstre

    def attaque(self,direction):
        #Quelle est sa magie de prédilection ? Pour l'instant on va prendre l'avalanche
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        if self.peut_payer(cout_pm_avalanche[skill.niveau-1]):
            self.skill_courant = Skill_magie
            self.magie_courante = "magie purification" #/!\
            self.dir_magie = direction
        else:
            self.skill_courant = Skill_stomp

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.entitees[2].a_parchemin_vierge():
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

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "dialogue1reponse1.1":
            self.replique="dialogue1phrase1.1"
            self.repliques = ["dialogue1reponse1.1.1","dialogue1reponse1.1.2"]
        elif replique == "dialogue1reponse1.1.1":
            self.replique="dialogue1phrase1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1","dialogue1reponse1.1.1.2"]
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
        elif replique == "dialogue1reponse1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1"]
        elif replique in ["dialogue1reponse1.1.1.1.1","dialogue1reponse1.1.1.2","dialogue1reponse1.1.2.1.2","dialogue1reponse1.2.1.1.1.1"]:
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "dialogue1reponse1.1.2":
            self.appreciations[0] -= 0.5
            self.replique="dialogue1phrase1.1.2"
            self.repliques = ["dialogue1reponse1.1.2.1","dialogue1reponse1.1.2.2"]
        elif replique == "dialogue1reponse1.1.2.1":
            self.replique="dialogue1phrase1.1.2.1"
            self.repliques = ["dialogue1reponse1.1.2.1.1","dialogue1reponse1.1.2.1.2"]
        elif replique in ["dialogue1reponse1.1.2.1.1","dialogue1reponse1.2.1.1.2","dialogue1reponse1.2.2.1"]:
            self.end_dialogue(-2)
            self.statut_humain = "exploration"
        elif replique == "dialogue1reponse1.1.2.2":
            self.end_dialogue(-3)
            self.statut_humain = "exploration"
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
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
        elif replique == "dialogue1reponse1.2.2":
            self.replique="dialogue1phrase1.2.2"
            self.repliques = ["dialogue1reponse1.2.2.1"]

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.replique="dialogue-2phrase1.1"
            self.repliques = ["dialogue-2reponse1.1"]
        elif replique == "dialogue-2reponse1.1":
            self.end_dialogue(-4)
            self.offenses.append([2,0.01,0])
            self.statut_humain = "exploration"
            self.attente = False
        elif replique == "dialogue-2reponse1.2":
            self.replique="dialogue-2phrase1.2"
            self.repliques = ["dialogue-2reponse1.2.1"]
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
        elif replique == "dialogue-2reponse1.2.1":
            self.end_dialogue()
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False

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
            if self.controleur.entitees[2].a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
        elif replique == "dialogue-1reponse1.1.1.2":
            self.controleur.get_entitee(2).start_select_agissant_dialogue()
            self.controleur.get_entitee(2).event = COMPLEMENT_DIALOGUE
        elif replique == "dialogue-1reponse1.1.2":
            self.controleur.get_entitee(2).start_select_case_dialogue()
            self.controleur.get_entitee(2).event = COMPLEMENT_DIALOGUE
        elif replique == "dialogue-1reponse1.1.3":
            self.replique = "dialogue-1phrase1.1.3"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.entitees[2].a_parchemin_vierge():
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
            if self.controleur.entitees[2].consomme_parchemin_vierge():
                self.replique = "dialogue-1phrase1.3"
                self.repliques = ["dialogue-1reponse1.3.1"]
            else:
                self.replique = "dialogue-1phrase1.3refus"
                self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.4"]
        elif replique == "dialogue-1reponse1.3.1":
            joueur = self.controleur.get_entitee(2)
            joueur.methode_fin = joueur.fin_menu_impregnation
            skill = trouve_skill(self.classe_principale,Skill_magie)
            joueur.options_menu = skill.menu_magie()
            joueur.start_menu()

        else:
            self.end_dialogue(self.dialogue)
            print("Je ne connais pas cette réplique !")

        self.replique_courante = 0

    def set_cible(self,cible):
        self.cible_deplacement = cible
        self.replique = "dialogue-1phrase1.1.1.2"
        self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
        if self.controleur.entitees[2].a_parchemin_vierge():
            self.repliques.append("dialogue-1reponse1.3")
        self.repliques.append("dialogue-1reponse1.4")

    def get_replique(self,code):
        return REPLIQUES_PESTE[code]

    def impregne(self,nom):
        skill = trouve_skill(self.classe_principale,Skill_magie)
        latence,magie = skill.utilise(nom)
        self.latence += latence
        cout = magie.cout_pm
        if self.peut_payer(cout):
            self.controleur.unset_phase(COMPLEMENT_MENU)
            self.methode_courante = None
            self.methode_fin = None
            self.paye(cout)
            parch = Parchemin_impregne(None,magie,cout//2)
            self.controleur.ajoute_entitee(parch)
            self.controleur.get_entitee(2).inventaire.ajoute(parch)
            self.replique = "dialogue-1phrase1.3.1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
            if self.controleur.entitees[2].a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")
        else:
            parch = Parchemin_vierge(None)
            self.controleur.ajoute_entitee(parch)
            self.controleur.get_entitee(2).inventaire.ajoute(parch)
            self.replique = "dialogue-1phrase1.3.1echec"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.4"]

    def get_skin_tete(self):
        return SKIN_TETE_PESTE

    def get_texte_descriptif(self):
        return [f"Une humaine (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Une sainte envoyée par son église pour purifier les monstres du labyrinthe."]
