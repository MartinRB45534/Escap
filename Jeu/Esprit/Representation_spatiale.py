from __future__ import annotations
from typing import TYPE_CHECKING, Set, Dict, List, Tuple

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Cote import Cote_position

# Pas de classe parente

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Espace_schematique:
    def __init__(self):
        self.frontiere:Set[Cote_position] = set()
        self.cases:Set[Position] = set()
        self.entrees:Set[Position] = set()
        self.skip = True

    def get_cases(self):
        return self.cases
    
    def get_all_cases(self):
        return self.cases|self.entrees

    def dist(self,entree1:Position,entree2:Position):
        if entree1 == entree2:
            return 0
        else:
            return len(self.cases)+1

class Zone_inconnue(Espace_schematique): # Représente une zone de la carte qui n'a pas encore été explorée
    def __init__(self,case:Position=ABSENT,zone=None):
        if zone is not None and not isinstance(zone,Zone_inconnue):
            print("Erreur : zone doit être une Zone_inconnue")
            zone = None
        self.cases:Set[Position] = {case} if case is not None else set()
        self.frontiere:Set[Cote_position] = set()
        self.entrees:Set[Position] = set()
        self.sorties:Set[Position] = set()
        self.occupants:Set[Agissant] = zone.occupants if zone is not None else set()
        # Copier les informations de la zone précédente
        self.skip = False

    def fusionne(self,zone):
        if isinstance(zone,Zone_inconnue):
            self.cases |= zone.cases
            self.frontiere |= zone.frontiere
            self.entrees |= zone.entrees
            self.sorties |= zone.sorties
            self.occupants |= zone.occupants
            # Copier les informations de la zone fusionnée
        else:
            print("Erreur : zone doit être une Zone_inconnue")

class Salle(Espace_schematique):
    def __init__(self,carre:Position):
        self.frontiere:Set[Cote_position] = set()
        self.cases:Set[Position] = set()
        self.carres:Set[Position] = {carre}
        self.entrees:Set[Position] = set()
        self.distances:Dict[Tuple[Position,Position],int] = {}
        self.skip = False

    def add_cases(self):
        self.cases = set()
        for case in [carre+dec for dec in Decalage(2,2) for carre in self.carres]:
            if not case in self.cases:
                self.cases.add(case)

    def make_bord(self):
        self.frontiere = {Cote_position(case,dir) for dir in DIRECTIONS for case in self.cases if case + dir not in self.cases}

    def calcule_distances(self):
        self.distances = {}
        entrees = list(self.entrees)
        for i in range(len(entrees)):
            queue:List[Tuple[Position,int]] = [(entrees[i],0)]
            visitees = [entrees[i]]
            while len(queue) :
                position,distance = queue.pop(0)
                for dir in DIRECTIONS:
                    voisin = position+dir
                    if voisin in self.cases and voisin not in visitees:
                        visitees.append(voisin)
                        queue.append((voisin,distance+1))
                        if voisin in entrees[i+1:]:
                            self.distances[(entrees[i],voisin)] = distance+1

    def dist(self,entree1:Position,entree2:Position):
        if entree1 == entree2:
            return 0
        else:
            return self.distances.get((entree1,entree2),self.distances.get((entree2,entree1),len(self.cases)+1))

class Couloir(Espace_schematique):
    def __init__(self,case:Position=ABSENT):
        self.frontiere:Set[Cote_position] = set()
        self.cases:List[Position] = [case] if case is not None else [] #Les cases d'un couloir doivent être ordonnées
        self.entrees:Set[Position] = set()
        self.skip = True
    
    def get_all_cases(self):
        return {*self.cases}|self.entrees

# Imports utilisés dans le code
from Jeu.Labyrinthe.Structure_spatiale.Decalage import Decalage
from Jeu.Labyrinthe.Structure_spatiale.Direction import DIRECTIONS
from Jeu.Labyrinthe.Structure_spatiale.Cote import Cote_position