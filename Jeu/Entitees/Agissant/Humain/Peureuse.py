from Jeu.Entitees.Agissant.Humain.Humain import *

class Peureuse(Multi_renforceur,Support_lointain,Stratege,Humain): #La quatrième humaine du jeu, à l'étage 3 (terrorisée par les monstres)
    """La classe de la peureuse."""
    def __init__(self,controleur,position):

        self.identite = 'peureuse'
        self.place = 3

        Humain.__init__(self,controleur,position,self.identite,1,5) #Plutôt faible, de base

        self.comportement_corps_a_corps = 2
        self.comportement_distance = 2
        self.antagonise_offensifs = False

        self.appreciations = [1,1,0,-1,0,9,1,6,-1,-1]
        self.dialogue = 1

        self.resolution = 4 #Permet aux humains de passer partout

        #Est-ce qu'elle a un minimum d'équippement ?

        #Peut recevoir l'ordre : d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self,degats=0):
        #On fuit si on est en danger (pv trop bas) ou en présence d'un monstre à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.7 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return (self.pv-degats) / self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : fuire dès qu'il y a un monstre en vue et accessible
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "dialogue-1phrase1"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
            if self.controleur.entitees[2].a_parchemin_vierge():
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

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

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
            self.appreciations[0] += 0.5
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "dialogue1reponse1.1.1.2":
            self.replique="dialogue1phrase1.1.1.2"
            self.repliques = ["dialogue1reponse1.1.1.2.1","dialogue1reponse1.1.1.2.2"]
        elif replique == "dialogue1reponse1.1.1.2.1":
            self.replique="dialogue1phrase1.1.1.2.1"
            self.repliques = "dialogue1reponse1.1.1.2.1.1","dialogue1reponse1.1.1.2.1.2"
        elif replique in ["dialogue1reponse1.1.1.1.1","dialogue1reponse1.1.1.2.1.2"]:
            self.replique="dialogue1phrase1.1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1.1","dialogue1reponse1.1.1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1.1.1":
            self.replique="dialogue1phrase1.1.1.1.1.1"
            self.repliques = ["dialogue1reponse1.1.1.1.1.2"]
        elif replique == "dialogue1reponse1.1.1.1.1.2":
            self.replique="dialogue1phrase1.1.1.1.1.2"
            self.repliques = ["dialogue1reponse1.1.1.1.1.2.1","dialogue1reponse1.1.1.1.1.2.2"]
        elif replique == "dialogue1reponse1.1.1.1.1.2.1":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "dialogue1reponse1.1.1.1.1.2.2":
            self.appreciations[0]-= 0.5
            self.end_dialogue(-2)
            self.statut_humain = "exploration"
        elif replique == "dialogue1reponse1.1.1.2.2":
            self.appreciations[0]-= 0.5
            self.end_dialogue(-2)
            self.statut_humain = "exploration"
        elif replique == "dialogue1reponse1.2":
            self.replique="dialogue1phrase1.2"
            self.repliques = ["dialogue1reponse1.2.1","dialogue1reponse1.2.2"]
        elif replique == "dialogue1reponse1.2.2":
            self.replique="dialogue1phrase1.2.2"
            self.repliques = ["dialogue1reponse1.2.1"]

        #Dialogue par défaut -2
        elif replique == "dialogue-2reponse1.1":
            self.end_dialogue(-2)
            self.statut_humain = "exploration"

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
            self.appreciations[0]+= 0.1
            self.end_dialogue()
        elif replique == "dialogue3reponse1.1.1.2":
            self.appreciations[0]-= 0.3
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
            self.appreciations[0]+= 0.5
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
            self.appreciations[0]+=0.5
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
            self.appreciations[0]-= 0.3

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
            ID_clee = self.inventaire.get_clee("Porte_avant_prison_5")
            self.inventaire.drop(None,ID_clee)
            self.controleur.entitees[2].inventaire.ramasse_item(ID_clee) #On refile au joueur la clé dont il a besoin
            self.replique="dialogue5phrase1.1.1.1"
            self.repliques = ["dialogue5reponse1.1.1.1.1"]
        elif replique == "dialogue5reponse1.1.1.1.1":
            self.end_dialogue()
        elif replique == "dialogue5reponse1.2":
            ID_clee = self.inventaire.get_clee("Porte_avant_prison_5")
            self.inventaire.drop(None,ID_clee)
            self.controleur.entitees[2].inventaire.ramasse_item(ID_clee) #On refile quand même au joueur la clé dont il a besoin
            self.appreciations[0]+= 0.5
            self.end_dialogue()
        elif replique == "dialogue5reponse1.3":
            ID_clee = self.inventaire.get_clee("Porte_avant_prison_5")
            self.inventaire.drop(None,ID_clee)
            self.controleur.entitees[2].inventaire.ramasse_item(ID_clee) #On refile quand même au joueur la clé dont il a besoin
            self.appreciations[0]-= 0.5
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
            self.appreciations[0]+= 0.5
            self.end_dialogue()
        elif replique == "dialogue6reponse1.3":
            self.appreciations[0]-= 0.5
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
            self.appreciations[0] -= 0.2
        elif replique == "dialogue7reponse1.1.1":
            self.replique="dialogue7phrase1.1.1"
            self.repliques = ["dialogue7reponse1.1.1.1","dialogue7reponse1.1.1.2"]
        elif replique == "dialogue7reponse1.1.2":
            self.replique="dialogue7phrase1.1.2"
            self.repliques = ["dialogue7reponse1.1.2.1"]
        elif replique == "dialogue7reponse1.1.3":
            self.appreciations[0] -= 0.1
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
            self.appreciations[0] -= 0.1
            self.replique="dialogue7phrase1.1.3.1"
            self.repliques = ["dialogue7reponse1.1.1.1.1","dialogue7reponse1.1.1.1.2"]
        elif replique == "dialogue7reponse1.1.3.2":
            self.end_dialogue()
            self.appreciations[0] -= 0.2
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
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
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
        return REPLIQUES_PEUREUSE[code]

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
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
            if self.controleur.entitees[2].a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
        else:
            parch = Parchemin_vierge(None)
            self.controleur.ajoute_entitee(parch)
            self.controleur.get_entitee(2).inventaire.ajoute(parch)
            self.replique = "dialogue-1phrase1.3.1echec"
            self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
            if self.controleur.entitees[2].a_parchemin_vierge():
                self.repliques.append("dialogue-1reponse1.3")
            self.repliques.append("dialogue-1reponse1.4")

    def get_skin_tete(self):
        return SKIN_TETE_PEUREUSE

    def get_texte_descriptif(self):
        return [f"Une humaine (niveau {self.niveau})",f"ID : {self.ID}","Nom : ???","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Une humaine terrorisée par les monstres. Elle peut quand-même se rendre utile."]
