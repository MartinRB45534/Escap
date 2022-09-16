from Jeu.Labyrinthe.Pattern import *
from Jeu.Labyrinthe.Vue import *

class Espace_schematique:
    def __init__(self):
        self.frontiere:List[Cote] = []
        self.cases:List[Position] = []
        self.entrees:List[Position] = []

class Salle(Espace_schematique):
    pass

class Couloir(Espace_schematique):
    pass
