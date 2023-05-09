from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Entitee.Entitees import *

# from Jeu.Constantes import *
# from Jeu.Effet.Effets import *
# from Jeu.Labyrinthe.Generateur import *
from Jeu.Labyrinthe.Pattern import *
from Jeu.Labyrinthe.Vue import *

class Labyrinthe(Vue):
    def __init__(self,ID:str,decalage:Decalage,depart:Position,patterns:List[Pattern]=[],durete = 1,niveau = 1,element = TERRE,proba=0.1,poids:List[int]=[1]*NB_DIRECTIONS):
        #print("Initialisation du labyrinthe")
        self.id = ID #Correspond à la clé du labyrinthe. Créer un init différend pour chaque lab ?
        self.decalage = decalage
        self.durete = durete
        self.niveau = niveau #Est-ce que la dureté des murs et le niveau des cases sont une seule et même chose ?
        self.element = element

        self.depart = depart

        self.matrice_cases = [[Case(Position(self.id,j,i),niveau,element) for i in range(decalage.y)]for j in range(decalage.x)]
        self.bord = Bord_lab(self.decalage,[pattern.bord for pattern in patterns])

        for cote in Bord(self.decalage):
            self[cote].effets = [Mur_impassable()]

        self.patterns=patterns
        self.cases_visitees = None

        self.temps_restant = -1 #Devient positif quand le labyrinthe est actif sans entitée supérieure
        self.controleur = None #Tant qu'il n'est pas actif, il n'a pas de controleur à qui se référer

        self.generation(proba,poids)
        #print("Génération : check")

    def __getitem__(self,key) -> Case|Mur:
        if isinstance(key,tuple):
            return self.matrice_cases[key[0].x][key[0].y][key[1]]
        elif isinstance(key,(Decalage,Position)):
            return self.matrice_cases[key.x][key.y]
        if isinstance(key,Cote):
            return self[key.emplacement][key.direction]
        return NotImplemented

    def __setitem__(self,key,value):
        if isinstance(key,tuple):
            self.matrice_cases[key[0].x][key[0].y][key[1]] = value
        elif isinstance(key,(Decalage,Position)):
            self.matrice_cases[key.x][key.y] = value
        if isinstance(key,Cote):
            self[key.emplacement][key.direction] = value
        else:
            return NotImplemented

    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Position):
            return item.lab == self.id and 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        elif isinstance(item,Cote):
            return item.emplacement in self
        return NotImplemented

    def __iter__(self):
        for decalage in self.decalage:
            yield Position(self.id,0,0) + decalage

    def generation(self,proba:float,poids:List[int]):
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
        #génération en profondeur via l'objet generateur
        #print("Génération du labyrinthe")
        self.generation_en_profondeur(poids)


        for pos in self:
            for mur in self.murs_utilisables(pos,0):
                if random.random() <= proba:
                    self[mur].brise()
                    self[mur.oppose()].brise()

        for pattern in self.patterns:
            if pattern.vide:
                for pos in pattern:
                    for cote in Bord_dec(pos):
                        if not cote in self.bord:
                            self[cote].brise()
                            self[cote.oppose()].brise()

            for i in range(len(pattern.entrees)):
                if i < len(pattern.codes):
                    self[pattern.entrees[i]+pattern.position].cree_porte(pattern.codes[i])
                    self[pattern.entrees[i].oppose()+pattern.position].cree_porte(pattern.codes[i])
                else:
                    self[pattern.entrees[i]].brise()
                    self[pattern.entrees[i].oppose()].brise()

    def generation_en_profondeur(self,poids:List[int]):
        """
        Fonction qui génère la matrice avec la méthode du parcours en profondeur
        Entrées:Rien
        Sorties:une matrice de cases générée avec le parcours en profondeur
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre générateur
        #cela permet d'avoir le meme résultat
        #rdm=851353618387733257
        #print("seed ",rdm)
        random.seed(rdm)

        #print("Début de la génération")
        #position dans la matrice
        position = self.depart
        #le stack est une liste de positions
        stack=[position]

        while len(stack)!=0 :

            #on récupère les coords de là où l'on est cad la dernière case dans le stack
            position = stack[len(stack)-1]

            murs_generables = self.murs_utilisables(position)

            if len(murs_generables) > 0 : 

                mur=random.choices(murs_generables,[poids[mur.direction] for mur in murs_generables])[0]
                mur_opp = mur.oppose()

                self[mur].brise()
                self[mur_opp].brise()

                new_pos = mur_opp.emplacement
                self[new_pos].clarte=1
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append(new_pos)
            else:
                #on revient encore en arrière
                stack.pop()

        #print("Fini")

    def murs_utilisables(self,position:Position,nb_murs=NB_DIRECTIONS) -> List[Cote]:
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables:List[Cote]=[]

        for cote in Bord_dec(position):
            opp = cote.oppose()
            if not cote in self.bord :
                if self[opp.emplacement].nb_murs_pleins() >= nb_murs:
                    murs_utilisables.append(cote)
        return murs_utilisables

    def veut_passer(self,intrus:Mobile,direction:Direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        self[intrus.get_position(),direction].veut_passer(intrus)

    def step(self,coord:Position,entitee:Entitee):
        self[coord].step(entitee)

    def get_vue(self,agissant:Agissant):
        return Representation_vue(self.id,self.resoud(agissant.get_position(),agissant.get_portee_vue()),self.decalage)
            
    def getMatrice_cases(self):
        #on obtient une copie indépendante du labyrinthe
        new_mat = [[self.matrice_cases[j][i].get_copie() for i in range(self.decalage.y)]for j in range(self.decalage.x)]
        return new_mat

    def get_case(self,position:Position):
        return self[position]

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].debut_tour()

    def pseudo_debut_tour(self): #On commence le tour
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].pseudo_debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].post_action()

    def fin_tour(self):
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].fin_tour()
        if self.temps_restant >= 0:
            if self.temps_restant == 0:
                self.controleur.desactive_lab(self.id)
                self.controleur = None
                for i in range(self.decalage.x):
                    for j in range(self.decalage.y):
                        self.matrice_cases[i][j].desactive()
            self.temps_restant -= 1
    #Et c'est la fin du tour !

    def quitte(self):
        self.temps_restant = 5

    def active(self,controleur:Controleur):
        self.controleur = controleur
        self.temps_restant = -1 #Au cas où
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].active(controleur)

    def attaque(self,position:Position,portee:int,propagation:str,direction:Direction,obstacles:List):
        self.resoud(position,portee,"attaque",propagation,direction,obstacles)

    def resoud(self,position:Position,portee:int,action="vue",propagation="C__S_Pb",direction:Direction|None=None,dead_ends:List=[],reset=True,clees:List[str]=[]) -> List[List[Representation_case]]|None:
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

        dirs = [Direction(i) for i in range(NB_DIRECTIONS)]
        forme = propagation[0]
        if forme == "R":
            dirs = [direction]
        elif forme == "S":
            dirs.remove(dirs[direction.oppose()])
        elif forme == "Q":
            dirs.remove(dirs[direction.oppose()])
            dirs.remove(dirs[direction.oppose()-1])

        queue=[(position,dirs,propagation)]

        self[position].clarte = portee

        retrait = 1

        while len(queue)!=0 :

            data=queue[0]
            position = data[0]
            if action == "vue":
                retrait = self[position].get_opacite()
            clarte = self[position].clarte - retrait
            #enlever position dans queue
            queue.pop(0)

            if not position in dead_ends:
                #trouver les positions explorables
                positions_voisins=self.voisins_case(data)

                datas_explorables = self.positions_utilisables(positions_voisins,data,clees)

                for data_explorable in datas_explorables:
                    pos = data_explorable[0]
                    clarte_cible = self[pos].clarte

                    if clarte <= 0 and clarte_cible <= 0:
                        self[pos].clarte = -1

                    elif clarte > clarte_cible :
                        #on marque la case comme visitée
                        self[pos].clarte = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(data_explorable)

        if action == "vue":
            matrice_cases:List[List[Representation_case]] = []
            for colonne in self.matrice_cases:
                collone = []
                for case in colonne:
                    collone.append(case.get_infos(clees))
                matrice_cases.append(collone)
            return matrice_cases

    def voisins_case(self,data:List):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        ainsi que leurs coordonnées
        """
        position:Position = data[0]
        propagation:str = data[2]
        deplacement = propagation[3]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        for i in DIRECTIONS:
            if deplacement == "S":
                cible = position+i
            elif deplacement == "T":
                cible = self[position,i].get_cible()
            else:
                print("Propagation inconnue")
            if not cible in self:
                cible = None
            positions_voisins.append(cible)

        return positions_voisins

    def positions_utilisables(self,positions_voisins:List[Position],data:List,clees:str):
        """
        Fonction qui prend en entrées:
            les voisins de la case
            les positions des voisins
            la position de la case
            le chemin deja exploré
        et qui renvoie les directions ou l'on peut passer
        """
        position:Position = data[0]
        directions:List[Direction] = data[1]
        propagation:str = data[2]
        forme = propagation[0]
        degenerescence = propagation[1]
        deplacement = propagation[3]
        passage = propagation[6]
        datas_utilisables=[]

        for direction in directions:
            if positions_voisins[direction]!=None:
                voisin = positions_voisins[direction]

                #on vérifie si on peut passer
                blocage = self[position].get_mur_dir(direction).get_blocage(clees)
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
                            dir_back = direction+2
                        elif deplacement=="T":
                            dir_back = 0
                            for i in DIRECTIONS:
                                if self[voisin,i].get_cible()==position:
                                    dir_back = i
                        #On n'y retournera pas !
                        nouv_dir=[]
                        for i in directions:
                            if i!=dir_back:
                                nouv_dir.append(i)
                    else:
                        nouv_dir=[dire for dire in DIRECTIONS]

                    nouv_data=(voisin,nouv_dir,nouv_prop)

                    datas_utilisables.append(nouv_data)

        return datas_utilisables
