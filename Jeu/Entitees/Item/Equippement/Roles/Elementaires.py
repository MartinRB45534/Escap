from Jeu.Entitees.Item.Equippement.Equippement import *

class Rocheux(Equipement):
    """La classe des équipements qui augmentent l'affinité à la terre."""
    def __init__(self,position,taux_aff_terre):
        Equipement.__init__(self,position)
        self.taux_aff_terre = taux_aff_terre

class Incandescant(Equipement):
    """La classe des équipements qui augmentent l'affinité au feu."""
    def __init__(self,position,taux_aff_feu):
        Equipement.__init__(self,position)
        self.taux_aff_feu = taux_aff_feu

class Neigeux(Equipement): #"Neigeux" ? "Glaçant" ? "Glacial" ?
    """La classe des équipements qui augmentent l'affinité à la glace."""
    def __init__(self,position,taux_aff_glace):
        Equipement.__init__(self,position)
        self.taux_aff_glace = taux_aff_glace

class Tenebreux(Equipement):
    """La classe des équipements qui augmentent l'affinité à l'ombre."""
    def __init__(self,position,taux_aff_ombre):
        Equipement.__init__(self,position)
        self.taux_aff_ombre = taux_aff_ombre
