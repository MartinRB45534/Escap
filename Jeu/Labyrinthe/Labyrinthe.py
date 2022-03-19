from Jeu.Constantes import *
from Jeu.Effet.Effets import *
from Jeu.Labyrinthe.Generateur import *
from Jeu.Labyrinthe.Pattern import *

class Labyrinthe:
    def __init__(self,ID,largeur,hauteur,depart,patterns=None,durete = 1,niveau = 1,element = TERRE,proba=0.1):
        #print("Initialisation du labyrinthe")
        self.id = ID #Correspond à la clé du labyrinthe. Créer un init différend pour chaque lab ?
        self.largeur = largeur
        self.hauteur = hauteur
        self.durete = durete
        self.niveau = niveau #Est-ce que la dureté des murs et le niveau des cases sont une seule et même chose ?
        self.element = element

        self.depart = depart

        self.matrice_cases = [[Case((self.id,j,i),niveau,element) for i in range(hauteur)]for j in range(largeur)]

        for i in range(self.largeur):
            self.matrice_cases[i][0].murs[HAUT].effets = [Mur_impassable()]
            self.matrice_cases[i][self.hauteur-1].murs[BAS].effets = [Mur_impassable()]

        for j in range(self.hauteur):
            self.matrice_cases[0][j].murs[GAUCHE].effets = [Mur_impassable()]
            self.matrice_cases[self.largeur-1][j].murs[DROITE].effets = [Mur_impassable()]

        self.patterns=patterns
        self.cases_visitees = None

        self.temps_restant = -1 #Devient positif quand le labyrinthe est actif sans entitée supérieure
        self.controleur = None #Tant qu'il n'est pas actif, il n'a pas de controleur à qui se référer

        self.generation(proba,None,None)
        #print("Génération : check")

    def generation(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui génère la matrice du labyrinthe
            Entrées:
                -Les cases spéciales sous la forme suivante:[coord_case,objet]
                -L'éventuelle probabilité pour casser des murs
                -L'éventuel nombre de murs casser
                -L'éventuelle pourcentage de murs a casser
            Sorties:
                rien
        """
        #ini du tableau de case (4 murs pleins)
        for colone in self.matrice_cases:
            for case in colone:
                for mur in case.murs:
                    mur.effets.append(Mur_plein(self.durete))
        
        #génération en profondeur via l'objet generateur
        #print("Génération du labyrinthe")
        gene=Generateur(self.matrice_cases,self.depart,self.largeur,self.hauteur,self.patterns)
        #print("Générateur : check")
        self.matrice_cases=gene.generation(proba,nbMurs,pourcentage)

    def veut_passer(self,intrus,direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        self.matrice_cases[intrus.get_position()[1]][intrus.get_position()[2]].veut_passer(intrus,direction)

    def step(self,coord,entitee):
        self.matrice_cases[coord[0]][coord[1]].step(entitee)

    def get_vue(self,agissant):
        return self.resoud(agissant.get_position(),agissant.get_portee_vue())
            
    def getMatrice_cases(self):
        #on obtient une copie indépendante du labyrinthe
        new_mat = [[self.matrice_cases[j][i].get_copie() for i in range(self.hauteur)]for j in range(self.largeur)]
        return new_mat

    def get_case(self,position):
        return self.matrice_cases[position[1]][position[2]]

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].debut_tour()

    def pseudo_debut_tour(self): #On commence le tour
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].pseudo_debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].post_action((self.id,i,j))

    def fin_tour(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].fin_tour()
        if self.temps_restant >= 0:
            if self.temps_restant == 0:
                self.controleur.desactive_lab(self.id)
                self.controleur = None
                for i in range(self.largeur):
                    for j in range(self.hauteur):
                        self.matrice_cases[i][j].desactive()
            self.temps_restant -= 1
    #Et c'est la fin du tour !

    def quitte(self):
        self.temps_restant = 5

    def active(self,controleur):
        self.controleur = controleur
        self.temps_restant = -1 #Au cas où
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].active(controleur)

    def attaque(self,position,portee,propagation,direction,obstacles):
        return self.resoud(position,portee,"attaque",propagation,direction,obstacles)

    def resoud(self,position,portee,action="vue",propagation="C__S_Pb",direction=None,dead_ends=[],reset=True,clees=[]):
        #Les possibilités de propagation sont :
        #                           Circulaire, le mode de propagation de la vision
        #                           Rectiligne, dans une unique direction
        #                           Semi-circulaire, dans trois directions fixées
        #                           Quarter-circulaire, dans deux directions fixées
        #                           Circulaire dégénéré, commence dans toutes les directions puis devient Semi-circulaire pour interdire les demi-tours
        #                           Semi-circulaire dégénéré, commence dans trois directions puis devient Quarter-circulaire pour interdire les demi-tours
        #                           Circulaire Double dégénéré, devient Semi-circulaire dégénéré
        #                           Spatial, se déplace selon les coordonées comme la vue
        #                           Teleporte, se déplace par les téléporteurs comme les attaques magiques
        #                           Passe-porte, passe au travers des portes
        #                           Passe-barrières, passe au travers de certaines portes
        #                           Passe-mur, ignore les murs
        #Exemple de syntaxe du mode de propagation : "Sd_T_Pp", "CD_S_Pm" ou "R__T___"

        if reset:
            for i in range(len(self.matrice_cases)):
                for j in range(len(self.matrice_cases[0])):
                    self.matrice_cases[i][j].clarte = 0

        dirs = [HAUT,DROITE,BAS,GAUCHE]
        forme = propagation[0]
        if forme == "R":
            dirs = [direction]
        elif forme == "S":
            dirs.remove(dirs[direction-2])
        elif forme == "Q":
            dirs.remove(dirs[direction-2])
            dirs.remove(dirs[direction-3])

        queue=[(position,dirs,propagation)]

        self.matrice_cases[position[1]][position[2]].clarte = portee

        retrait = 1

        while len(queue)!=0 :

            data=queue[0]
            position = data[0]
            if action == "vue":
                retrait = self.matrice_cases[position[1]][position[2]].get_opacite()
            clarte = self.matrice_cases[position[1]][position[2]].clarte - retrait
            #enlever position dans queue
            queue.pop(0)

            if not position in dead_ends:
                #trouver les positions explorables
                positions_voisins=self.voisins_case(data)

                datas_explorables = self.positions_utilisables(positions_voisins,data,clees)

                for data_explorable in datas_explorables:
                    pos = data_explorable[0]
                    clarte_cible = self.matrice_cases[pos[1]][pos[2]].clarte

                    if clarte <= 0 and clarte_cible <= 0:
                        self.matrice_cases[pos[1]][pos[2]].clarte = -1

                    elif clarte > clarte_cible :
                        #on marque la case comme visitée
                        self.matrice_cases[pos[1]][pos[2]].clarte = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(data_explorable)

        if action == "vue":
            matrice_cases = []
            for colonne in self.matrice_cases:
                collone = []
                for case in colonne:
                    collone.append(case.get_infos(clees))
                matrice_cases.append(collone)
        else :
            matrice_cases = self.matrice_cases

        return matrice_cases

    def voisins_case(self,data):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        ainsi que leurs coordonnées
        """
        position = data[0]
        propagation = data[2]
        deplacement = propagation[3]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        if deplacement == "S":
            if position[2]-1>=0:
                positions_voisins.append((position[0],position[1],position[2]-1))
            else:
                positions_voisins.append(None)
                
            if position[1]+1<self.largeur:
                positions_voisins.append((position[0],position[1]+1,position[2]))
            else:
                positions_voisins.append(None)
                
            if position[2]+1<self.hauteur:
                positions_voisins.append((position[0],position[1],position[2]+1))
            else:
                positions_voisins.append(None)
                
            if position[1]-1>=0:
                positions_voisins.append((position[0],position[1]-1,position[2]))
            else:
                positions_voisins.append(None)
        elif deplacement == "T":
            for i in range(4):
                cible = self.matrice_cases[position[1]][position[2]].murs[i].get_cible()
                if cible != None:
                    if cible[0] != position[0]:
                        cible = None
                positions_voisins.append(cible)
        else:
            print("Propagation inconnue")

        return positions_voisins

    def positions_utilisables(self,positions_voisins,data,clees):
        """
        Fonction qui prend en entrées:
            les voisins de la case
            les positions des voisins
            la position de la case
            le chemin deja exploré
        et qui renvoie les directions ou l'on peut passer
        """
        position = data[0]
        directions = data[1]
        propagation = data[2]
        forme = propagation[0]
        degenerescence = propagation[1]
        deplacement = propagation[3]
        passage = propagation[6]
        datas_utilisables=[]
        cardinaux = [HAUT,DROITE,BAS,GAUCHE]

        for direction in directions:
            if positions_voisins[direction]!=None:
                voisin = positions_voisins[direction]

                #on vérifie si on peut passer
                blocage = self.matrice_cases[position[1]][position[2]].get_mur_dir(direction).get_blocage(clees)
                if blocage != "Imp" and (passage=="m" or (blocage!="Ple" and ((passage=="p" and (blocage == "Por" or blocage == "P_b")) or (passage=="b" and (blocage == "Bar" or blocage == "P_b")) or (blocage == "Esc" and deplacement == "T") or (blocage == "Tel" and deplacement == "T") or blocage == None))):
                    #On détermine éventuellement la nouvelle forme de propagation
                    if degenerescence == "d":
                        if forme == "C":
                            nouv_prop = "S_"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Q_"+propagation[2:]
                        elif forme == "Q":
                            nouv_prop = "R_"+propagation[2:]
                    elif degenerescence == "D":
                        if forme == "C":
                            nouv_prop = "Sd"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Qd"+propagation[2:]
                    else:
                        nouv_prop = propagation

                    if forme=="R":
                        nouv_dir=[direction]
                    elif forme!="C":
                        #On détermine la direction d'où l'on vient
                        if deplacement=="S":
                            dir_back = cardinaux[direction-2]
                        elif deplacement=="T":
                            dir_back = 0
                            for i in cardinaux:
                                if self.matrice_cases[voisin[1]][voisin[2]].get_mur_dir(i).get_cible()==position:
                                    dir_back = i
                        #On n'y retournera pas !
                        nouv_dir=[]
                        for i in directions:
                            if i!=dir_back:
                                nouv_dir.append(i)
                    else:
                        nouv_dir=[HAUT,DROITE,BAS,GAUCHE]

                    nouv_data=(voisin,nouv_dir,nouv_prop)

                    datas_utilisables.append(nouv_data)
        return datas_utilisables
