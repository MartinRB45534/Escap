from Jeu.Entitee.Agissant.Agissants import *
from Jeu.Esprit.Representation_spatiale import *

from typing import Dict, Literal
import operator

class Esprit :
    """La classe des esprits, qui manipulent les agisants."""
    def __init__(self,nom:str): #On identifie les esprits par des noms (en fait on s'en fout, vu qu'on ne fait pas d'opérations dessus on pourrait avoir des labs, des entitees et des esprits nommés avec des str, des int, des float, des bool, etc.)
        self.corps:Dict[int,str] = {}
        self.vue = Vues()
        self.ennemis:Dict[int,List[float]] = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.oubli = 1
        self.resolution = 0 #0 pour se déplacer normalement, 1 pour passer les portes dont on a les clés, 2 pour traverser les portails, 3 pour passer les protes et les portails, 4 pour passer partout (portes, portails, changer d'étage)
        self.nom = nom
        self.controleur:Controleur = None

    def ajoute_corp(self,corp:int):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            self.controleur[corp].rejoint(self.nom)

    def ajoute_corps(self,corps:List[int]):
        for corp in corps:
            self.ajoute_corp(corp)

    def retire_corp(self,corp:int):
        if corp in self.corps:
            self.corps.pop(corp)

    def retire_corps(self,corps:List[int]):
        for corp in corps:
            self.retire_corp(corp)

    def get_corps(self):
        corps:List[int] = []
        for corp in self.corps.keys():
            corps.append(corp)
        return corps

    def get_importance(self,position:Position):
        importance = 0
        if position in self.vue:
            case = self.vue[position]
            for ID in case[6]:
                if self.controleur[ID].etat == "vivant":
                    if ID in self.ennemis:
                        new_importance = self.ennemis[ID][0]
                        if new_importance > importance:
                            importance = new_importance
        return importance

    def ajoute_vue(self,vue:Vue): #Indiquer les cases nouvellement vues
        self.vue[vue.id] = vue
        nouvelles_cases = []
        for decalage in vue.decalage:
            case = vue[decalage]
            if case[1] > 0:
                nouvelles_cases.append(case[0])
        return nouvelles_cases

    def maj_vue(self,vue:Vue): #Indiquer les cases nouvellement vues
        nouvelles_cases = []
        for decalage in vue.decalage:
            case = vue[decalage]
            if case[1] > 0 and not self.vue[case[0]][1]: #/!\ Réduire ça proprement
                nouvelles_cases.append(case[0])
            if case[1] > 0: #Si la clarté est positive
                case[2] = self.oubli
                self.vue[case[0]] = case #On remplace par la dernière version de la vision
        return nouvelles_cases

    def trouve_agissants_vue(self,vue:Vue):
        agissants = []
        for decalage in vue.decalage:
            case = vue[decalage]
            agissants += case[6]
        return agissants

    def trouve_agissants(self):
        agissants = []
        for case in self.vue:
            agissants += case[6]
        return sorted(agissants)

    def get_corps_vus(self):
        corps = []
        for agissant in self.trouve_agissants():
            if agissant in self.corps.keys() and self.controleur.est_agissant(agissant):
                corps.append(agissant)
        return corps

    def get_ennemis_vus(self):
        ennemis = []
        for agissant in self.trouve_agissants():
            if agissant in self.ennemis.keys() and self.controleur.est_agissant(agissant):
                ennemis.append(agissant)
        return ennemis

    def get_neutres_vus(self):
        neutres = []
        for agissant in self.trouve_agissants():
            if agissant not in self.corps.keys() and agissant not in self.ennemis.keys() and self.controleur.est_agissant(agissant):
                neutres.append(agissant)
        return neutres

    def oublie_agissants(self,agissants:List[int]):
        for case in self.vue:
            for ID in agissants:
                if ID in case[6]:
                    case[6].remove(ID)

    def refait_vue(self):
        vues:List[Vue] = []
        agissants_vus:List[int] = []
        for corp in self.corps.keys(): #On récupère les vues
            if self.corps[corp] != "incapacite":
                agissant:Agissant = self.controleur[corp]
                vues.append(agissant.vue)
                agissants_vus += self.trouve_agissants_vue(agissant.vue)
        self.oublie_agissants(agissants_vus) #Puisqu'on les a vus, on n'a plus besoin de garder en mémoire leur position précédente. /!\ À modifier plus tard
        for ID_agissant in agissants_vus:
            if not(ID_agissant in self.ennemis.keys() or ID_agissant in self.corps.keys()):
                for espece in self.controleur.get_especes(ID_agissant):
                    if espece in self.prejuges:
                        self.ennemis[ID_agissant] = [0.01,0]
        nouvelles_cases = []
        for vue in vues :
            if vue.id in self.vue.keys(): 
                nouvelles_cases+=self.maj_vue(vue)
            else:
                nouvelles_cases+=self.ajoute_vue(vue)
        nouvelles_cases = [*set(nouvelles_cases)] #Pour retirer les doublons
        # update_representation(nouvelles_cases)

    def update_representation(self,cases):
        carres_pot = []
        for case in cases:
            for dec in Decalage(1,1):
                carres_pot.append(case-dec)
        pass

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant:Agissant = self.controleur[corp]
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                self.antagonise_attaquant(offense)
                self.antagonise_supports(offense)
        
    def antagonise_attaquant(self,offense):
        ID_offenseur:int = offense[0]
        gravite:float = offense[1]
        degats:float = offense[2]
        if ID_offenseur in self.ennemis:
            self.ennemis[ID_offenseur][0] += gravite
            if self.ennemis[ID_offenseur][1] < degats:
                self.ennemis[ID_offenseur][1] = degats
        else:
            self.ennemis[ID_offenseur] = [gravite,degats]

    def antagonise_supports(self,offense):
        pass

    def get_pos_vues(self):
        positions = []
        for corp in self.corps.keys():
            if self.corps[corp] != "incapacite":
                agissant = self.controleur[corp]
                positions.append(agissant.position)
        return positions

    def trouve_strateges(self):
        # On détermine comment on va réfléchir (en fonction des stratèges qu'on a)
        # (Pour l'instant juste pour la traversée des portes, portails, escaliers)
        self.resolution = 0
        for ID_corp in self.corps.keys():
            corp = self.controleur[ID_corp]
            if isinstance(corp,Stratege): # Comment faire quand on a plusieurs stratèges ? /!\
                self.resolution = corp.resolution

    def calcule_trajets(self):
        # On détermine la dangerosité de chaque case en fonction des dégats qui vont y avoir lieu
        coef=7 #/!\ Expérimenter avec ce coef à l'occasion
        for case in self.vue:
            for effet in case[7]:
                dangerosite = coef*effet[2]/(effet[1]+coef)
                case[3][2] += dangerosite
                case[3][3] += dangerosite

        # On modifie légèrement pour pouvoir sortir des zones concernées
        coef_croissant = 1.1
        # On commence par trouver les seuils, vers lesquels on va vouloir aller
        seuils = self.trouve_seuils(self.get_pos_vues()) # On part des différents endroit d'où l'on voit, qui devraient théoriquement nous donner accès à toute notre vision
        self.propage(seuils,coef_croissant,3,False,-1) # On propage de façon croissante à partir des seuils (à l'intérieur)
        self.propage(seuils,coef_croissant,2,True,-1) # On propage de façon croissante à partir des seuils (à l'intérieur), en contournant les obstacles

        # On rajoute les ennemis
        coef_importance = 0.9
        coef_dangerosite = 0.9
        dangerosites = seuils
        importances = []
        for ID_ennemi in self.ennemis.keys():
            ennemi = self.controleur[ID_ennemi]
            if ennemi.etat == "vivant":
                position = ennemi.get_position()
                if position.lab in self.vue.keys():
                    importance = self.ennemis[ID_ennemi][0]
                    dangerosite = self.ennemis[ID_ennemi][1]
                    if importance > self.vue[position][3][0]:
                        self.vue[position][3][0]=importance
                        self.vue[position][3][1]=importance
                        importances.append(position)
                    if dangerosite > self.vue[position][3][2]:
                        self.vue[position][3][2]=dangerosite
                        if not position in dangerosites: # On peut avoir des doublons (ennemis sur les seuils par exemple)
                            dangerosites.append(position)
                    if dangerosite > self.vue[position][3][3]:
                        self.vue[position][3][3]=dangerosite
                        if not position in dangerosites:
                            dangerosites.append(position)
        # On propage l'importance de façon décroissante à partir des ennemis
        self.propage(importances,coef_importance) #Traversée
        self.propage(importances,coef_importance,0,True) #Contournement (<= Traversée)
        # On propage la dangerosité de façon décroissante à partir des ennemis et des seuils
        self.propage(dangerosites,coef_dangerosite,3) #Traversée
        self.propage(dangerosites,coef_dangerosite,2,True) #Contournement

        # /!\ Prendre aussi en compte les alliés, et les cases inconnues (mais on va déjà tester ça)

    def resoud(self,position:Position,portee:int,indice=1,dead_ends=False):
        """'Résoud' un labyrinthe à partir d'une case donnée."""

        if indice == 4:
            for case in self.vue:
                case[3][4] = 0

        #la queue est une liste de positions
        queue=[position]

        if position in self.vue:

            self.vue[position][3][indice] = portee

            arret_obstacle = False

            while len(queue)!=0 :

                position = queue[0]

                clarte = self.vue[position][3][indice]*self.dispersion_spatiale
                #enlever position dans queue
                queue.pop(0)

                #trouver les positions explorables

                pos_explorables = self.positions_utilisables(position,arret_obstacle)

                arret_obstacle = dead_ends

                for pos in pos_explorables:
                    if clarte > self.vue[pos][3][indice]:
                        #on marque la case comme visitée
                        self.vue[pos][3][indice] = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(pos)

    def propage(self,positions:List[Position],coef,indice=1,dead_ends=False,comparateur=1):
        """'Résoud' un labyrinthe à partir de plusieurs points"""

        if indice == 4:
            for case in self.vue:
                case[3][4] = 0

        #la queue est une liste de positions
        queue = [position for position in positions]

        arret_obstacle = False

        departs = len(positions)

        while len(queue)!=0 :

            position = queue[0]

            valeur = self.vue[position][3][indice]*coef
            #enlever position dans queue
            queue.pop(0)

            #trouver les positions explorables

            if departs == 0:
                arret_obstacle = dead_ends
            else:
                departs -= 1

            pos_explorables = self.positions_utilisables(position,arret_obstacle)

            for pos in pos_explorables:
                if valeur*comparateur > self.vue[pos][3][indice]*comparateur:
                    #on marque la case comme visitée
                    self.vue[pos][3][indice] = valeur

                    #on ajoute toutes les directions explorables
                    queue.append(pos)

    def trouve_seuils(self,positions:List[Position],indice=2,dead_ends=False):
        """Fonction qui trouve les 'seuils', c'est à  dire les cases qui ont un valeur plus grande que leurs voisines"""

        for case in self.vue:
            case[3][5] = False

        seuils:List[Position] = []

        #la queue est une liste de positions
        queue = [position for position in positions]

        arret_obstacle = False

        departs = len(positions)

        while len(queue)!=0 :

            position = queue[0]
            #enlever position dans queue
            queue.pop(0)

            #trouver les positions explorables

            if departs == 0:
                arret_obstacle = dead_ends
            else:
                departs -= 1

            pos_explorables = self.positions_utilisables(position,arret_obstacle)

            for pos in pos_explorables:
                if self.vue[position][3][indice] > self.vue[pos][3][indice] and not position in seuils:
                    seuils.append(position)
                elif self.vue[position][3][indice] < self.vue[pos][3][indice] and not pos in seuils:
                    seuils.append(pos)
                if not self.vue[pos][3][5]:
                    #on marque la case comme visitée
                    self.vue[pos][3][5] = True
                        
                    #on ajoute toutes les directions explorables
                    queue.append(pos)
        return seuils

    def print_vue(self):
        for etage in self.vue.keys():
            matrice = self.vue[etage]
            print("Vue de l'esprit :")
            print(self.nom)
            for i in range(len(matrice)):
                haut = ""
                centre = ""
                bas = ""
                for j in range(len(matrice[0])):
                    case = matrice[i][j]
                    if case[1] == 0:
                        haut += " ~~~ "
                        centre += ": ? :"
                        bas += " ~~~ "
                    else:
                        haut+= " "
                        if case[5][0]:
                            haut += "   "
                        else:
                            haut += "---"
                        haut += " "
                        if case[5][3]:
                            centre += " "
                        else:
                            centre += "|"
                        if case[5] > 0:
                            centre += "x"
                        else:
                            centre += " "
                        if case[6] != []:
                            occ = " "
                            for occupant in case[6]:
                                if occupant in self.corps.keys():
                                    occ = "O"
                                elif occupant in self.ennemis.keys():
                                    occ = "X"
                            centre += occ
                        else:
                            centre += " "
                        if case[3][1] > 0:
                            centre += "x"
                        else:
                            centre += " "
                        if case[5][1]:
                            centre += " "
                        else:
                            centre += "|"
                        bas += " "
                        if case[5][2]:
                            bas += "   "
                        else:
                            bas += "---"
                        bas += " "
                print(haut)
                print(centre)
                print(bas)

    def positions_utilisables(self,position:Position,dead_ends:bool):
        pos_utilisables:List[Position]=[]

        case = self.vue[position]

        for direction in DIRECTIONS:
            if any(case[5][direction]) and not(dead_ends and case[6]!=[]) and case[5][direction][4].lab in self.vue.keys():
                pos_utilisables.append(case[5][direction][4])

        return pos_utilisables

    def antagonise(self,nom_esprit:str):
        for corp in self.controleur.get_esprit(nom_esprit).get_corps():
            if not corp in self.ennemis.keys():
                self.ennemis[corp] = [0.1,0]

    def decide(self):
        for corp in self.corps.keys():
            if corp != self.controleur.joueur and self.corps[corp] in ["attaque","fuite","soin","soutien"]:
                self.deplace(corp)

    def fuite_utile(self,ID:int):
        for corp in self.corps.keys():
            if corp != ID and self.corps[corp] not in ["fuite","incapacite","mort"]:
                return True
        return False

    def deplace(self,ID:int):
        corp:Agissant = self.controleur[ID]
        position = corp.position
        case = corp.vue[position]
        tcase = self.vue[position]
        repoussante = tcase[8]
        cases = [[-1,tcase[0],tcase[3][0],tcase[3][1],-tcase[3][2],tcase[3][2],-tcase[3][3],tcase[3][3]]]
        dirs = []
        importance = 0
        fuite = corp.veut_fuir(tcase[3][2])
        attaque = corp.veut_attaquer(tcase[3][2])
        res = "attente"
        for i in DIRECTIONS: #On commence par se renseigner sur les possibilités :
            mur:Union[Position,Literal[False]] = case[5][i][self.resolution]
            if mur:
                if mur in position and corp.vue[mur][1]>0:
                    case_pot = self.vue[mur]
                    entitees = case_pot[6]
                    libre = True #On n'y va pas pour s'en enfuir après
                    for ID_entitee in entitees:
                        entitee = self.controleur[ID_entitee]
                        if issubclass(entitee.get_classe(),Non_superposable): #On ne peut pas aller sur cette case
                            libre = False
                            if issubclass(entitee.get_classe(),Agissant): #Elle est occupée par un agissant
                                if ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                    if corp.peut_voir(i) and (attaque or (fuite and not self.fuite_utile(ID))) : #On veut attaquer lorsqu'on croise un ennemi au corps à corps (et on a assez de mana pour, si on utilise la magie)
                                        if self.ennemis[ID_entitee][0] > importance:
                                            importance = self.ennemis[ID_entitee][0]
                                            corp.attaque(i)
                                            res = "attaque"
                                    elif fuite and self.fuite_utile(ID): #On veut fuire lorsqu'on croise un ennemi au corps à corps
                                        res = "fuite"
                    if libre:
                        cases.append([i,case_pot[0],case_pot[3][0],case_pot[3][1],-case_pot[3][2],case_pot[3][2],-case_pot[3][3],case_pot[3][3]])
                        dirs.append(i)
        if res == "attente": #Quelques comportements possibles :
            comportement = corp.comporte_distance(tcase[3][2])
            if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                res = "deplacement"
            elif comportement == 1 or (comportement > 1 and not self.fuite_utile(ID)): #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                res = corp.agit_en_vue(self,"deplacement")
                if repoussante:
                    res = "deplacement"
            elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                res = corp.agit_en_vue(self,"fuite")
                if repoussante:
                    res = "fuite"
            elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                res = "fuite"
        if res in ["deplacement","fuite"] and corp.latence <= 0:
            if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                res = "bloqué"
                corp.skill_courant = None
                importance = 0
                for i in DIRECTIONS:
                    mur:Union[Position,Literal[False]] = case[5][i][self.resolution]
                    if mur:
                        if mur.lab in self.vue.keys():
                            case_pot = self.vue[mur]
                            entitees = case_pot[6]
                            for ID_entitee in entitees:
                                entitee = corp.controleur[ID_entitee]
                                if issubclass(entitee.get_classe(),Agissant): #Cette case est occupée par un agissant
                                    if corp.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                        if self.ennemis[ID_entitee][0] > importance:
                                            importance = self.ennemis[ID_entitee][0]
                                            corp.attaque(i)
                                            res = "attaque"
            elif tcase[3][1] == 0: #Et tcase[3] forcément aussi par la même occasion, donc on est totalement libre de chercher
                res = "paix"
                if not isinstance(corp,Sentinelle) or isinstance(corp,Humain) or repoussante:
                    res = "exploration"
                    if len(dirs)>1: #On peut se permettre de choisir
                        if corp.dir_regard != None: #L'agissant regarde quelque part
                            dir_back = corp.dir_regard+2
                            if dir_back in dirs: #On ne veut pas y retourner
                                dirs.remove(dir_back)
                    corp.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                    if ID == 4: # /!\ Ne pas nettoyer, c'est très utile par moment
                        constantes_deplacements.append([self.controleur.nb_tours,"cherche",corp.dir_regard,cases])
            else:
                if repoussante: #On ne veut pas rester en place
                    cases.pop(0)
                if res == "deplacement":
                    new_cases = sorted(cases,key=operator.itemgetter(2,3,4,6)) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    res = "approche"
                    if new_cases[-1][0] != -1: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                        corp.va(new_cases[-1][0])
                        if ID == 4:
                            constantes_deplacements.append([self.controleur.nb_tours,"deplacement",corp.dir_regard,new_cases])
                    else:
                        res = corp.agit_en_vue(self)
                elif res == "fuite":
                    new_cases = sorted(cases,key=operator.itemgetter(5,7,2,3)) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    if new_cases[0][0] != -1: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                        corp.va(new_cases[0][0])
                        if ID == 4:
                            constantes_deplacements.append([self.controleur.nb_tours,"fuite",corp.dir_regard,new_cases])
                    else:
                        res = corp.agit_en_vue(self)
        corp.statut = res

    def oublie(self): #/!\ Marquer les cases anciennement vues
        anciennes_cases = []
        for case in self.vue:
            if case[2] > 0:
                case[2] -= 1
            if case[2] <= 0:
                case[1] = 0
                case[4] = 0
                case[5] = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
                case[6] = []
                anciennes_cases.append(case[0])
            case[3] = [0,0,0,0,0,False]
            case[7] = []
            case[8] = False
        # downdate_representation(anciennes_cases)

    #Découvront le déroulé d'un tour avec esprit-sensei :
    def debut_tour(self):
        #On va faire plein de choses pendant ce tour (est-ce vraiment nécessaire de prendre des décisions si aucun des corps ne va jouer à ce tour ?
        self.get_offenses() #On s'insurge à grands cris (s'il y a lieu)
        self.refait_vue() #On prend connaissance de son environnement
        #Il faudra éventuellement définir une stratégie
        self.trouve_strateges()
        self.calcule_trajets() #On dresse les plans de bataille (s'il y a lieu)
        self.decide() #On donne les ordres

    def pseudo_debut_tour(self):
        pass

    #Tout le monde agit, nos bon-à-rien d'agissants se font massacrer à cause de leurs capacités médiocres ou remportent la victoire grâce à nos ordres brillants

    def fin_tour(self):
        #Le tour est fini, on réfléchira pendant le prochain. Comment ça, c'est mauvais pour la mémoire ?
        self.oublie()
