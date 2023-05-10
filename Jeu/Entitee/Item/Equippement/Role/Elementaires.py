from Jeu.Entitee.Item.Equippement.Equippement import *

class Rocheux(Equipement):
    """La classe des équipements qui augmentent l'affinité à la terre."""
    def __init__(self,position:Optional[Position]=None,taux_aff_terre:float):
        Equipement.__init__(self,position)
        self.taux_aff_terre = taux_aff_terre

class Incandescant(Equipement):
    """La classe des équipements qui augmentent l'affinité au feu."""
    def __init__(self,position:Optional[Position]=None,taux_aff_feu:float):
        Equipement.__init__(self,position)
        self.taux_aff_feu = taux_aff_feu

class Neigeux(Equipement): #"Neigeux" ? "Glaçant" ? "Glacial" ?
    """La classe des équipements qui augmentent l'affinité à la glace."""
    def __init__(self,position:Optional[Position]=None,taux_aff_glace:float):
        Equipement.__init__(self,position)
        self.taux_aff_glace = taux_aff_glace

class Tenebreux(Equipement):
    """La classe des équipements qui augmentent l'affinité à l'ombre."""
    def __init__(self,position:Optional[Position]=None,taux_aff_ombre:float):
        Equipement.__init__(self,position)
        self.taux_aff_ombre = taux_aff_ombre
