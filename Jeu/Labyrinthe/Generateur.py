# from Jeu.Constantes import *
# from Jeu.Labyrinthe.Structure_spatiale.Espace import *
# import random

# class Generateur(Espace):
#     def __init__(self,matrice_cases,depart,largeur,hauteur,paterns,modeGeneration="Profondeur"):
#         #print("Initialisation du générateur")
#         self.depart = depart
#         self.largeur = largeur
#         self.hauteur = hauteur
#         self.matrice_cases = matrice_cases
#         self.modeGeneration = modeGeneration
#         self.paterns = paterns
#         self.poids = [1,1,1,1]

#     def __getitem__(self,key):
#         if isinstance(key,tuple):
#             return self.matrice_cases[key[0].x][key[0].y][key[1]]
#         elif isinstance(key,Position):
#             return self.matrice_cases[key.x][key.y]
#         else:
#             return NotImplemented

#     def __contains__(self,item):
#         if item is None:
#             return False
#         elif isinstance(item,Position):
#             return item.lab == self.ID and 0<=item.x<self.largeur and 0<=item.y<self.hauteur
#         elif isinstance(item,Decalage):
#             return 0<=item.x<self.largeur and 0<=item.y<self.hauteur
#         return NotImplemented

#     def generation(self,proba=None,nbMurs=None,pourcentage=None):
#         """
#         Fonction qui permet de générer une matrice conformément au paramètres
#         et au paterns
#         Entrées:
#             -L'éventuelle probabilité pour casser des murs
#             -L'éventuel nombre de murs casser
#             -L'éventuelle pourcentage de murs a casser
#         Sorties:une matrice de cases générée
#         """
#         #print("Génération")
        
#         self.pre_gene_paterns()
#         if self.modeGeneration=="Profondeur":
#             #print("Mode de génération : profondeur")
#             self.generation_en_profondeur()
#             #print("Génération en profondeur : check")
#             #on casse les murs conformément aux paramètres
#             self.casser_X_murs(proba,nbMurs,pourcentage)
#         else:
#             print("mode de génération choisi incompatible")

#         self.post_gene_paterns()

#         for case in self.matrice_cases[0]:
#             case[3].interdit()
#         for case in self.matrice_cases[-1]:
#             case[1].interdit()
#         for colonne in self.matrice_cases:
#             colonne[0][0].interdit()
#             colonne[-1][2].interdit()

#     def pre_gene_paterns(self):
#         """
#         Fonction qui pregenere les paterns
#         (on génère le squelette)
#         """
#         if self.paterns != None:
#             for patern in self.paterns :
#                 patern.pre_generation(self.matrice_cases)

#     def post_gene_paterns(self):
#         """
#         Fonction qui postgenere les paterns
#         (on remplie les patterns)
#         """
#         if self.paterns != None:
#             for patern in self.paterns :
#                 patern.post_generation(self.matrice_cases)

#     def generation_en_profondeur(self):
#         """
#         Fonction qui génère la matrice avec la méthode du parcours en profondeur
#         Entrées:Rien
#         Sorties:une matrice de cases générée avec le parcours en profondeur
#         """
#         rdm=random.randrange (1,10**18,1)

#         #on définit la seed de notre générateur
#         #cela permet d'avoir le meme résultat
#         #rdm=851353618387733257
#         #print("seed ",rdm)
#         random.seed(rdm)

#         #print("Début de la génération")
#         #position dans la matrice
#         position = self.depart
#         #le stack est une liste de positions
#         stack=[position]
    

#         while len(stack)!=0 :
            
#             #on récupère les coords de là où l'on est cad la dernière case dans le stack
#             position = stack[len(stack)-1]
            
#             murs_generables = self.murs_utilisables(position)

#             if len(murs_generables) > 0 : 
                
#                 #randrange est exclusif
#                 num_mur=self.randomPoids(murs_generables)
                
#                 #direction du mur à casser
#                 direction_mur=murs_generables[num_mur]

#                 mur = self[position,direction_mur]

#                 self.casser_mur(mur)

#                 new_pos = mur.get_cible()
#                 #on ajoute les nouvelles coordonnées de la case au stack
#                 stack.append(new_pos)
#             else:
#                 #on revient encore en arrière
#                 stack.pop()

#         #print("Fini")

#     def murs_utilisables(self,position,murs_requis = 4):
#         """
#         Fonction qui prend en entrées:
#             les voisins de la case
#         et qui renvoie les directions ou les murs sont cassables
#         """
#         murs_utilisables=[]

#         for i in DIRECTIONS:
#             mur = self[position,i]
#             cible = mur.get_cible()
#             if cible in self.depart:
#                 case_cible = self[cible]
#                 mur_oppose = self.get_mur_oppose(mur)
#                 if mur_oppose != None and case_cible.nb_murs_pleins()>=murs_requis and mur_oppose.is_touchable() and mur.is_touchable():
#                     murs_utilisables.append(i)
#         return murs_utilisables

#     def randomPoids(self,murs_utilisables):
#         """
#         Fonction qui prend en entrée:
#             les murs utilisables par la fonction
#         et qui renvoie le numéro d'un mur générée avec un alétoire modifié
#         """

#         nbrandom=0
#         res=-1
        
#         poids_selectionnees=[]
#         poids_total=0

#         for i in range (0,len(murs_utilisables)):
#             poids_selectionnees+=[poids_total+self.poids[murs_utilisables[i]]]
#             poids_total+=self.poids[murs_utilisables[i]]

#         nbrandom=random.randrange(0,poids_total)

#         i=0

#         while i<len(poids_selectionnees) and res==-1:
#             if nbrandom < poids_selectionnees[i]:
#                 res=i
#             i+=1
#         return res

#     def casser_X_murs(self,proba=None,nbMurs=None,pourcentage=None):
#         """
#         Fonction qui doit casser des murs sur la matrice
#         on peut déterminer le nombre de murs avec un probabilité (proba*nb murs au total)
#         ou selon un nombre défini en entrée
#         ou un pourcentage
#         """
#         if proba!=None:
#             self.casser_murs_selon_proba(proba)
#         elif nbMurs!=None:
#             self.casser_murs(nbMurs)
#         elif pourcentage!=None:
#             self.casser_murs(int(pourcentage/100*self.nb_murs_total()))
#         else:
#             print("mauvaise utilisation de la fonction, on ne sait que faire")

#     def casser_murs(self,nb_murs_a_casser):
#         """
#         Fonction qui casse un certains nombre de murs aléatoirement
#         Entrées:
#             -le nombre de murs a casser
#         """
#         nb_murs_casser=0

#         while nb_murs_casser<=nb_murs_a_casser:
#             coord_case=[random.randrange(0,len(self.matrice_cases)),random.randrange(0,len(self.matrice_cases[0]))]

#             if self.casser_mur_random_case(coord_case):
#                 nb_murs_casser+=1


#     def restrictions_case(self,coord_case):
#         """
#         Fonction qui renvoie les murs intouchables
#         Entrées:
#             -les coordonnées de le case
#         Sorties:
#             -les directions ou les murs ne sont pas touchables
#         """
#         directions_interdites=[]

#         murs=self[coord_case].get_murs()
#         for i in DIRECTIONS:
#             if not(murs[i].is_touchable):
#                 directions_interdites.append(i)
            
#         return directions_interdites

#     def casser_mur_random_case(self,position_case):
#         """
#         Fonction qui prend en entrée la position de la case dont on veut casser un mur
#         et qui renvoie un booléen indiquant si l'on as pu casser un mur
#         """
#         casser = False

#         murs=self.murs_utilisables(self.voisins_case(position_case))
#         if len(murs)!=0:
#             mur_a_casser=random.randrange(0,len(murs))
#             self.casser_mur(self[position_case,murs[mur_a_casser]])
#             casser = True
#         return casser

#     def casser_murs_selon_proba(self,proba):
#         """
#         Fonction qui casse des murs selon une probabilité donnée
#         Entrée:
#             -la probabilité de casser un mur
#         """
#         for x in range(1,self.largeur) :
#             for y in range(1,self.hauteur) :
#                 pos=Position(self.depart.lab,x,y)
#                 case = self[pos]
#                 murs=self.murs_utilisables(pos,0)
#                 if HAUT in murs and random.random() <= proba :
#                     self.casser_mur(case[HAUT])
#                 if GAUCHE in murs and random.random() <= proba :
#                     self.casser_mur(case[GAUCHE])
                    
#     def casser_mur(self,mur):
#         """
#         Fonction qui casse un mur spécifique
#         Entrées:
#             la direction du mur
#             la position de la case
#         Sorites:Rien
#         """
#         #on casse les murs de la case et de la case d'en face
#         autre_mur = self.get_mur_oppose(mur)
#         if autre_mur ==  None :
#             print("On a un mur non réciproque !")
#         else :
#             mur.brise()
#             autre_mur.brise()

#     def nb_murs_total(self):
#         """
#         Fonction qui renvoie le nombres de murs pleins contenus dans le labyrinthe
#         """
#         murs_pleins=0
#         for x in range(self.largeur):
#             for y in range(self.hauteur):
#                 murs_pleins+=self[Position(self.depart.lab,x,y)].nb_murs_pleins()
        
#         return int((murs_pleins-self.hauteur*2-self.largeur*2)/2)

#     def get_mur_oppose(self,mur):
#         cible = mur.get_cible()
#         mur_oppose = None
#         if cible in self.depart:
#             for mur_potentiel in self[cible].murs :
#                 cible_potentielle = mur_potentiel.get_cible()
#                 if cible_potentielle in self.depart:
#                     if mur in self[cible_potentielle].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
#                         mur_oppose = mur_potentiel
#         return mur_oppose
