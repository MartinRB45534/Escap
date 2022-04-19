from Jeu.Constantes import *
from Jeu.Effet.Effets import *
from Jeu.Labyrinthe.Case import *
from Jeu.Labyrinthe.Structure_spatiale.Espace import *

class Patern(Espace):
    def __init__(self,position,decalage,entrees=[Decalage(1,0)],codes=[],vide = True,durete = 1,niveau = 1,element = TERRE):
        self.position = position
        self.decalage = decalage
        self.matrice_cases = [[Case(self.position+j*DROITE+i*BAS) for i in range(decalage.y)]for j in range(decalage.x)]
        self.entrees = entrees
        self.codes = codes
        self.vide = vide
        self.durete = durete
        self.niveau = niveau
        self.element = element

    def __getitem__(self,key):
        if isinstance(key,tuple):
            return self[key[0]][key[1]]
        elif isinstance(key,Decalage):
            return self.matrice_cases[key.x][key.y]
        elif isinstance(key,Position):
            return self[key-self.position]
        else:
            return NotImplemented

    def __contains__(self,item):
        if item is None:
            return False
        elif isinstance(item,Position):
            return self.converti(item) in self
        elif isinstance(item,Decalage):
            return 0<=item.x<self.decalage.x and 0<=item.y<self.decalage.y
        return NotImplemented

    def converti(self,position):
        return position-self.position

    def post_gen_entrees(self,matrice_lab):
        """
        Fonction qui transforme les entrées en portes ou en murs vides
        """

        for nb in range(len(self.entrees)):
            pos_entree = self.position+self.entrees[nb]
            case = matrice_lab[pos_entree.x][pos_entree.y]
            for bord in self.contraintes_cases(self.entrees[nb]):
                mur = case[bord]
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
        for i in range(self.decalage.x):
            if not Decalage(i,0) in self.entrees:
                mur = matrice_lab[self.position.x+i][self.position.y][HAUT]
                mur.interdit()
                mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                if mur_oppose != None :
                    mur_oppose.interdit()
            if not Decalage(i,self.decalage.y-1) in self.entrees:
                mur = matrice_lab[self.position.x+i][self.position.y+self.decalage.y-1][BAS]
                mur.interdit()
                mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                if mur_oppose != None :
                    mur_oppose.interdit()
        for j in range(self.decalage.y):
            if not Decalage(0,j) in self.entrees:
                mur = matrice_lab[self.position.x][self.position.y+j][GAUCHE]
                mur.interdit()
                mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                if mur_oppose != None :
                    mur_oppose.interdit()
            if not Decalage(self.decalage.x-1,j) in self.entrees:
                mur = matrice_lab[self.position.x+self.decalage.x-1][self.position.y+j][DROITE]
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
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                pos_pat = Position(self.position.lab,i,j)
                #on enlève les murs intouchables
                dirs_intouchables=[]
                if self.case_au_bord(pos_pat):
                    dirs_intouchables=self.contraintes_cases(pos_pat)
                for direction in DIRECTIONS:
                    mur = matrice_lab[self.position.x+i][self.position.y+j][direction]
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
        return (position.x == 0 or position.x == self.decalage.x-1)or(position.y == 0 or position.y == self.decalage.y-1)
        
    def clear_case(self,position):
        """
        Fonction qui clear la case selectionner
        """
        for i in range(4):
            self[position].casser_mur(i)
    
    def incorporation_case(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on casse les murs qui ne sont pas aux extrèmes
        if position.x!=0:
            self[position].casser_mur(GAUCHE)
            
        if position.x!=(self.decalage.x-1):
            self[position].casser_mur(DROITE)

        if position.y!=0:
            self[position].casser_mur(HAUT)
            
        if position.y!=(self.decalage.y-1):
            self[position].casser_mur(BAS)

    def integration_case(self,position,matrice_lab):
        """
        Fonction qui prend en enetrées:
            les coordonnées de la case
            la matrice du labyrinthe

        et casse les murs qui empêches la navigation dans le labyrinthe
        """

        bords=self.case_bord(position,len(matrice_lab),len(matrice_lab[0]))

        for bord in bords:
            mur = matrice_lab[position.x][position.y][bord]
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
        if position.x!=0:
            bords+=[GAUCHE]
            
        if position.x!=(largeur_mat-1):
            bords+=[DROITE]

        if position.y!=0:
            bords+=[HAUT]
            
        if position.y!=(hauteur_mat-1):
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
        
        if position.x==0:
            bords+=[GAUCHE]
            
        if position.x==(self.decalage.x-1):
            bords+=[DROITE]

        if position.y==0:
            bords+=[HAUT]
            
        if position.y==(self.decalage.y-1):
            bords+=[BAS]

        return bords

    def copie(self,position,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui copie les cases du patern dans le labyrinthe
        """
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                matrice_lab[position.x+i][position.y+j]=self.matrice_cases[i][j]
                self.integration_case(self.position+i*DROITE+j*BAS,matrice_lab)
        return matrice_lab

    def get_pos(self):
        return self.position

    def get_mur_oppose(self,mur,matrice_lab):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None:
            if cible in self.position:
                for mur_potentiel in matrice_lab[cible.x][cible.y].murs :
                    cible_potentielle = mur_potentiel.get_cible()
                    if cible_potentielle in self.position:
                        if mur in matrice_lab[cible_potentielle.x][cible_potentielle.y].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                            mur_oppose = mur_potentiel
        return mur_oppose
