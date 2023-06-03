from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Equippement.Equippement import Equipement

class Rocheux(Equipement):
    """La classe des équipements qui augmentent l'affinité à la terre."""
    def __init__(self,taux_aff_terre:float):
        self.taux_aff_terre = taux_aff_terre

class Incandescant(Equipement):
    """La classe des équipements qui augmentent l'affinité au feu."""
    def __init__(self,taux_aff_feu:float):
        self.taux_aff_feu = taux_aff_feu

class Neigeux(Equipement): #"Neigeux" ? "Glaçant" ? "Glacial" ?
    """La classe des équipements qui augmentent l'affinité à la glace."""
    def __init__(self,taux_aff_glace:float):
        self.taux_aff_glace = taux_aff_glace

class Tenebreux(Equipement):
    """La classe des équipements qui augmentent l'affinité à l'ombre."""
    def __init__(self,taux_aff_ombre:float):
        self.taux_aff_ombre = taux_aff_ombre
