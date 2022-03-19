from Jeu.Constantes import *
from Jeu.Effet.Effets import *
from Jeu.Labyrinthe.Case import *

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
