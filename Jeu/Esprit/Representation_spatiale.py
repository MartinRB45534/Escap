from Jeu.Labyrinthe.Pattern import *
from Jeu.Labyrinthe.Vue import *

class Espace_schematique:
    def __init__(self):
        self.frontiere:List[Cote] = []
        self.cases:List[Position] = []
        self.entrees:List[Position] = []
        self.skip = True

    def get_cases(self):
        return self.cases
    
    def get_all_cases(self):
        return self.cases+self.entrees

    def dist(self,entree1,entree2):
        if entree1 == entree2:
            return 0
        else:
            return len(self.cases)+1

class Salle(Espace_schematique):
    def __init__(self,carre:Position):
        self.frontiere:List[Cote] = []
        self.cases:List[Position] = []
        self.carres:List[Position] = [carre]
        self.entrees:List[Position] = []
        self.distances:List[List[int]] = []
        self.skip = False

    def add_cases(self):
        self.cases = []
        for case in [carre+dec for dec in Decalage(2,2) for carre in self.carres]:
            if not case in self.cases:
                self.cases.append(case)

    def make_bord(self):
        self.frontiere = [Cote(case,dir) for dir in DIRECTIONS for case in self.cases if not case + dir in self.cases]

    def calcule_distances(self):
        self.distances = []
        for i in range(len(self.entrees)):
            distances = [0]*(len(self.entrees)-i-1)
            queue = [(self.entrees[i],0)]
            visitees = self.entrees[:i+1]
            while len(queue) :
                position,distance = queue.pop(0)
                for dir in DIRECTIONS:
                    voisin = position+dir
                    if voisin in self.cases and voisin not in visitees:
                        visitees.append(voisin)
                        queue.append((voisin,distance+1))
                        if voisin in self.entrees:
                            distances[self.entrees.index(voisin)-i-1] = distance+1
            self.distances.append(distances)

    def dist(self,entree1,entree2):
        if entree1 == entree2:
            return 0
        else:
            i1,i2 = self.entrees.index(entree1),self.entrees.index(entree2)
            i,j = min(i1,i2),max(i1,i2)
            return self.distances[i][j-i-1]

class Couloir(Espace_schematique):
    def __init__(self,case:Position=None):
        self.frontiere:List[Cote] = []
        self.cases:List[Position] = [case] if case != None else []
        self.entrees:List[Position] = []
        self.skip = True
