from Jeu.Constantes import *
from Jeu.Effet.Effets import *

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

class Generateur:
    def __init__(self,matrice_cases,depart,largeur,hauteur,paterns,modeGeneration="Profondeur"):
        #print("Initialisation du générateur")
        self.depart = depart
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = matrice_cases
        self.modeGeneration = modeGeneration
        self.paterns = paterns
        self.poids = [1,1,1,1]

    def generation(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui permet de générer une matrice conformément au paramètres
        et au paterns
        Entrées:
            -L'éventuelle probabilité pour casser des murs
            -L'éventuel nombre de murs casser
            -L'éventuelle pourcentage de murs a casser
        Sorties:une matrice de cases générée
        """
        #print("Génération")
        matrice=None
        
        self.pre_gene_paterns()
        if self.modeGeneration=="Profondeur":
            #print("Mode de génération : profondeur")
            matrice= self.generation_en_profondeur()
            #print("Génération en profondeur : check")
            #on casse les murs conformément aux paramètres
            self.casser_X_murs(proba,nbMurs,pourcentage)
        else:
            print("mode de génération choisi incompatible")

        self.post_gene_paterns()

        for case in matrice[0]:
            case.murs[3].interdit()
        for case in matrice[-1]:
            case.murs[1].interdit()
        for colonne in matrice:
            colonne[0].murs[0].interdit()
            colonne[-1].murs[2].interdit()
        
        return matrice

    def pre_gene_paterns(self):
        """
        Fonction qui pregenere les paterns
        (on génère le squelette)
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.pre_generation(self.matrice_cases)

    def post_gene_paterns(self):
        """
        Fonction qui postgenere les paterns
        (on remplie les patterns)
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.post_generation(self.matrice_cases)

    def generation_en_profondeur(self):
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
                
                #randrange est exclusif
                num_mur=self.randomPoids(murs_generables)
                
                #direction du mur à casser
                direction_mur=murs_generables[num_mur]

                mur = self.matrice_cases[position[1]][position[2]].murs[direction_mur]

                self.casser_mur(mur)

                new_pos = mur.get_cible()
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append(new_pos)
            else:
                #on revient encore en arrière
                stack.pop()

        #print("Fini")
        
        return self.matrice_cases

    def murs_utilisables(self,position,murs_requis = 4):
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables=[]

        for i in range(4):
            mur = self.matrice_cases[position[1]][position[2]].murs[i] #mur = self.matrice_cases[position[1][0]][position[1][1]].murs[i]
            cible = mur.get_cible()
            if cible != None and cible[0]==self.depart[0]:
                case_cible = self.matrice_cases[cible[1]][cible[2]]
                mur_oppose = self.get_mur_oppose(mur)
                if mur_oppose != None and case_cible.nb_murs_pleins()>=murs_requis and mur_oppose.is_touchable() and mur.is_touchable():
                    murs_utilisables.append(i)
        return murs_utilisables

    def randomPoids(self,murs_utilisables):
        """
        Fonction qui prend en entrée:
            les murs utilisables par la fonction
        et qui renvoie le numéro d'un mur générée avec un alétoire modifié
        """

        nbrandom=0
        res=-1
        
        poids_selectionnees=[]
        poids_total=0

        for i in range (0,len(murs_utilisables)):
            poids_selectionnees+=[poids_total+self.poids[murs_utilisables[i]]]
            poids_total+=self.poids[murs_utilisables[i]]

        nbrandom=random.randrange(0,poids_total)

        i=0

        while i<len(poids_selectionnees) and res==-1:
            if nbrandom < poids_selectionnees[i]:
                res=i
            i+=1
        return res

    def casser_X_murs(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui doit casser des murs sur la matrice
        on peut déterminer le nombre de murs avec un probabilité (proba*nb murs au total)
        ou selon un nombre défini en entrée
        ou un pourcentage
        """
        if proba!=None:
            self.casser_murs_selon_proba(proba)
        elif nbMurs!=None:
            self.casser_murs(nbMurs)
        elif pourcentage!=None:
            self.casser_murs(int(pourcentage/100*self.nb_murs_total()))
        else:
            print("mauvaise utilisation de la fonction, on ne sait que faire")

    def casser_murs(self,nb_murs_a_casser):
        """
        Fonction qui casse un certains nombre de murs aléatoirement
        Entrées:
            -le nombre de murs a casser
        """
        nb_murs_casser=0

        while nb_murs_casser<=nb_murs_a_casser:
            coord_case=[random.randrange(0,len(self.matrice_cases)),random.randrange(0,len(self.matrice_cases[0]))]

            if self.casser_mur_random_case(coord_case):
                nb_murs_casser+=1


    def restrictions_case(self,coord_case):
        """
        Fonction qui renvoie les murs intouchables
        Entrées:
            -les coordonnées de le case
        Sorties:
            -les directions ou les murs ne sont pas touchables
        """
        directions_interdites=[]

        murs=self.matrice_cases[coord_case[0]][coord_case[1]].get_murs()
        for i in range(0,4):
            if not(murs[i].is_touchable):
                directions_interdites.append(i)
            
        return directions_interdites

    def casser_mur_random_case(self,position_case):
        """
        Fonction qui prend en entrée la position de la case dont on veut casser un mur
        et qui renvoie un booléen indiquant si l'on as pu casser un mur
        """
        casser = False

        murs=self.murs_utilisables(self.voisins_case(position_case[0],position_case[1]))
        if len(murs)!=0:
            mur_a_casser=random.randrange(0,len(murs))
            self.casser_mur(self.matrice_cases[position_case[0]][position_case[1]].murs[murs[mur_a_casser]])
            casser = True
        return casser

    def casser_murs_selon_proba(self,proba):
        """
        Fonction qui casse des murs selon une probabilité donnée
        Entrée:
            -la probabilité de casser un mur
        """
        for x in range(1,self.largeur) :
            for y in range(1,self.hauteur) :
                case = self.matrice_cases[x][y]
                murs=self.murs_utilisables((self.depart[0],x,y),0)
                if HAUT in murs and random.random() <= proba :
                    self.casser_mur(case.murs[HAUT])
                if GAUCHE in murs and random.random() <= proba :
                    self.casser_mur(case.murs[GAUCHE])
                    
    def casser_mur(self,mur):
        """
        Fonction qui casse un mur spécifique
        Entrées:
            la direction du mur
            la position de la case
        Sorites:Rien
        """
        #on casse les murs de la case et de la case d'en face
        autre_mur = self.get_mur_oppose(mur)
        if autre_mur ==  None :
            print("On a un mur non réciproque !")
        else :
            mur.brise()
            autre_mur.brise()

    def nb_murs_total(self):
        """
        Fonction qui renvoie le nombres de murs pleins contenus dans le labyrinthe
        """
        murs_pleins=0
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                murs_pleins+=self.matrice_cases[x][y].nb_murs_pleins()
        
        return int((murs_pleins-self.hauteur*2-self.largeur*2)/2)

    def get_mur_oppose(self,mur):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None and cible[0] == self.depart[0]:
            for mur_potentiel in self.matrice_cases[cible[1]][cible[2]].murs :
                cible_potentielle = mur_potentiel.get_cible()
                if cible_potentielle != None and cible_potentielle[0] == self.depart[0]:
                    if mur in self.matrice_cases[cible_potentielle[1]][cible_potentielle[2]].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                        mur_oppose = mur_potentiel
        return mur_oppose

class Case:
    def __init__(self,position,niveau = 1,element = TERRE,effets = [],opacite = 1):
        # Par défaut, pas de murs.
        self.position = position
        self.murs = [Mur([Teleport((position[0],position[1],position[2]-1))]),Mur([Teleport((position[0],position[1]+1,position[2]))]),Mur([Teleport((position[0],position[1],position[2]+1))]),Mur([Teleport((position[0],position[1]-1,position[2]))])]
        self.opacite = opacite
        self.opacite_bonus = 0
        self.niveau = niveau
        self.element = element
        self.clarte = 0
        self.code = 0
        self.repoussante = False
        self.effets = [] #Les cases ont aussi des effets ! Les auras, par exemple.
        self.effets += effets
        if self.element == TERRE:
            self.effets.append(Terre_permanente(self.niveau*2))
        elif self.element == FEU:
            self.effets.append(Feu_permanent(self.niveau,self.niveau*5))
        elif self.element == GLACE:
            self.effets.append(Glace_permanente(self.niveau,self.niveau/10))
        elif self.element == OMBRE:
            self.effets.append(Ombre_permanente(self.niveau,self.niveau/2))
        self.controleur = None

    #Découvrons le déroulé d'un tour, avec case-chan :

    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! On commence par activer les effets réguliers :
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()
            if effet.phase == "affichage":
                self.effets.remove(effet)
                

    def pseudo_debut_tour(self):
        self.code = 0
        priorite_max = 0
        IDmax = 0
        auras = {}

        for effet in self.effets:
            if isinstance(effet,Aura_elementale):
                ID = effet.responsable
                if ID in auras.keys() : # On a déjà une aura de ce type
                    auras[ID].append(effet)
                else:
                    auras[ID]=[effet]
                prio = effet.priorite
                if prio > priorite_max : # On a un nouveau gagnant !
                    IDmax = ID
                    priorite_max = prio

        for aura in auras[IDmax]:
            if isinstance(aura,(Terre,Terre_permanente)):
                self.code += 1
            elif isinstance(aura,(Feu,Feu_permanent)):
                self.code += 2
            elif isinstance(aura,(Glace,Glace_permanente)):
                self.code += 4
            elif isinstance(aura,(Ombre,Ombre_permanente)):
                self.code += 8

    #Certains agissants particulièrement tapageurs font un concours de celui qui aura la plus grosse aura (comment ça, cette phrase particulièrement compliquée aura juste servi à faire un jeu de mot sur aura
    def ajoute_aura(self,aura):
        """Fonction qui ajoute un effet d'aura. On décidera de ceux qui s'exécutent plus tard."""
        self.effets.append(aura)
        if isinstance(aura,Aura_elementale): #On a besoin de savoir quelle aura prévaudra
            aura.priorite += self.clarte/2 #La clarté vient d'être utilisée pour déterminer la portée de l'aura, et n'est normalement pas encore réinitialisée
            if isinstance(aura,Feu):
                resp = aura.responsable
                for aura_bis in self.effets:
                    if isinstance(aura_bis,Feu) and aura_bis.responsable == resp :
                        aura_bis.phase = "terminé"

    #Les agissants prennent des décisions, agissent, se déplacent, les items se déplacent aussi.
    def veut_passer(self,intrus,direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère au mur compétent, qui gère tout."""
        self.murs[direction].veut_passer(intrus)

    def step_out(self,entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_out):
                effet.execute(entitee)

    def step_in(self,entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_in):
                effet.execute(entitee) #On agit sur les agissants qui arrivent (pièges, téléportation, etc.)

    #Tout le monde a fini de se déplacer.
    def post_action(self,position):
        self.opacite_bonus = 0 # On reset ça à chaque tour, sinon ça va devenir tout noir
        self.code = 0
        if len(self.effets) == 1: #On a un seul effet ! L'effet d'aura.
            if self.element != TERRE: #Les auras de terre sont juste là pour embêter les autres de toute façon
                self.effets[0].execute(self,position)
            else :
                self.code += 1
        else:
            on_attaques = []
            attaques = []
            priorite_max = 0
            IDmax = 0
            auras = {}

            for effet in self.effets:
                if isinstance(effet,Aura_elementale):
                    ID = effet.responsable
                    if ID in auras.keys() : # On a déjà une aura de ce type
                        auras[ID].append(effet)
                    else:
                        auras[ID]=[effet]
                    prio = effet.priorite
                    if prio > priorite_max : # On a un nouveau gagnant !
                        IDmax = ID
                        priorite_max = prio
                elif isinstance(effet,On_attack):
                    on_attaques.append(effet)
                elif (isinstance(effet,Attaque_case_delayee) and effet.delai > 0):
                    effet.execute(self,position) #On diminue le délai
                elif isinstance(effet,Attaque_case):
                    attaques.append(effet)
                elif isinstance(effet,On_post_action): #Les auras non-élémentales sont aussi des On_post_action
                    effet.execute(self,position)

            for aura in auras[IDmax]:
                aura.execute(self,position)

            for attaque in attaques:
                for protection in on_attaques:
                    protection.execute(attaque)
                attaque.execute(self,position)

    def fin_tour(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if effet.phase == "terminé":
                self.effets.remove(effet)

    #Le tour se termine gentiment, et on recommence !

#Pour la génération, quand on a pas encore les barrières, portes et compagnie.
    def nb_murs_pleins(self):
        """
        Fonction qui renvoie le nombre de murs pleins dans la case
        """
        pleins=0

        for mur in self.murs :
            if mur.is_ferme() :
                pleins+=1
        
        return pleins
                
    def casser_mur(self,direction):
        """
        Fonction qui casse le mur dans la direction indiquée
        """
        self.murs[direction].brise()

    def construire_mur(self,direction,durete):
        """
        Fonction qui construit le mur dans la direction indiquée
        """
        self.murs[direction].construit(durete)

    def interdire_mur(self,direction):
        """
        Fonction qui construit le mur impassable dans la direction indiquée
        """
        self.murs[direction].interdit()

    def mur_plein(self,direction):
        """
        Fonction qui indique si le mur indiquée par la direction est plein ou non
        """
        return self.murs[direction].is_ferme()

    def acces(self,direction,clees=[]):
        return not(self.murs[direction].is_ferme(clees)) and self.murs[direction].get_cible()

    def murs_pleins(self):
        directions = []
        for direction in [HAUT,DROITE,BAS,GAUCHE]:
            if self.mur_plein[direction]:
                directions.append(direction)
        return directions

    def get_mur_dir(self,direction):
        return self.murs[direction]

    def get_murs(self):
        return self.murs

    def get_mur_haut(self):
        return self.murs[0]

    def get_mur_droit(self):
        return self.murs[1]

    def get_mur_bas(self):
        return self.murs[2]

    def get_mur_gauche(self):
        return self.murs[3]

    def toString(self):
        return "haut "+str(self.murs[0].get_etat())+" droite "+str(self.murs[1].get_etat())+" bas "+str(self.murs[2].get_etat())+" gauche "+str(self.murs[3].get_etat())+"  "

    def get_opacite(self):
        return self.opacite + self.opacite_bonus

    def get_infos(self,clees): #Est-ce que ce serait plus clair sous forme de dictionnaire ? Ou d'objet ?
        return [self.position, #La position de la case, sous forme de tuple
                self.clarte, #La clarté, qui vient d'être calculée pour l'agissant
                0, #Pour le décompte de l'oubli
                [0, #Pour les trajets (importance des ennemis), en contournant les agissants
                 0, #Pour les trajets (importance des ennemis), en traversant les agissants
                 0, #Pour les trajets (dangerosité), en contournant les agissants
                 0, #Pour les trajets (dangerosité), en traversant les agissants
                 0, #Pour les autres trajets (pour calculer de façon unique, effacé avant chaque calcul)
                 False],
                self.calcule_code(), #Le code correspondant aux auras et autres effets
                [self.murs[i].get_cible_ferme(clees) for i in range(4)], #Les murs et leur traversabilité pour l'agissant
                [], #Pour stocker les entitées
                self.get_codes_effets(), #Pour stocker les effets (attaques delayées)
                self.repoussante] #Pour savoir si on peut y rester

    def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
        new_courant = pygame.time.get_ticks()
        # duree = new_courant - constantes_temps['courant']
        # constantes_temps['reste'] += duree
        # constantes_temps['courant'] = new_courant
        return self.code

    def get_codes_effets(self):
        effets=[]
        for effet in self.effets:
            if isinstance(effet,Attaque_case_delayee):
                effets.append([effet.responsable,effet.delai,effet.degats])
        return effets

    def get_copie(self):
        copie = Case(self.position,self.niveau,self.element,self.effets,self.opacite)
        copie.murs = self.murs
        return copie

    def active(self,controleur):
        self.controleur = controleur
        for mur in self.murs :
            mur.active(controleur)

    def desactive(self):
        self.controleur = None
        for mur in self.murs :
            mur.desactive()

class Mur:
    def __init__(self,effets):
        self.effets = effets
        self.peut_passer = False
        self.controleur = None

    def is_ferme(self,clees=[]):
        ferme = False
        for effet in self.effets :
            if isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                ferme = True
        return ferme

    def get_blocage(self,clees):
        blocage = None
        for effet in self.effets :
            if isinstance(effet,Mur_impassable):
                blocage = "Imp"
            elif blocage != "Imp" and isinstance(effet,Mur_plein) and not(effet.casse):
                blocage = "Ple"
            elif blocage != "Imp" and blocage != "Ple" and isinstance(effet,Porte_barriere) and effet.ferme and not(effet.code in clees):
                blocage = "P_b"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and isinstance(effet,Porte) and effet.ferme and not(effet.code in clees):
                blocage = "Por"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and isinstance(effet,Barriere):
                blocage = "Bar"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and blocage != "Por" and blocage != "Bar" and isinstance(effet,Escalier):
                blocage = "Esc"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and blocage != "Por" and blocage != "Bar" and blocage != "Esc" and isinstance(effet,Teleport) and effet.affiche:
                blocage = "Tel"
        return blocage

    def is_touchable(self):
        touchable = True
        for effet in self.effets :
            if isinstance(effet,(Mur_impassable)):
                touchable = False
        return touchable

    def veut_passer(self,intrus):
        self.peut_passer = True
        for effet in self.effets :
            if isinstance(effet,On_try_through):
                effet.execute(self,intrus) #On vérifie que rien n'empêche le passage de l'intrus
        if self.peut_passer :
            for effet in self.effets :
                if isinstance(effet,On_through):
                    effet.execute(intrus) #Il est conseillé d'avoir un seul effet de déplacement, comme un seul effet d'autorisation de passage...
            if issubclass(intrus.get_classe(),Item):
                intrus.vole()
        elif issubclass(intrus.get_classe(),Item):
            intrus.heurte_mur()

    def peut_voir(self):
        visible = True
        for effet in self.effets :
            if (isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and effet.ferme)) or (isinstance(effet,Teleport) and effet.affiche):
                visible = False
        return visible

    def interdit(self):
        self.effets.append(Mur_impassable())

    def construit(self,durete):
        self.effets.append(Mur_plein(durete))

    def detruit(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_try_through):
                self.effets.remove(effet)
                del(effet)

    def brise(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_try_through) and not isinstance(effet,Mur_impassable) :
                self.effets.remove(effet)
                del(effet)

    def cree_porte(self,durete,code,porte=None):
        self.brise()
        if porte == None:
            self.effets.append(Porte(durete,code))
        else:
            self.effets.append(porte(durete,code))

    def get_trajet(self):
        trajet = None
        for effet in self.effets :
            if trajet != "teleport" and (isinstance(effet,Escalier) and effet.sens == HAUT):
                trajet = "escalier haut"
            elif trajet != "teleport" and (isinstance(effet,Escalier) and effet.sens == BAS):
                trajet = "escalier bas"
            elif isinstance(effet,Teleport) and effet.affiche == True:
                trajet = "teleport"
        return trajet

    def get_cible(self):
        cible = None
        en_cours = True
        i = 0
        while en_cours and i < len(self.effets) :
            effet = self.effets[i]
            if isinstance(effet,Teleport) :
                en_cours = False
                cible = effet.position
            i += 1
        return cible

    def get_cible_ferme(self,clees):
        return [self.get_cible_ferme_simple(),self.get_cible_ferme_portes(clees),self.get_cible_ferme_portails(),self.get_cible_ferme_portes_portails(clees),self.get_cible_ferme_escaliers(clees)]

    def get_cible_ferme_simple(self):
        """Renvoie la position de la case d'arrivée si on est un mur ouvert sans téléporteur, False sinon"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not effet.affiche :
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and effet.ferme):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portes(self,clees):
        """Renvoie aussi la position si le mur est une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not effet.affiche :
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portails(self):
        """Renvoie aussi la position si le mur est un téléporteur (mais pas s'il est une porte)"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not isinstance(effet,Escalier):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and effet.ferme):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portes_portails(self,clees):
        """Renvoie aussi la position si le mur est un téléporteur ou une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not isinstance(effet,Escalier):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_escaliers(self,clees):
        """Renvoie aussi la position si le mur est un téléporteur ou une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def set_cible(self,position,surnaturel=False,portail=None):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        if portail == None:
            portail = Teleport
        self.effets.append(portail(position,surnaturel))

    def set_escalier(self,position,sens,escalier=None):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        if escalier == None:
            escalier = Escalier
        self.effets.append(escalier(position,sens))

    def get_mur_oppose(self):
        mur_oppose = None
        cible = self.get_cible()
        if cible != None:
            case_cible = self.controleur.get_case(cible)
            for mur in case_cible.murs :
                cible_potentielle = mur.get_cible()
                if cible_potentielle != None:
                    case_cible_potentielle = self.controleur.get_case(cible_potentielle)
                    if self in case_cible_potentielle.murs:
                        mur_oppose = mur
        return mur_oppose
        

    def active(self,controleur):
        self.controleur = controleur

    def desactive(self):
        self.controleur = None

class Patern:
    def __init__(self,position,largeur,hauteur,entrees=[(0,1,0)],codes=[],vide = True,durete = 1,niveau = 1,element = TERRE):
        self.position = position
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrice_cases = [[Case((self.position[0],j+self.position[1],i+self.position[2]),niveau,element) for i in range(hauteur)]for j in range(largeur)]
        self.entrees = entrees
        self.codes = codes
        self.vide = vide
        self.durete = durete
        self.niveau = niveau
        self.element = element

    def post_gen_entrees(self,matrice_lab):
        """
        Fonction qui transforme les entrées en portes ou en murs vides
        """
        
        for nb in range(len(self.entrees)):
            x = self.entrees[nb][1]+self.position[1]
            y = self.entrees[nb][2]+self.position[2]
            case = matrice_lab[x][y]
            for bord in self.contraintes_cases(self.entrees[nb]):
                mur = case.murs[bord]
                if nb < len(self.codes) :
                    if mur.get_blocage([]) != "Imp": # /!\ Nécessaire ?
                        mur.cree_porte(self.durete,self.codes[nb])
                    mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                    if mur_oppose != None and mur_oppose.get_blocage([]) != "Imp":
                        mur_oppose.cree_porte(self.durete,self.codes[nb])
                else :
                    mur.brise()
                    mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                    if mur_oppose != None:
                        mur_oppose.brise()

    def pre_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui pre génère les cases du patern
        """
        coordonnee_x = self.position[1]
        coordonnee_y = self.position[2]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                x_pat=i-coordonnee_x
                y_pat=j-coordonnee_y
                #on ne doit générer que les cases au bords
                #plus précisement on doit empêcher le générateur d'y toucher
                if not self.case_est_une_entree((self.position[0],x_pat,y_pat)) and self.case_au_bord((self.position[0],x_pat,y_pat)):
                    dirs_intouchables=self.contraintes_cases((self.position[0],x_pat,y_pat))
                    for direction in dirs_intouchables:
                        mur = matrice_lab[i][j].murs[direction]
                        mur.interdit()
                        mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                        if mur_oppose != None :
                            mur_oppose.interdit()

    def post_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui clear la salle
        """
        for i in range(self.position[1],self.position[1]+self.largeur):
            for j in range(self.position[2],self.position[2]+self.hauteur):
                pos_pat = (self.position[0],i-self.position[1],j-self.position[2])
                #on enlève les murs intouchables
                dirs_intouchables=[]
                if self.case_au_bord(pos_pat):
                    dirs_intouchables=self.contraintes_cases(pos_pat)
                for direction in [HAUT,DROITE,BAS,GAUCHE]:
                    mur = matrice_lab[i][j].murs[direction]
                    if direction in dirs_intouchables:
                        mur.detruit()
                        mur.construit(self.durete)
                        mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                        if mur_oppose != None :
                            mur_oppose.detruit()
                            mur_oppose.construit(self.durete)
                    elif self.vide:
                        mur.detruit()
        self.post_gen_entrees(matrice_lab)
            
    def case_est_une_entree(self,position):
        """
        Fonction qui prend en entrées:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si elle est une entrée ou pas
        """
        est_entree=False
        for entree in self.entrees:
            if entree == position:
                est_entree=True

        return est_entree
    def case_au_bord(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si la case est au bord ou non
        """
        return (position[1] == 0 or position[1] == self.largeur-1)or(position[2] == 0 or position[2] == self.hauteur-1)
        
    def clear_case(self,position):
        """
        Fonction qui clear la case selectionner
        """
        for i in range(0,4):
            self.matrice_cases[position[1]][position[2]].casser_mur(i)
    
    def incorporation_case(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on casse les murs qui ne sont pas aux extrèmes
        if position[1]!=0:
            self.matrice_cases[position[1]][position[2]].casser_mur(GAUCHE)
            
        if position[1]!=(self.largeur-1):
            self.matrice_cases[position[1]][position[2]].casser_mur(DROITE)

        if position[2]!=0:
            self.matrice_cases[position[1]][position[2]].casser_mur(HAUT)
            
        if position[2]!=(self.hauteur-1):
            self.matrice_cases[position[1]][position[2]].casser_mur(BAS)

    
    
    def integration_case(self,position,matrice_lab):
        """
        Fonction qui prend en enetrées:
            les coordonnées de la case
            la matrice du labyrinthe

        et casse les murs qui empêches la navigation dans le labyrinthe
        """

        bords=self.case_bord(position,len(matrice_lab),len(matrice_lab[0]))

        for bord in bords:
            mur = matrice_lab[position[1]][position[2]].murs[bord]
            mur_oppose=self.get_mur_oppose(mur,matrice_lab)
            if mur_oppose!=None and not(mur.is_ferme()):
                mur.briser()

    def case_bord(self,position,largeur_mat,hauteur_mat):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            la largeur et la hauteur de la matrice
            et qui renvoie la/les direction/s des bords
        """
        bords=[]
        
        #on ajoute les murs qui ne sont pas aux extrèmes
        if position[1]!=0:
            bords+=[GAUCHE]
            
        if position[1]!=(largeur_mat-1):
            bords+=[DROITE]

        if position[2]!=0:
            bords+=[HAUT]
            
        if position[2]!=(hauteur_mat-1):
            bords+=[BAS]

        return bords

    def contraintes_cases(self,position):
        """
        Fonction qui renvoie les murs qui sont soumis a des contraintes
        venant de la salle
        Entrées:
            -les coordonnées de la case
        Sorties:
            -les directions des murs a ne pas caser
        """
        #pour l'instant les contraintes se limites justes au bords de la matrice
        bords=[]
        
        if position[1]==0:
            bords+=[GAUCHE]
            
        if position[1]==(self.largeur-1):
            bords+=[DROITE]

        if position[2]==0:
            bords+=[HAUT]
            
        if position[2]==(self.hauteur-1):
            bords+=[BAS]

        return bords

    def copie(self,position,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui copie les cases du patern dans le labyrinthe
        """
        for i in range(position[1],position[1]+self.largeur):
            for j in range(position[2],position[2]+self.hauteur):
                matrice_lab[i][j]=self.matrice_cases[i-position[1]][j-position[2]]
                self.integration_case((self.position[0],i,j),matrice_lab)
        return matrice_lab

    def get_pos(self):
        return self.position

    def get_mur_oppose(self,mur,matrice_lab):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None:
            if cible[0] == self.position[0]:
                for mur_potentiel in matrice_lab[cible[1]][cible[2]].murs :
                    cible_potentielle = mur_potentiel.get_cible()
                    if cible_potentielle != None:
                        if cible_potentielle[0] == self.position[0]:
                            if mur in matrice_lab[cible_potentielle[1]][cible_potentielle[2]].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                                mur_oppose = mur_potentiel
        return mur_oppose
